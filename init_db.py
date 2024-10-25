from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://TwoWheelers_seasonwhen:4733bb22058b2604a82529411a7a4e8482a71916@319gf.h.filess.io:3307/TwoWheelers_seasonwhen'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class SitioTuristico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    ubicacion = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(200), nullable=True)
    horario = db.Column(db.String(50), nullable=False)
    costo = db.Column(db.Float, nullable=False)
    categoria = db.Column(db.String(50), nullable=False)

from app import app, db

with app.app_context():
    db.create_all()
    print("Tablas creadas exitosamente.")