uvifunction show(event) {
    event.preventDefault();
    let buttonElement = event.currentTarget;
    let showId = buttonElement.getAttribute('show');

    let showElement = document.getElementById(showId);
    showElement.classList.remove("is-hidden");
}

function set(event) {
    event.preventDefault();
    let element = event.currentTarget;
    let toId = element.getAttribute('set_to');
    let value = element.getAttribute('set_value');
    let toElement = document.getElementById(toId);
    toElement.value = value
}

function hide(event) {
    event.preventDefault();
    let buttonElement = event.currentTarget;
    let hideId = buttonElement.getAttribute('hide');

    let hideElement = document.getElementById(hideId);
    hideElement.classList.add("is-hidden");
}

function removeElement(event) {
    event.preventDefault();
    let buttonElement = event.currentTarget;
    let id = buttonElement.getAttribute('remove');
    let element = document.getElementById(id);
    element.remove();
    id = buttonElement.getAttribute('remove_hr');
    element = document.getElementById(id);
    element.remove(id);
}

function decrementValue(event, remove=false) {
    event.preventDefault();
    let buttonElement = event.currentTarget;
    let targetInput = buttonElement.getAttribute('to');

    let inputElement = document.getElementById(targetInput);
    let inputValue = Number(inputElement.value);

    if (inputValue > 0) {
        inputElement.value = inputValue - 1;

        // Hide counter and show addElement when value reaches 0
        if (inputElement.value == 0) {
            if (remove) {
                removeElement(event);
            } else {
                hide(event);
            }
            show(event);
        }
    }
}

function incrementValue(event) {
    event.preventDefault();
    let buttonElement = event.currentTarget;
    let targetInput = buttonElement.getAttribute('to');

    let inputElement = document.getElementById(targetInput);
    let inputValue = Number(inputElement.value);

    inputElement.value = inputValue + 1;
}

function addTo(event) {
    event.preventDefault();
    let buttonElement = event.currentTarget;
    let fromInput = buttonElement.getAttribute('add_from');
    let toInput = buttonElement.getAttribute('add_to');

    let fromElement = document.getElementById(fromInput);
    let fromValue = Number(fromElement.value);
    let toElement = document.getElementById(toInput);
    let toValue = Number(toElement.value);

    toElement.value = toValue + fromValue;
}