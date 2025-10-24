import os, sqlite3
from flask import Flask
from utils.database import db
from flask_migrate import Migrate

# --- Rutas absolutas seguras ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH  = os.path.join(BASE_DIR, "db.sqlite3")
SQL_PATH = os.path.join(BASE_DIR, "data.sql")

app = Flask(__name__)

# Usa ruta ABSOLUTA en SQLAlchemy (evita sorpresas con cwd)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + DB_PATH.replace("\\", "/")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET_KEY", "dev")

db.init_app(app)
migrate = Migrate(app, db)

print("Ruta absoluta de la base de datos:", DB_PATH)

def init_db():
    """Crea o completa la BD si faltan tablas (idempotente)."""
    print("Chequeando/Inicializando BD...")
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='vendedores'")
    exists = cur.fetchone() is not None
    if not exists:
        print("No hay tablas => cargando data.sql ...")
        with open(SQL_PATH, "r", encoding="utf-8") as f:
            conn.executescript(f.read())
        print("Base creada correctamente ✅")
    else:
        print("BD ya inicializada ✅")
    conn.close()

# Inicializa ANTES de registrar blueprints
with app.app_context():
    init_db()

# (después de init_db) importa y registra blueprints
from controllers.venta_controller import main_blueprint
app.register_blueprint(main_blueprint)

if __name__ == "__main__":
    app.run()

