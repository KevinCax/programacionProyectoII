// Función para generar un código aleatorio de 8 dígitos
function generarCodigo() {
    const codigo = Math.floor(10000000 + Math.random() * 90000000); // Generar número entre 10000000 y 99999999
    document.getElementById('codigo').value = codigo; // Asignar el código generado al input
}

function cancelar() {
    Swal.fire({
        title: '¿Estás seguro?',
        text: "Todos los datos se perderán.",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, cancelar',
        cancelButtonText: 'No',
        customClass: {
            container: 'custom-swal'
        }
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = redirectUrl;  // Redirigir nuevamente a producto
        }
    })
}
