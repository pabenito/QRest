function post_handler(url_post, url_redirect) {
    // Enviar la solicitud POST vacía mediante fetch
    fetch(url_post, {
        method: 'POST'
    })
    .then(response => {
        if (!response.ok) {
            // Si la respuesta no es OK, lanzar un error
            return response.text().then(text => {
                throw new Error(`${response.status} ${text}`);
            });
        }
        // Si la respuesta es exitosa, redirigir
        window.location.href = url_redirect;
    })
    .catch(error => {
        console.error(error);

        // Extrae la parte JSON del mensaje de error
        const jsonPart = error.message.match(/\{.*\}/);
        if (jsonPart) {
            try {
                // Intenta parsear la parte JSON y obtener el mensaje
                const errorObj = JSON.parse(jsonPart[0]);
                showError(errorObj.message);
            } catch (parseError) {
                // Si hay un error al parsear, muestra el mensaje de error original
                showError(error.message);
            }
        } else {
            // Si no se encuentra JSON en el mensaje, muestra el mensaje de error original
            showError(error.message);
        }
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
