# API | 10 de Marzo al 22 de Marzo

## 📋 Resumen

Corregir errores del prototipo, hacer la API y testearla.

## ?? Estado del proyecto



> ### Logros
- Corregir bugs del prototipo:
- Modal no sale en medio de la pantalla. 
- Solución: Sacar fuera de `box` el modal. 
- Texto de modal no hace salto de línea.
- Solución: Quitar `is-narrow` de la columna.
- Cuando el texto es de distinto tamaño no están alineados los checkbox.
- Solución: Usar `level`.
Añadir mejoras prototipo:
- Duplicar el plato a partir del Panel de pedido
- Se ha añadido un botón.
- Cambiar iconos de sección
- Como no podía usar FontAwesome me he descargado los iconos de [https://icon-icons.com/es/pack/Food---Line/3274](https://icon-icons.com/es/pack/Food---Line/3274) 
- Añadir colores a los alérgenos:
- He descargado los iconos de [https://icon-icons.com/es/buscar/iconos/alergenos](https://icon-icons.com/es/buscar/iconos/alergenos)
- API de la Carta
- Test de la API
> ### Incidencias del proyecto y riesgos
- El solucionar el bug de *Modal no sale en medio de la pantalla *ha surgido el problema de que si pones los modales fuera del `box` ¿Cómo haces el formulario de ese elemento de la carta?
- La solución es que si todos los campos están en un modal desplegables fuera del `box` se puede hacer un `form` que agrupe los modales.
