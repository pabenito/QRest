export { ShowHideManager };

class ShowHideManager {
    constructor(elementId) {
        this.id = elementId;
    }

    showHide(){
        if (this.#getElement().classList.contains("is-hidden")) {
            this.show();
        } else {
            this.hide();
        }
    }

    hide() {
        this.#getElement().classList.add("is-hidden");
    }

    show() {
        this.#getElement().classList.remove("is-hidden");
    }

    #getElement(){
        return document.getElementById(this.id);
    }
}