// Obtiene los elementos que se necesitan actualizar
let navbarSection = document.getElementById('section');
let navbarSubsection = document.getElementById('subsection');

// Obtiene las secciones
let sections = document.querySelectorAll('section');

// Función para actualizar el título y subtítulo en el navbar
function updateNavbarTitle(section) {
    let title = section.getAttribute('title');
    let subtitle = section.getAttribute('subtitle');

    navbarSection.innerText = title;

    if (subtitle) {
        navbarSubsection.innerText = subtitle;
        navbarSubsection.classList.remove('is-invisible');
    } else {
        navbarSubsection.classList.add('is-invisible');
    }
}

// Actualizar el título y subtítulo al cargar la página
updateNavbarTitle(sections[0]);

// Evento de scroll
document.body.addEventListener('scroll', function () {
    for (let section of sections) {
        let rect = section.getBoundingClientRect();

        if (rect.top <= 50 && rect.bottom > 50) {
            updateNavbarTitle(section);
            break;
        }
    }
});