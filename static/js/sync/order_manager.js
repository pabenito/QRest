import { Variant, Element } from './entities.js';
import {WebSocketManager} from './websocket_manager.js';

class OrderManager {
    /**
     * Crea una instancia de ElementInterface.
     * @param {string} group - El grupo para la conexión WebSocket.
     * @param {string} client - El cliente para la conexión WebSocket.
     * @param {function} showError - Función para mostrar errores.
     * @param {function} updateHTMLElement - Función para generar elementos HTML.
     */
    constructor(group, client, showError, updateHTMLElement) {
        this.showError = showError;
        this.updateHTMLElement = updateHTMLElement;

        this.websocketManager = new WebSocketManager(
            group,
            client,
            (error) => this.showError(error),
            (element) => this.updateHTMLElement(element)
        );
    }

    #updateElement(section, element, client, quantity, variants, extras, ingredients) {
        let newElement = new Element(section, element, client, quantity, variants, extras, ingredients);
        this.websocketManager.sendElement(newElement);
    }

    increaseElementQuantity(section, element, client, variants, extras, ingredients) {
        this.#updateElement(section, element, client, 1, variants, extras, ingredients);
    }

    decreaseElementQuantity(section, element, client, variants, extras, ingredients) {
        this.#updateElement(section, element, client, -1, variants, extras, ingredients);
    }
}
