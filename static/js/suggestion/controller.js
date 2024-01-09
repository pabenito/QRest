import {SuggestionHTML} from "./view.js";

export class SuggestionController {
    /**
     * Crea una instancia de SuggestionController.
     * @param {SuggestionHTML} view - Manager de la vista HTML.
     * @param {LocalStorageListManager} model - Actúa como modelo de persistencia de la lista.
     */
    constructor(view, model) {
        this.view = view;
        this.model = model;
    }

    setSuggestions(){
        for (let suggestion of this.model.getList()) {
            this.view.putSuggestion(suggestion);
        }
    }
}