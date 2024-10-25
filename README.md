# API REST para Aplicación Web Turística
# Proyecto de API REST para Sitios Turísticos

Esta aplicación es una API REST construida con Flask para manejar operaciones CRUD sobre sitios turísticos.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```
/e:/PROGRAMACION/UNIAJC/Programacion/Backend/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── forms.py
│   └── templates/
│       ├── index.html
│       ├── create.html
│       ├── update.html
│       └── delete.html
├── config.py
├── run.py
└── README.md
```

### Descripción de Archivos

- **app/__init__.py**: Inicializa la aplicación Flask y configura la base de datos.
- **app/routes.py**: Define las rutas de la aplicación y las funciones asociadas a cada ruta.
- **app/models.py**: Contiene las definiciones de los modelos de base de datos.
- **app/forms.py**: Define los formularios utilizados en las vistas HTML.
- **app/templates/index.html**: Página principal que muestra una lista de sitios turísticos.
- **app/templates/create.html**: Formulario para crear un nuevo sitio turístico.
- **app/templates/update.html**: Formulario para actualizar un sitio turístico existente.
- **app/templates/delete.html**: Confirmación para eliminar un sitio turístico.

### Requisitos

- Python 3.x
- MySQL
- Pip

### Instalación

1. Clona el repositorio:
    ```sh
    git clone https://github.com/Highlander2003/Backend
    ```
2. Navega al directorio del proyecto:
    ```sh
    cd /e:/PROGRAMACION/UNIAJC/Programacion/Backend/
    ```
3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```
4. Configura la base de datos en `config.py`.

### Ejecución

Para ejecutar la aplicación, usa el siguiente comando:
```sh
python run.py
```

### Uso

Una vez que la aplicación esté en funcionamiento, puedes acceder a las siguientes rutas:

- `/`: Página principal con la lista de sitios turísticos.
- `/create`: Crear un nuevo sitio turístico.
- `/update/<id>`: Actualizar un sitio turístico existente.
- `/delete/<id>`: Eliminar un sitio turístico.

### Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio.

                                                                 
## Requisitos

- Python 3.x
- MySQL
- Pip

