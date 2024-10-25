from flask import Flask, send_from_directory, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='frontend')

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sitios.db'
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

# Crear un nuevo sitio turístico (CREATE)
@app.route('/sitios', methods=['POST'])
def crear_sitio():
    datos = request.get_json()
    nuevo_sitio = SitioTuristico(
        nombre=datos['nombre'],
        ubicacion=datos['ubicacion'],
        descripcion=datos.get('descripcion', ''),
        horario=datos['horario'],
        costo=datos['costo'],
        categoria=datos['categoria']
    )
    db.session.add(nuevo_sitio)
    db.session.commit()
    return jsonify({'mensaje': 'Sitio creado exitosamente'}), 201

# Obtener todos los sitios turísticos (READ)
@app.route('/sitios', methods=['GET'])
def obtener_sitios():
    sitios = SitioTuristico.query.all()
    resultado = [
        {
            'id': sitio.id,
            'nombre': sitio.nombre,
            'ubicacion': sitio.ubicacion,
            'descripcion': sitio.descripcion,
            'horario': sitio.horario,
            'costo': sitio.costo,
            'categoria': sitio.categoria
        } for sitio in sitios
    ]
    return jsonify(resultado)

# Actualizar un sitio turístico (UPDATE)
@app.route('/sitios/<int:id>', methods=['PUT'])
def actualizar_sitio(id):
    sitio = SitioTuristico.query.get_or_404(id)
    datos = request.get_json()
    sitio.nombre = datos.get('nombre', sitio.nombre)
    sitio.ubicacion = datos.get('ubicacion', sitio.ubicacion)
    sitio.descripcion = datos.get('descripcion', sitio.descripcion)
    sitio.horario = datos.get('horario', sitio.horario)
    sitio.costo = datos.get('costo', sitio.costo)
    sitio.categoria = datos.get('categoria', sitio.categoria)
    db.session.commit()
    return jsonify({'mensaje': 'Sitio actualizado exitosamente'})

# Eliminar un sitio turístico (DELETE)
@app.route('/sitios/<int:id>', methods=['DELETE'])
def eliminar_sitio(id):
    sitio = SitioTuristico.query.get_or_404(id)
    db.session.delete(sitio)
    db.session.commit()
    return jsonify({'mensaje': 'Sitio eliminado exitosamente'})

if __name__ == '__main__':
    app.run(debug=True)