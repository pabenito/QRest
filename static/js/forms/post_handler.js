import {showError} from "../utils/errorHandler";
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
