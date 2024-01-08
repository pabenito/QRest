import { WebSocketManager } from './model_websocket.js';
import { PayHTMLManager } from './view.js';

export { PayController };

class PayController {
    /**
     * Crea una instancia de ElementInterface.
     * @param {PayHTMLManager} view - Manager de la vista HTML de los Elementos.
     * @param {WebSocketManager} model - WebSocket que actúa como modelo accediendo al backend.
     */
    constructor(view, model) {
        this.view = view;
        this.model = model;
        this.model.setOnError((message) => this.view.showError(message));
        this.model.setOnMessage((element) => this.view.onPay());
    }

    waitForPayment(elements) {
        this.view.openModal();
        this.model.sendJSON(elements);
    }
}
