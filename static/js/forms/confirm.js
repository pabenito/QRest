function confirm(url_post, url_redirect) {
    // Enviar la solicitud POST vacía mediante fetch
    fetch(url_post, {
        method: 'POST'
    }).then(response => {
        if (!response.ok) {
            console.log(`Error al confirmar comanda: ${response.status} ${response.text()}`);
        }
    }).then(data => {
        // Aquí puedes redirigir o manejar la respuesta como necesites
        window.location.href = url_redirect;
    }).catch(error => {
        console.error('Error:', error);
    });
}
