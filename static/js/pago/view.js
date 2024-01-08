export { PayHTMLManager };
import { redirect } from '../utils/redirect.js';
import { ShowHideManager } from '../utils/showhide.js';
import { showMessage, showError } from "../utils/errorHandler.js";

class PayHTMLManager {
    constructor(modalId, urlRedirect) {
        this.modal = new ShowHideManager(modalId);
        this.urlRedirect = urlRedirect;
    }
    showError(message) {
        showError(message);
    }

    showMessage(messages) {
        showMessage(messages);
    }

    closeModal() {
        this.modal.hide();
    }

    openModal() {
        this.modal.show();
    }

    onPay() {
        this.closeModal()
        this.redirect();
    }

    redirect(){
        redirect(this.urlRedirect + "?message=Pago realizado");
    }

    reload(){
        window.location.reload();
    }
}
