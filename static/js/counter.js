function show(event) {
    event.preventDefault();
    let buttonElement = event.currentTarget;
    let showId = buttonElement.getAttribute('show');

    let showElement = document.getElementById(showId);
    showElement.classList.remove("is-hidden");

    // Automatically increase the value to 1 upon showing the counter
    let targetInput = buttonElement.getAttribute('to');
    let inputElement = document.getElementById(targetInput);
    inputElement.value = 1;
}

function hide(event) {
    event.preventDefault();
    let buttonElement = event.currentTarget;
    let hideId = buttonElement.getAttribute('hide');

    let hideElement = document.getElementById(hideId);
    hideElement.classList.add("is-hidden");
}

function decrementValue(event) {
    event.preventDefault();
    let buttonElement = event.currentTarget;
    let targetInput = buttonElement.getAttribute('to');

    let inputElement = document.getElementById(targetInput);
    let inputValue = Number(inputElement.value);

    if (inputValue > 0) {
        inputElement.value = inputValue - 1;

        // Hide counter and show addElement when value reaches 0
        if (inputElement.value == 0) {
            hide(event);
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