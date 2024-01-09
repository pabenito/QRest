export class LocalStorageListManager {
    constructor(listName) {
        this.listName = listName;
    }

    // Agrega un elemento a la lista
    addElement(element) {
        let list = this.getList();
        list.push(element);
        localStorage.setItem(this.listName, JSON.stringify(list));
    }

    // Elimina un elemento de la lista
    removeElement(element) {
        let list = this.getList();
        const index = list.indexOf(element);
        if (index > -1) {
            list.splice(index, 1);
            localStorage.setItem(this.listName, JSON.stringify(list));
        }
    }

    // Comprueba si un elemento está en la lista
    hasElement(element) {
        let list = this.getList();
        return list.includes(element);
    }

    // Obtiene la lista completa
    getList() {
        let list = JSON.parse(localStorage.getItem(this.listName));
        return list ? list : [];
    }

    // Elimina toda la lista
    clearList() {
        localStorage.removeItem(this.listName);
    }
}
