from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='frontend')

# Configuración de la base de datos MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://usuario:contraseña@localhost/nombre_base_de_datos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de datos para SitioTuristico
class SitioTuristico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    ubicacion = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(200), nullable=True)
    horario = db.Column(db.String(50), nullable=False)
    costo = db.Column(db.Float, nullable=False)
    categoria = db.Column(db.String(50), nullable=False)

# Ruta para servir el archivo index.html
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

# Ruta para servir otros archivos estáticos (CSS, JS, imágenes, etc.)
@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory(app.static_folder, path)

# Importar las rutas CRUD desde routes.py
from routes import *

if __name__ == '__main__':
    app.run(debug=True)
