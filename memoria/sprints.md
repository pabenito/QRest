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

Del 7 de Diciembre al 14 de Diciembre:
- Arreglar función que compruba si un elemento está en el menu
- API para mostrar todos los pedidos existentes
- Arreglar CSS para que el mensaje apareza centrado en pantalla
- Cambiar WS a WSS
- Modelo Vista Controlador para pedir, consultar y persistir el nombre del cliente en LocalStorage

Del 15 de Diciembre al 20 de Diciembre:
- API / genera nuevo pedido y redirige a /{pedido}
- Backend de generar recibo
- Casos de prueba de generar recibo
- Tests de generar recibo
- Prototipo de generar recibo
- Frontend de generar recibo

Del 27 de Diciembre al 2 de Enero:
- Casos de uso de pago
- Casos de prueba de ver por pagar y pago
- Test de ver por pagar
- Bakend de ver por pagar
- Bakend de pago
- Por pagar y recibo deparados en por pagar individual y total
- Prototipo y frontend de por pagar

Del 3 de Enero al 9 de Enero:
- API /{pedido} redirecciona a /{pedido}/carta
- Arreglar problema con /carta
- Añadir funcionalidad para solicitar pagar en caja.
- Crear websocket para solicitar pagar en caja.
- Crear backend para solicitar pagar en caja.
- API /caja para ver lo que se está esperando a pagar en caja. (Parte del restaurante)
- Prototipo /caja
- Frontend /caja
- Modelo-Vista-Controlador para esperar a pagar en caja.
- Arreglar imágenes del Frontend
- Añadir Modelo-Vista-Controlador para añadir sugerencias para volve a pedir un producto anterior. 

## Trello

Sprint 1, 2 y 3:
- Modelo conceptual del sistema
- Planificar sprints
- Preparar entorno de desarrollo
- Prototipado
- Coger entidad (correo y dominio)
- Aprender pymongo a fondo
- Modelo de datos de Carta y Pedidos

Sprint 4:
- Establecer Jinja2
    1. Crear un HTML en la carpeta _static_.
    2. Crear con FastAPI un endpoint que lo devuelva. 
    3. Probar a añadirle un CSS o imágenes. 
    4. Probar a añadirle variables.
    5. Probar a añadirle código de Jinja2
- Carta con Jinja2:
    1. Devolver prototipo estático desde FastAPI
    2. Devolverlo con Jinja2.
    3. Recoger los datos de la base de datos. 
    4. Mostrar alguna variable.
    5. Integrar mostrar variable con código.
    6. Mostrar imágenes. 
    7. Mostrar todo.

Sprint 5: 
- Prototipo de carta V2 basada en Qamarero.
- Javascript para la carta. Separar en documentos en /static/js
- Extraer CSS a /static/css.

Sprint 6: 
- Añadir subsecciones al backend
- Hacer tests de subsecciones
- Independizar el la base de datos en un archivo aparta database.py
- Jinja2 de Carta v2.

Sprint 7:
- Prototipo de pedido.
- Modelo de datos de pedido
- Reestructuración de modelo de datos de pedidos
- Extraer modelos en carpeta independiente
- Buscar solución para cambiar de un código monolítico a en capas. Principios SOLID y Clean Architecture.
- Planear cómo resolver problema de volver a la carta desde la página del peido.
- Diseño de solución para sincronizar los pedidos: Se eliminan requests, guardar en cada elemento los clientes que lo han pedido y actualizar directamente en la comanda actual cada vez que se hace un +/- en un elemento.

## Hacer memoria para recordar todo lo que se ha hecho

Fase 1 - Inicio:
- Investigar competidores
- Pensar en soluciones a problemas existentes en de los competidores
- Elegir un nombre para el proyecto
- Coger entidad: correo electrónico y dominio

Fase 2 - Análisis y Planificación:
- Definir funcionaliades deseables de la aplicación.
- Diagrama conceptual simple del sistema basado en funcionaliades.
- Planificar los sprints basados en las funcionalidades.

Fase 3 - Prototipo Carta:
- Definir y crear el entorno de desarrollo
- Diseñar modelo de datos de la carta (soportando elementos simples y complejos).
- Diseñar prototipo de carta.
- Crear HTML del protitipo de carta.
- Añadir CSS con BulmaCSS.
- Añadir funciones JS en mismo documento HTML (pricipalmente basados en attributos HTML).

Fase 4 - Backend Carta:
- Implementar modelo de datos de la carta.
- Desarrollar API CRUD de secciones de la carta.
- Desarrollar API CRUD de elementos embebidos en las secciones de la carta.

