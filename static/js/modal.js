function createModal(modalId) {
    return Bulma.create('modal', {
        element: document.querySelector(`#${modalId}`)
    });
}

// Obtén todos los elementos con la clase 'modal'
var modals = document.getElementsByClassName('modal');

// Para cada modal, crea un modal de Bulma
for (var i = 0; i < modals.length; i++) {
    var modalId = modals[i].id;
    window[modalId] = createModal(modalId);
}
