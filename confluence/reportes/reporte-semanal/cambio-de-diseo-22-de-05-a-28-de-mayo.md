# Cambio de diseño | 22 de 05 a 28 de Mayo

## 📋 Resumen

Se ha cambiado el dieño anterior de la carta, que estaba muy cargado de elementos y era muy complejo, por un diseño muy parecido al de Qamarero [https://pedrobenito.atlassian.net/wiki/spaces/QRest/pages/294938](https://pedrobenito.atlassian.net/wiki/spaces/QRest/pages/294938).

## ?? Estado del proyecto



> ### Logros
- Cambiar el diseño para que se parezca al de Qamarero
- Añadir el JS necesario para que lar carta sea interactiva y dinámica:
- Contadores
- Scroll automático a secciones del índice
- Actualización del navbar cuando la sección llegar al navbar
- Simplificar JS con atributos: 
- Antes: Todo se hacía con ids toda la lógica, eventos, etc. desde JS. Había mucha duplicidad de codigo y era más complejor. Todo estaba hardcodeado.
- Ahora: Se utilizan atributos del html y llamadas a funciones desde el elemento en cuestión `funcion(event)`  y desde el JS en función de los atributos del elemento se modifican unos u otros elementos. La función es genérica y reutilizable.  
- Alternativas de nombres para la aplicación: Clickmanda, QRápido, AlaMesa.
> ### Incidencias del proyecto y riesgos
Hay que ver hasta qué punto es legal haber copiado el diseño de Qamarero. 

> ### Mejoras propuestas
> ### Aprendizajes
- Se puede usar la clase “containter” de Bulma para quitar restricciones de otras clases, por ejemplo en un footer de un modal, que tiene un estilo concreto puedes poner un “containter” para que no te afecte el formato del footer. 
- Se pueden usar atributos de los elementos del HTML para hacer que los elementos llamen a una función genérica con el evento y que se cojan los atributos desde el JS. Simplifica mucho el código.
- El evento scroll no se da en la ventana (window) sino en el body (document.body)
- Si tienes un botón dentro de un formulario y no quieres que se use como trigger para la acción del formulario tienes que especificar el tipo type=”button”, sino se supone que es type=”submit”.
- Si un evento no está funcionando puedes poner `event.preventDefault();` también es conveniente usar `event.currentTarget` en ves de `event.target` porque por ejemplo si tienes un icono dentro de un botón y se dispara el evento pulsando sobre el icono, `event.target` te dará el icono, no el botón, mientras que current `event.currentTarget` sí te dará el botón. 


