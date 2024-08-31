function guardarProducto() {
    // Obtener los valores del formulario
    const codigo = document.getElementById('codigo').value;
    const cantidad = document.getElementById('cantidad').value;
    const descripcion = document.getElementById('descripcion').value;
    const categoria = document.getElementById('categoria').value;
    const precioUnitario = document.getElementById('precio-unitario').value;
    const costoUnitario = document.getElementById('costo-unitario').value;

    // Crear un objeto con los datos
    const productoData = {
        codigo: codigo,
        cantidad: cantidad,
        descripcion: descripcion,
        categoria: categoria,
        precio_unitario: precioUnitario,
        costo_unitario: costoUnitario
    };

    // Enviar la solicitud POST al servidor
    fetch("{% url 'agregar_producto' %}", {
        method: 'POST',  // Método POST
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,  // Token CSRF
        },
        body: JSON.stringify(productoData)  // Enviar los datos en formato JSON
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Error en la respuesta del servidor');
        }
        return response.json();  // Convertir la respuesta a JSON
    })
    .then(data => {
        if (data.status === 'success') {
            Swal.fire({
                title: 'Producto guardado',
                text: data.message,
                icon: 'success',
                confirmButtonText: 'Ingresar otro'
            }).then((result) => {
                if (result.isConfirmed) {
                    // Limpiar el formulario
                    document.getElementById('agregar-producto-form').reset();
                }
            });
        } else {
            Swal.fire({
                title: 'Error',
                text: data.message,
                icon: 'error',
                confirmButtonText: 'OK'
            });
        }
    })
    .catch(error => {
        Swal.fire({
            title: 'Error',
            text: error.message,
            icon: 'error',
            confirmButtonText: 'OK'
        });
    });
}
