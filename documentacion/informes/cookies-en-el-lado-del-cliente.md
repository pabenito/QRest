# Cookies en el lado del cliente

# Informe: Almacenamiento Local de Información de Alérgenos en Aplicación Web

## Objetivo

El objetivo de este informe es analizar las diferentes opciones para almacenar información de alérgenos de manera local en el dispositivo de un usuario utilizando tecnologías web, especialmente JavaScript. Queremos evitar el envío de esta información al servidor y mantener la información de alérgenos persistente incluso cuando se recarga la página.

## Opciones de Almacenamiento Local

Existen varias formas de almacenar información en el navegador del usuario. Las siguientes son las opciones más comunes:

1. **LocalStorage**: Permite almacenar datos en pares clave-valor, con una capacidad de almacenamiento de alrededor de 5-10MB.
2. **IndexedDB**: Es una base de datos NoSQL en el lado del cliente que permite guardar una gran cantidad de datos y datos más complejos.
3. **Web SQL Database (Deprecado)**: Una API web para almacenar datos en bases de datos SQL en el cliente. Fue deprecada y no se recomienda su uso.
4. **Cookies**: Permiten almacenar una cantidad pequeña de datos en el navegador del usuario.
5. **Cache API**: Permite guardar y recuperar recursos de red, beneficiando el rendimiento de la aplicación.
6. **API File System Access (Limitado)**: Permite leer y escribir archivos en el dispositivo del usuario, pero la compatibilidad con los navegadores es limitada.

## Análisis de Opciones

Para el caso específico de almacenar la información de alérgenos del usuario, algunas opciones pueden descartarse inmediatamente. Las cookies y la Cache API no son adecuadas para este tipo de datos. Web SQL está deprecado, y la API File System Access tiene una compatibilidad limitada con los navegadores.

Esto nos deja con LocalStorage e IndexedDB. Ambas opciones nos permiten almacenar los datos en el lado del cliente y persistir los datos incluso cuando se recarga la página. 

IndexedDB es una base de datos más compleja y puede manejar una gran cantidad de datos, pero para nuestro caso, la información de alérgenos es relativamente simple y no es grande en tamaño, por lo que el uso de IndexedDB podría ser excesivo.

## Decisión

Basado en el análisis, **LocalStorage** parece ser la mejor opción para este caso. 

La información de alérgenos puede representarse como un objeto simple de JavaScript con pares clave-valor, y el tamaño de los datos no excede la capacidad de almacenamiento de LocalStorage. Además, LocalStorage es compatible con todos los principales navegadores y es fácil de usar.

Aunque LocalStorage no es seguro para almacenar datos sensibles, la información de alérgenos no se considera datos sensibles. Sin embargo, es importante informar al usuario de que su información de alérgenos se almacenará en su dispositivo.

## Código de Ejemplo

El siguiente es un ejemplo de cómo se puede usar LocalStorage para almacenar y recuperar la información de alérgenos del usuario:

```html 
<!DOCTYPE html>
<html>
<head>
  <title>Alérgenos</title>
</head>
<body>

<h1>Por favor, selecciona tus alérgenos:</h1>

<form id="alergenosForm">
  <input type="checkbox" id="celery" name="celery"> Apio<br>
  <input type="checkbox" id="gluten" name="gluten"> Gluten<br>
  <input type="checkbox" id="crustaceans" name="crustaceans"> Crustáceos<br>
  <input type="checkbox" id="eggs" name="eggs"> Huevos<br>
  <input type="checkbox" id="fish" name="fish"> Pescado<br>
  <input type="checkbox" id="lupin" name="lupin"> Altramuz<br>
  <input type="checkbox" id="milk" name="milk"> Leche<br>
  <input type="checkbox" id="molluscs" name="molluscs"> Moluscos<br>
  <input type="checkbox" id="mustard" name="mustard"> Mostaza<br>
  <input type="checkbox" id="nuts" name="nuts"> Frutos secos<br>
  <input type="checkbox" id="peanuts" name="peanuts"> Cacahuetes<br>
  <input type="checkbox" id="sesame" name="sesame"> Sésamo<br>
  <input type="checkbox" id="soybeans" name="soybeans"> Soja<br>
  <input type="checkbox" id="sulphur" name="sulphur"> Dióxido de azufre y sulfitos<br>
</form>

<script>
  const allergens = [
    "celery", "gluten", "crustaceans", "eggs", "fish", 
    "lupin", "milk", "molluscs", "mustard", "nuts", 
    "peanuts", "sesame", "soybeans", "sulphur"
  ];

  document.addEventListener("DOMContentLoaded", function() {
    allergens.forEach(function(allergen) {
      const savedAllergen = JSON.parse(localStorage.getItem(allergen));
      
      if(savedAllergen) {
        document.getElementById(allergen).checked = true;
      }
    });
  });

  allergens.forEach(function(allergen) {
    const checkbox = document.getElementById(allergen);
    
    checkbox.addEventListener('change', function() {
      localStorage.setItem(allergen, JSON.stringify(checkbox.checked));
    });
  });
</script>

</body>
</html>
```

Este código HTML y JavaScript creará una lista de casillas de verificación para cada alérgeno. Cuando el usuario marque o desmarque una casilla de verificación, su estado se guardará en LocalStorage. Cuando se recargue la página, el código JavaScript leerá los datos de LocalStorage y actualizará el estado de las casillas de verificación en consecuencia.
