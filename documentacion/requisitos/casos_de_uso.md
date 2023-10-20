# Casos de Uso

Este documento recoge los casos de uso que contempla QRest en sus distintos ámbitos.

## Glosario

## Sintaxis

- **(-> Pantalla _)**: Accede a la pantalla indicada.

### Actores

- **Cliente**: Entendido como cliente del restaurante que usa la app.
- **Empleado**: Entendido como una persona que opera el restaurante.
- **Comensal**: Dicho de un cliente que está sentado en la misma mesa que el cliente al que se refiere. Y que por tanto comparte pedido.

### Pantallas

- **Entrada**: Métodos para acceder a la pantalla en cuestión. Puede ser otra pantalla u otro método.
- **Salida**: Pantallas a las que se puede acceder desde la pantalla en cuestión.
- **Acciones**: Casos de uso que se pueden ejecutar desde la pantalla en cuestión.
- **Ruta**: Punto de acceso en la API.
- **Query**: Los atributos query necestarios en la URL.

## Pantallas

### Carta

Es la **pantalla inicial**. Se ven los elementos de la carta del restaurante y pueden añadir o eliminar unidades de cualquier elemento de la carta. Todos los clientes de una misma mesa están asociados al mismo pedido y ven en tiempo real cualquer actualización (añadir o eliminar unidades de algún elemento) que haga cualquier cliente de la misma mesa.

- **Ruta**: /{Identificador de la mesa}
- **Entrada**: QR.
- **Salida**: Pantalla Pedido.
- **Acciones**:
    - Añadir elemento simple.
    - Eliminar elemento simple.
    - Añadir elemento complejo.
    - Eliminar elemento complejo.
    - Ver pedido. (-> Pantalla Pedido)

### Pedido

Se ven todos los elementos que han pedido los comensales de la mesa. Esto incluye el elemento concreto; con sus variantes, extras, e ingredientes eliminados, en caso de elementos complejos; y la cantidad.

- **Ruta**: /{Identificador de la mesa}/pedido
- **Entrada**: Pantalla Carta.
- **Salidas**:
    - Carta.
    - Comanda Confirmada.

## Casos de uso

Actor principal: Cliente.

Páginas:

### 
