from app import db

class SitioTuristico(db.Model):
    __tablename__ = 'sitios'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    ubicacion = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    horario = db.Column(db.String(50), nullable=False)
    costo = db.Column(db.Integer, nullable=False)
    categoria = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Sitio {self.nombre}>'
