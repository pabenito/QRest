export {WebSocketManager};

class WebSocketManager {
    /**
     * Crea una instancia de WebSocketManager.
     * @param {string} URL - URL para la conexión WebSocket.
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
        console.log(error);
        if (this.onError) {
            this.onError(`WebSocket Error: ${error.message}`);
        }
    }

    #handleClose(event) {
        console.log("WebSocket closed", event);
    }

    #handleMessage(message) {
        try {
            if (this.onMessage) {
                let parsedMessage = JSON.parse(message.data);
                if ("type" in parsedMessage && parsedMessage.type === "error") {
                    this.#handleError(parsedMessage);
                } else {
                    this.onMessage(parsedMessage);
                }
            }
        } catch (e) {
            this.#handleError(e);
        }
    }
}