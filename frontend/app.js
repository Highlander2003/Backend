document.getElementById('sitioForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const nombre = document.getElementById('nombre').value;
    const ubicacion = document.getElementById('ubicacion').value;
    const descripcion = document.getElementById('descripcion').value;
    const horario = document.getElementById('horario').value;
    const costo = document.getElementById('costo').value;
    const categoria = document.getElementById('categoria').value;

    const response = await fetch('/sitios', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            nombre,
            ubicacion,
            descripcion,
            horario,
            costo,
            categoria
        })
    });

    const data = await response.json();
    alert(data.mensaje);
    document.getElementById('sitioForm').reset();
});

function obtenerSitios() {
    fetch('/sitios')
    .then(response => response.json())
    .then(data => {
        const sitiosList = document.getElementById('sitiosList');
        sitiosList.innerHTML = '';
        data.forEach(sitio => {
            const li = document.createElement('li');
            li.textContent = `${sitio.nombre} - ${sitio.ubicacion}`;
            sitiosList.appendChild(li);
        });
    });
}

document.addEventListener('DOMContentLoaded', obtenerSitios);