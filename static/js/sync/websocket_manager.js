class WebSocketManager {
    /**
     * Crea una instancia de WebSocketManager.
     * @param {string} group - El grupo para la conexión WebSocket.
     * @param {string} client - El cliente para la conexión WebSocket.
     * @param {function} onError - Función a llamar en caso de error.
     * @param {function} onElementReceived - Función a llamar cuando se recibe un Elemento.
     */
    constructor(group, client, onError, onElementReceived) {
        this.ws = new WebSocket(`ws://localhost:8000/ws/mesa/${group}/client/${client}`);
        this.ws.onerror = (error) => this.#handleError(error);
        this.ws.onclose = (event) => this.#handleClose(event);
        this.ws.onmessage = (message) => this.#handleMessage(message);

        this.onError = onError;
        this.onElementReceived = onElementReceived;
    }

    /**
     * Envia un elemento al WebSocket.
     * @param {Element} element - El elemento a enviar.
     */
    sendElement(element) {
        if (this.ws.readyState === WebSocket.OPEN) {
            this.ws.send(JSON.stringify(element));
        } else {
            console.error("WebSocket is not open");
        }
    }

    #handleError(error) {
        if (this.onError) {
            this.onError(`WebSocket Error: ${error.message}`);
        }
    }

    #handleClose(event) {
        console.log("WebSocket closed", event);
    }

    #handleMessage(message) {
        try {
            const element = JSON.parse(message.data);
            if (this.onElementReceived) {
                this.onElementReceived(element);
            }
        } catch (e) {
            this.#handleError(e);
        }
    }
}