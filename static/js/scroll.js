window.doScroll = function doScroll(event) {
    event.preventDefault(); // Evita que se produzca el comportamiento de enlace predeterminado
    modalSeccionesClose();
    var toValue = event.target.getAttribute("to"); // Obtiene el valor del atributo "to"
    var elementoDestino = document.getElementById(toValue); // Selecciona el elemento destino
    if (elementoDestino) {
        elementoDestino.scrollIntoView({ behavior: "smooth" }); // Hace scroll al elemento destino
    } else {
        console.log('elementoDestino not found'); // Mensaje si elementoDestino no se encuentra
    }
}