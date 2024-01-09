import { ShowHideManager } from '../utils/showhide.js';

export { ClientController };

class ClientController {
    constructor(modalId, inputId, onSet) {
        this.#setModal(modalId);
        this.#setInput(inputId);
        this.onSet = onSet;
        this.setClientFromLocalStorage();
    }

    #setModal(modal){
        this.modal = new ShowHideManager(modal);
    }

    #setInput(inputId){
        this.inputId = inputId;
    }

    #getModal(){
        return this.modal;
    }

    #getInput(){
        return document.getElementById(this.inputId);
    }

    #setClient(client){
        this.client = client;
        if (this.onSet) {
            this.onSet(this.client);
        }
    }

    showModal() {
        this.#getModal().show();
    }

    setClientFromLocalStorage() {
        const clientFromStorage = localStorage.getItem('client');
        if (clientFromStorage) {
            this.#setClient(clientFromStorage);
        }
    }

    setClientFromModal() {
        const inputElement = this.#getInput();
        if (inputElement && inputElement.value.length > 0) {
            this.#setClient(inputElement.value);
            localStorage.setItem('client', this.client);
            this.#getModal().hide();
        } else {
            this.#showError("No se ha introducido ningún nombre");
        }
    }

    hasClient() {
        return this.client !== undefined;
    }

    getClient() {
        return this.client;
    }

    #showError(message) {
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
}
