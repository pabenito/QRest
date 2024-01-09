export class SuggestionHTML {
  putSuggestion(elementId) {
    let tags = document.getElementById("tags_" + elementId);
    tags.classList.remove("is-hidden");
    tags.appendChild(this.#createSuggestion());
  }

  #createSuggestion() {
    // Crear el elemento span principal con clase 'tag' y 'is-rounded'
    var suggestion = document.createElement("span");
    suggestion.className = "tag is-rounded";

    // Crear el span interno para el ícono
    var iconSpan = document.createElement("span");
    iconSpan.className = "icon";

    // Crear el elemento i para el ícono de Font Awesome
    var icon = document.createElement("i");
    icon.className = "fas fa-repeat";

    // Añadir el ícono (i) al span del ícono
    iconSpan.appendChild(icon);

    // Añadir el span del ícono al elemento principal (suggestion)
    suggestion.appendChild(iconSpan);

    // Crear el span para el texto
    var textSpan = document.createElement("span");
    textSpan.className = "is-size-7 is-capitalized ml-1";
    textSpan.textContent = "Repite";

    // Añadir el span del texto al elemento principal (suggestion)
    suggestion.appendChild(textSpan);

    return suggestion;
  }
}
