export class WebSocketManager {
    /**
     * Crea una instancia de WebSocketManager.
     * @param {string} URL - URL para la conexión WebSocket.
     * @param {function} onError - Función a llamar en caso de error.
     * @param {function} onMessage - Función a llamar cuando se recibe un Elemento.
     */
    constructor(URL) {
        this.ws = new WebSocket(URL);
        this.ws.onerror = (error) => this.#handleError(error);
        this.ws.onclose = (event) => this.#handleClose(event);
        this.ws.onmessage = (message) => this.#handleMessage(message);
    }

    setOnError(onError) {
        this.onError = onError;
    }

    setOnMessage(onMessage) {
        this.onMessage = onMessage;
    }

    sendJSON(element) {
        if (this.ws.readyState === WebSocket.OPEN) {
            this.ws.send(JSON.stringify(element));
        } else {
            console.error("WebSocket is not open");
        }
    }

    #handleError(error) {
        if (this.onError) {
            this.onError(`WebSocket Error: ${error.message}`);
        } else {
            console.log(`WebSocket Error: ${error.message}`)
        }
    }

    #handleClose(event) {
        console.log("WebSocket closed", event);
    }

    #handleMessage(message) {
        try {
            const element = JSON.parse(message.data);
            if (this.onMessage) {
                this.onMessage(element);
            }
        } catch (e) {
            this.#handleError(e);
        }
    }
}