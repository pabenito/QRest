import { Element } from './entities.js';
import { WebSocketManager } from './model_websocket.js';
import { ElementHTMLManager } from './view_interface.js';
import { ClientController } from '../client/controller.js';
import { LocalStorageListManager } from "../suggestion/localStorageListManager.js";

export { OrderController };

class OrderController {
    /**
     * Crea una instancia de ElementInterface.
     * @param {ElementHTMLManager} view - Manager de la vista HTML de los Elementos.
     * @param {WebSocketManager} model - WebSocket que actúa como modelo accediendo al backend.
     * @param {ClientController} clientController - Controlador de cliente.
     */
    constructor(view, model, clientController, listElementsName){
        this.view = view;
        this.model = model;
        this.clientController = clientController;
        this.localStorageListManager = undefined;
        if (listElementsName) {
            this.localStorageListManager = new LocalStorageListManager(listElementsName);
        }
        this.localStorageListManager = new LocalStorageListManager(listElementsName);
        this.model.setOnError((message) => this.view.showError(message));
        this.model.setOnMessage((element) => this.view.putElement(element));
    }

    #updateElementModel(id, section, element, client, quantity, variants, extras, ingredients) {
        let newElement = new Element(id, section, element, [client], quantity, variants, extras, ingredients);
        this.model.sendJSON(newElement);
    }

    updateElementView(element) {
        this.view.putElement(element)
    }

    showErrorView(message) {
        this.view.showError(message);
    }

    increaseElementQuantityModel(id, section, element, variants, extras, ingredients) {
        if (this.localStorageListManager && !this.localStorageListManager.hasElement(element)) {
            this.localStorageListManager.addElement(element);
        }
        if (this.clientController.hasClient())
        {
            this.#updateElementModel(id, section, element, this.clientController.getClient(), 1, variants, extras, ingredients);
        } else {
            this.clientController.showModal();
        }
    }

    decreaseElementQuantityModel(id, section, element, variants, extras, ingredients) {
        if (this.clientController.hasClient())
        {
            this.#updateElementModel(id, section, element, this.clientController.getClient(), -1, variants, extras, ingredients);
        } else {
            this.clientController.showModal();
        }
    }
}
