# Sprints

## Confluence

Del 2 de Febrero al 17 de Febrero:  Anteproyecto

Del 18 de Febrero al 23 de Febrero: Preparación entorno de desarrollo, definición de sprints y modelo del sistema

Del 24 de Febrero al 9 de Marzo: Redefinición de sprints, [https://pedrobenito.atlassian.net/wiki/spaces/QRest/pages/295061](https://pedrobenito.atlassian.net/wiki/spaces/QRest/pages/295061), Prototipo de Carta.

Del 10 de Marzo al 22 de Marzo: Corregir errores del prototipo, API y Tests.

Del 22 Marzo al 16 Abril: Cambiar idioma del código de Español a Inglés. 

Del 17 de Abril al 20 de Abril: Crear Confluence para reportes semanales, redefinir sprints.   [https://pedrobenito.atlassian.net/wiki/spaces/QRest/pages/295092](https://pedrobenito.atlassian.net/wiki/spaces/QRest/pages/295092) 

Del 23 de Abril al 30 de Abril: Analizar tecnologías a usar en el resto del sistema. [https://pedrobenito.atlassian.net/wiki/spaces/QRest/pages/295089](https://pedrobenito.atlassian.net/wiki/spaces/QRest/pages/295089) 

Del 1 de Mayo al 7 de Mayo: Añadir JS a la carta y análisis de competidor [https://pedrobenito.atlassian.net/wiki/spaces/QRest/pages/294938](https://pedrobenito.atlassian.net/wiki/spaces/QRest/pages/294938) 

Del 22 de Mayo al 28 de Mayo: Rediseñar carta como la de Qamarero.

Del 7 de Junio al 18 de Junio: Añadir subsecciones y prueba de LocalStorage.

Del 19 de Junio al 11 de Julio: Modelo de datos de pedido y prototipo.

Del 26 de Septiembre al 8 de Octubre: Actualización de Python 10 a Python 11 y CRUD de pedidos. Descargar archivos de Confluence. Hacer API de pedidos.

Del 8 de Octubre al 19 de Octubre: Aprender sobre Arquitectura web. Reestructurar la aplicación y empezar la aplicación prácticamente desde cero. 

Del 20 de Octubre a 25 de Octubre: Definir a fondo diagramas de flujo de la aplicación, casos de uso de alto del usuario y del backend. Trazabilidad de matriz de casos de uso. 

Del 26 de Octubre al 30 de Octubre: Implementar en capas menu, allergenos y pedidos. Definir casos de prueba e implementar tests para los pedidos.

Del 1 de Noviembre al 5 de Noviembre: Los repositorios ya no son un simple CRUD. Se implementa MongoStandardRepository. Se implementa OCC y luego transacciones. Se crean los repositorios de pedidos, menu y alergenos. Se crean Excepiones como una Fábrica.

Del 6 de Noviembre al 12 de Noviembre: Modifical los casos de uso de la carta y de los alérgenos. Se crean interfaces con ABC. Ahora todos los repositorios usan IStandardRepository (una interfaz que permite hacer un CRUD complejo) junto con MongoStandardRepository que es la clase que la implmenta con MongoDB. Se añaden manejadores de Excepciones a la aplicación de FastAPI. Se arreglan los tests de comandas. Se arregla a operación para actualizar el estado de los elementos de un pedido. Se pasan todos los tests de comandas. Frontend de carta y pedido funcionando. Se crea la capa services dentro de los casos de uso.

Del 13 de Noviembre al 20 de Noviembre: 
- Se crea un modelo de datos para el frontend con más información que los del dominio. 
- Se actualiza el JS para gestionar los elementos. 
- Se añaden los elementos del pedido a la carta.
- Se sincronizan los elementos del pedido en la carta con websocket.

Del 21 de Noviembre al 27 de Noviembre: 
- Peidos sincronizados.
- Mensajes de error en pedidos.

Del 28 de Noviembre al 6 de Diciemnre:
- Despliegue Heroku.
- Mensajes de error en carta.
- Redirección de rutas.
- Soporte de mensajes y errores como query.
- Gestión de errores en Websocket.
- Fianalizar frontend de la carta sincronizada.

Del 7 de Diciembre al _ de Diciembre:



