export { Variant, Element };
class Variant {
    /**
     * @param {string} name
     * @param {string} value
     */
    constructor(name, value) {
        this.name = name;
        this.value = value;
    }
}

class Element {
    /**
     * Crea una instancia de Element.
     * @param {string} id - El identificador del elemento.
     * @param {string} section - La sección del elemento.
     * @param {string} element - El nombre del elemento.
     * @param {string[]} clients - Los clientes asociados con el elemento.
     * @param {number} quantity - La cantidad del elemento.
     * @param {Variant[]} [variants] - Las variantes del elemento, opcional.
     * @param {string[]} [extras] - Información extra sobre el elemento, opcional.
     * @param {string[]} [ingredients] - Los ingredientes del elemento, opcional.
     */
    constructor(id, section, element, clients, quantity, variants, extras, ingredients) {
        this.id = id;
        this.section = section;
        this.element = element;
        this.clients = clients;
        this.quantity = quantity;
        if (variants !== undefined) {
            this.variants = variants;
        }
        if (extras !== undefined) {
            this.extras = extras;
        }
        if (ingredients !== undefined) {
            this.ingredients = ingredients;
        }
    }
}
