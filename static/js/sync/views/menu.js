import { ElementHTMLManager } from '../view_interface.js';

export { MenuElementHTMLManager };

class MenuElementHTMLManager extends ElementHTMLManager{
    constructor() {
        super();
    }

    showError(message) {
        const notification = document.createElement('div');
        notification.className = 'notification is-danger';
        notification.textContent = message;
        document.body.appendChild(notification);

        // Opcional: Cerrar la notificación después de un tiempo
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 3000);
    }

    putElement(element){
        const elementCounter = document.getElementById(`quantity_${element.id}`);
        if (elementCounter) {
            if (element.quantity > 0) {
                elementCounter.value = element.quantity;
            } else {
                document.getElementById(element.id).remove();
            }
        } else {
            this.#generateElement(element);
        }
    }

    #generateElement(element) {
        // Crear div principal
        const elementDiv = document.createElement('div');
        elementDiv.className = 'columns is-multiline m-0 is-mobile is-vcentered';
        
        // Añadir imagen
        const imageDiv = this.#createElementImage(element);
        elementDiv.appendChild(imageDiv);

        // Añadir detalles del elemento
        const detailsDiv = this.#createElementDetails(element);
        elementDiv.appendChild(detailsDiv);

        // Añadir control de cantidad
        const quantityControlDiv = this.#createQuantityControl(element);
        elementDiv.appendChild(quantityControlDiv);

        this.elementsContainer.appendChild(elementDiv);
    }

    #createElementImage(element) {
        const imgDiv = document.createElement('div');
        imgDiv.className = 'column is-narrow';
        const figure = document.createElement('figure');
        figure.className = 'image is-96x96';
        const img = document.createElement('img');
        img.className = 'has-rounded-border';
        img.src = element.image || 'https://bulma.io/images/placeholders/96x96.png';
        figure.appendChild(img);
        imgDiv.appendChild(figure);
        return imgDiv;
    }

    #createElementDetails(element) {
        const detailsDiv = document.createElement('div');
        detailsDiv.className = 'column';
        
        // Título
        const title = document.createElement('p');
        title.className = 'title is-size-5 m-0 is-underlined is-word-unbreakable has-text-centered';
        title.textContent = element.element;
        detailsDiv.appendChild(title);

        // Detalles (variantes, extras, ingredientes)
        const details = this.#createDetails(element);
        detailsDiv.appendChild(details);

        return detailsDiv;
    }

    #createDetails(element) {
        const detailsDiv = document.createElement('div');
        detailsDiv.className = 'columns is-multiline m-0 is-mobile is-vcentered is-centered';
        
        // Variantes, Extras, Ingredientes
        if (element.variants) {
            detailsDiv.appendChild(this.#createDetailColumn(element.variants, ''));
        }
        if (element.extras) {
            detailsDiv.appendChild(this.#createDetailColumn(element.extras, '+'));
        }
        if (element.ingredients) {
            detailsDiv.appendChild(this.#createDetailColumn(element.ingredients, '-'));
        }

        return detailsDiv;
    }

    #createDetailColumn(items, prefix) {
        const columnDiv = document.createElement('div');
        columnDiv.className = 'column is-narrow';
        items.forEach(item => {
            const p = document.createElement('p');
            p.className = 'subtitle is-size-5 m-0 is-unbreakable';
            p.textContent = prefix + item;
            columnDiv.appendChild(p);
        });
        return columnDiv;
    }

    #createQuantityControl(element) {
        const quantityDiv = document.createElement('div');
        quantityDiv.className = 'column is-narrow';
        const field = document.createElement('div');
        field.className = 'field has-addons';
        quantityDiv.appendChild(field);

        // Botón de decremento
        const decrementButton = this.#createButton('is-danger', 'fa-minus', element, true);
        field.appendChild(decrementButton);

        // Input de cantidad
        const input = document.createElement('input');
        input.id = `quantity_${element.id}`;
        input.className = 'input';
        input.type = 'number';
        input.min = '0';
        input.value = element.quantity;
        input.readOnly = true;
        const inputControl = document.createElement('div');
        inputControl.className = 'control';
        inputControl.appendChild(input);
        field.appendChild(inputControl);

        // Botón de incremento
        const incrementButton = this.#createButton('is-success', 'fa-plus', element, false);
        field.appendChild(incrementButton);

        return quantityDiv;
    }

    #createButton(colorClass, iconClass, element, isDecrement) {
        const button = document.createElement('button');
        button.className = `button ${colorClass}`;
        button.onclick = (event) => isDecrement ? this.decrementValue(event, element) : this.incrementValue(event, element);

        const span = document.createElement('span');
        span.className = 'icon';
        const i = document.createElement('i');
        i.className = `fas ${iconClass}`;
        span.appendChild(i);
        button.appendChild(span);

        return button;
    }
}