Fase 5 - Frontend Carta:
- Separar CSS en archivos individuales en /static/css
- Separar JS en archivos individuales en /static/js
- Frontend de la carta con Jinja2.

Fase 6 - Carta V2:
- Analizar competidor llamado Qamarero.
- Decisión de cambiar el diseño actual al de Qamarero.
- Diseño un prototipo como el de Qamarero.
- Implemento nuevo JS.
- Nuevo Frontend de la carta V2 con Jinja2.

Fase 7 - Subsecciones
- Diseñar nuevo modelo de datos de carta para soportar subsecciones.
- Implementar backend de subsecciones.

Fase 8 - Tests de integración de la carta
- Diseñar casos de uso de la carta.
- Diseñar casos de pruaba de la carta.
- Desarrollar tests de integración de la carta.

Fase 9 - Diseño de pedido
- Diseñar modelo de datos de pedidos.
- Diseñar prototipo de pedidos.
- Implementar backend de pedidos.
- Frontend de pedidos con Jinja2.

Fase 10 - Rediseño Clean Architecture
- Buscar solución para cambiar arquitecturar monolítica a arquitectura en capas.
- Aprender sobre Clean Architecture.
- Diseñar la arquitectura en capas de la aplicación al estilo Clean Architecture.
- Definir diagramas de flujo de las vistas de la aplicación (con los casos de uso que se pueden ejecutar como transiciones).
- Definir diagrama en capas de qué casos de uso puede ejecutar cada vista de la aplicación.
- Definir diagrama de capas de qué llamadas a la capa de persistencia puede ejecutar cada caso de uso.
- Re-planificar el proyecto (centrarse solo en la parte de los clientes del restaurante).
- Eliminar la API CRUD monolítica para modificar las secciones de la carta.

Fase 11 - Interfaz de persistencia
- Diseñar una interfaz de persistencia con MongoDB.
- Implementar una capa de persistencia que simplifique la interacción con MongoDB.
- Analizar opciones para evitar colisiones en la base de datos.
- Implementar Optimistic Concurrency Control en la capa de persistencia.
- Implementar Transacciones con MongoDB.

Fase 11 - Pedidos:
- Rehacer el backend de pedidos en base al nuevo diseño (en capas).
- Rehacer el frontend de pedidos con FastAPI.
- Diseñar casos de prueba de pedidos.
- Implementar test de integración de pedidos.
- Diseñar protocolo de sincronización de pedidos.
- Diseñar modelo de datos de pedidos para soportar sincronización.
- Re-implementar modelo de datos de pedidos.
- Implementar el backend de Websockets de pedidos.
- Crear Websockets en el JS de Jinja2.
- Implementar Modelo-Vista-Controlador en JS para sincronización.

Fase 12 - Cliente LocalStorage:
- Prueba de uso de LocalStorage.
- Prototipo de vista de pedido para pedir cliente.
- Actualizar frontend de pedido para pedir cliente.
- Implementar Modelo-Vista-Controlador para guardar y consultar el cliente en LocalStorage.

Fase 13 - Recibos:
- Diseñar solición para poder consultar el recibo total o indiviudal.
- Diseñar casos de pureba de recibo.
- Implementar test de integración de recibo.
- Implementar backend de recibo.
- Diseñar prototipo de recibo.
- Implementar frontend de recibo.

Fase 14 - Por pagar:
- Diseñar solución para poder consultar por pagar tota o individual.
- Diseñar casos de prueba de por pagar.
- Implementar test de integración de por pagar.
- Implementar backend de por pagar.
- Diseñar prototipo de por pagar.
- Implementar frontend de por pagar.

Fase 15 - Proteger rutas:
- Diseñar casos de error en cada vista del sistema.
- Diseñar redirecciones en base al estado del pedido.
- Diseñar redirecciones de nueva API.
- Implementar errores y mensajes en cada vista del sistema (backend + frontend).
- Añadir comprobación del estado del pedido para redireccionar automáticamente si es necesario.
- Añadir nuevas rutas del la API para redireccionar automáticamente y facilitar la navegación.

Fase 16 - Pago:
- Diseñar solución para solicitar pagar en caja y esperar confirmación.
- Extender el modelo de datos de pedido para soportar pagos pendientes en caja.
- Diseñar prototipo de pago en caja.
- Implementar backend de pago.
- Implementar frontend de pago en caja.
- Implementar websocket con identificadores para sicronización de pago en caja.

Fase 17 - Sugerencias:
- Analizar qué tipo de sugerencias era más conveniente.
- Diseñar prototipo de sugerencias para volver a pedir elemento pedido anteriormente.
- Implementar Modelo-Vista-Controlador en JS para persistir y consultar LocalStorage.
- Implmentar en el frontend con Jinja2.




