function showHide(id){
    let element = document.getElementById(id);
    if (element.classList.contains("is-hidden")) {
        showElement(id);
    } else {
        hideElement(id);
    }
}

function hideElement(id) {
    let element = document.getElementById(id);
    element.classList.add("is-hidden");
}

function showElement(id) {
    let element = document.getElementById(id);
    element.classList.remove("is-hidden");
}