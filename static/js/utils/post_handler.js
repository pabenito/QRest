function post_handler(url_post, url_redirect) {
    // Enviar la solicitud POST vacía mediante fetch
    fetch(url_post, {
        method: 'POST'
    }).then(response => {
        if (!response.ok) {
            console.log(`Error: ${response.status} ${response.text()}`);
            showError(`Error: ${response.status} ${response.text()}`);
        }
    }).then(data => {
        // Aquí puedes redirigir o manejar la respuesta como necesites
        window.location.href = url_redirect;
    }).catch(error => {
        console.error('Error:', error);
        showError(`Error: ${error}`);
    });
}

function showError(message) {
    const notification = document.createElement('div');
    notification.className = 'notification is-danger';
    notification.textContent = message;
    notification.style.position = 'fixed'; // Posicionamiento fijo
    notification.style.left = '50%'; // Centrar horizontalmente
    notification.style.top = '50%'; // Centrar verticalmente
    notification.style.transform = 'translate(-50%, -50%)'; // Ajuste de la posición
    notification.style.zIndex = '1000'; // Asegurarse de que está encima de otros elementos
    notification.style.width = 'auto'; // El ancho se ajusta al contenido
    notification.style.maxWidth = '100%'; // Prevenir que la notificación sea más ancha que la pantalla
    notification.style.boxSizing = 'border-box'; // El padding y el borde se incluyen en el ancho y la altura
    notification.style.padding = '1rem'; // Añadir algo de padding para que no esté pegado al texto

    document.body.appendChild(notification);

    // Opcional: Cerrar la notificación después de un tiempo
    setTimeout(() => {
        document.body.removeChild(notification);
    }, 3000);
}
