function confirm(event) {
    // Prevenir el comportamiento por defecto del formulario
    event.preventDefault();

    // Preparar la URL para la solicitud POST
    let url = event.target.action;

    // Enviar la solicitud POST vacía mediante fetch
    fetch(url, {
        method: 'POST'
    }).then(response => {
        if (!response.ok) {
            console.log(`Error al confirmar comanda: ${response.status} ${response.text()}`);
        }
    }).then(data => {
        // Aquí puedes redirigir o manejar la respuesta como necesites
        window.location.href = url;
    }).catch(error => {
        console.error('Error:', error);
    });
}
