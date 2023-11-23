import { Element } from './entities.js';
import { WebSocketManager } from './model_websocket.js';
import { ElementHTMLManager } from './view_interface.js';

export { OrderController };

class OrderController {
    /**
     * Crea una instancia de ElementInterface.
     * @param {ElementHTMLManager} view - Manager de la vista HTML de los Elementos.
     * @param {WebSocketManager} model - WebSocket que actúa como modelo accediendo al backend.
     */
    constructor(view, model) {
        this.view = view;
        this.model = model;
        this.model.setOnError((message) => this.view.showError(message));
        this.model.setOnMessage((element) => this.view.putElement(element));
    }

    #updateElementModel(section, element, client, quantity, variants, extras, ingredients) {
        let newElement = new Element(section, element, [client], quantity, variants, extras, ingredients);
        this.model.sendJSON(newElement);
    }

    updateElementView(element) {
        this.view.putElement(element)
    }

    showErrorView(message) {
        this.view.showError(message);
    }

    increaseElementQuantityModel(section, element, client, variants, extras, ingredients) {
        this.#updateElementModel(section, element, client, 1, variants, extras, ingredients);
    }

    decreaseElementQuantityModel(section, element, client, variants, extras, ingredients) {
        this.#updateElementModel(section, element, client, -1, variants, extras, ingredients);
    }
}
