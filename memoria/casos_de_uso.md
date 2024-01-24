# Casos de uso

## Glosario

- **Cliente**: Es un cliente del restaurante que todavía no tiene asignado un pedido.
- **Empleado**: Entendido como una persona que opera el restaurante.
- **Comensal**: Dicho de un cliente que el cual tiene asignado un pedido que con los clientes de la misma mesa.
- **Comanda**: Conjunto de elementos que se piden en la misma ronda.
- **Comanda actual**: Conjunto de elmento que se han seleccionado para pedir pero que todavía no se han confirmado.
- **Comanda confirmada**: Conjundo elementos de una ronda que ya se confirmó y se mandó a cocina.
- **Pedido**: Estructura de datos que guarda el estado de Comandas, Recibos y Pagos de una mesa de comensales.
- **Elemento**: Cualquier bebida, entrante, plato, postre, etc. de la carta que puede añadirse al pedido.
- **Pedido Activo**: Pedido para el cual todavía no hay cuenta generada. Y por tanto se pueden seguir pidiendo comandas.

## Listado de casos de uso

- Crear pedido
- Modificar comanda
- Confirmar comanda
- Pedir cuenta
- Ver recibo total
- Ver recibo individual
- Ver por pagar total
- Ver por pagar individual
- Pagar

## Estados de la mesa

1. No hay ningún pedido activo creado en la mesa ahoramismo.
2. No hay ninguna comanda confirmada.
3. Hay almenos una comanda confirmada.
4. Se ha generado el recibo.
5. El pedido ha sido pagado.

## Caso de uso total

**Precondición**: No hay ningún pedido activo creado en la mesa ahoramismo.
**Postcondición**: Se ha pagado el pedido.

### Escenario principal

1. El cliente se sienta en la mesa.
2. El cliente crea un pedido. [Caso de uso Crear pedido]
3. Un comensal modifica la carta. [Caso de uso Modificar comanda]
4. Un comensal confirma la comanda. [Caso de uso Confirmar comanda]
5. Uno de los comensale pide la cuenta. [Caso de uso Pedir cuenta]
6. Los comensales pagan la cuenta. [Caso de uso Pagar]

### Escenario alternatios

4a. Un comensal modifica la carta.
    1. Vualve al paso 3. 
5a. Los comensales piden otra comanda.
    1. Vuelve al paso 3.

## Crear pedido

**Precondición**: No hay ningún pedido activo creado en la mesa ahoramismo.  
**Postcondiciones**:

- Se ha generado un pedido activo para esa mesa.
- Los comensales se encuentran viendo la carta.

### Escenario pricipal

1. El cliente se sienta en la mesa.
2. El cliente escanea el QR sobre la mesa.
3. El sistema genera un nuevo pedido activo.
4. El sistema muestra al cliente el QR del pedido.
5. El cliente comparte el QR del pedido con los comensales.
6. Los comensales acceden a la carta.

## Modificar Comanda

**Precondiciones**:

- El pedido está activo.
- Los comensales se encuentran en la carta.

**Postcondición**: Si la comanda no resulta nula se puede confirmar la comanda.

### Escenario principal
1. Un comensal navega por la carta.
2. El comensal selecciona la opción de añadir ó eliminar sobre uno de los elementos de la carta.
3. El sistema añade o elimina ese elemento al pedido.
4. El sistema actualiza el estado del pedido para todos los comensales.

### Escenario Altenativo

3a. El elemento no lo ha pedido el cliente anteriormente.
1. El elemento no ha sido pedido anteriormente por el cliente que solicita eliminarlo.
2. El sitema muestra un mensaje de error.
3. Vuelve al paso 1.

## Confirmar comanda

**Precondiciones**:

- El pedido está activo.
- La comanda actual no es nula.

**Poscondición**: Se ha ordenado una comanda.

### Escenario principal

1. Un comensal selecciona ver resumen de la comanda.
2. El sistema comprueba si hay elementos en la comanda actual.
3. El sistema muestra el resumen de la comanda.
4. El comensal selecciona confirmar comanda.
5. El sistema comprueba si hay elementos en la comanda actual.
6. El sistema marca la comanda actual como confirmada.
7. El sistema muestra un mensaje de éxito.
8. El sistema redirige a la carta.

### Escenario alternativo

[2 ó 5]a. No hay elementos en la comanda.
1. El sistema no encuentra elementos en la comanda actual.
2. El sitema muestra un mensaje de error.
3. El sistema muestra la carta.

4a. El comensal modifica la comanda.
1. El comensal añade o elimina elementos del pedido. [Caso de uso Modificar comanda]
2. Vuelve al paso 2.

## Pedir cuenta

**Precondiciones**:

- El pedido está activo.
- Hay al menos una comanda confirmada.

**Postcondición**:

- El pedido deja de estar activo. No se pueden pedir más comandas.
- Se ha generado el recibo.

### Escenario principal

1. Un comensal selecciona la opción de pedir cuenta.
2. El sistema comprueba que no se haya generado ya un recibo.
3. El sistema comprueba que haya al menos una comanda confirmada. 
4. El sistema comprueba que no haya una comanda por confirmar.
5. El sistema genera un recibo en base a todas las comandas confirmadas.
6. El sistema muestra el recibo.

### Escenarios alternativos

2a. Ya existe el recibo.
1. El sistema detecta que ya existe el recibo.
2. El sistema muestra el recibo.

3a. No hay comandas confirmadas.
1. El sistema no encuentra ninguna comanda confirmada.
2. El sistema muestra un mensaje de error.

4a. Hay elementos por confirmar.
1. El sistema detecta que hay elementos en la comanda por confirmar.
2. El sistema muestra un mensaje de error.

## Pagar

**Precondiciones**: Hay recibo generado.
**Postcondición**: Se ha padago al menos una parte.

### Escenario principal

1. El sistema muestra el recibo.
2. Un comensal selecciona pagar.
3. El sistema marca el recibo como pensiente de pago.
4. El sistema muestra un mensaje al comensal indicando que vaya a caja a pagar.
5. El sistema muestra al empleado del restaurante el recibo pendiente de pago.
6. El comensal paga en caja.
7. El empleado marca el recibo como pagado.
8. El sistema confirma el pago del recibo.
9. El sistema muestra un mensaje al comensal indicando que el pago se ha realizado con éxito.
10. El sistema muestra lo que queda pendiente por pagar.

### Escenario alternativo

2a. Ver recibo indiviudual.
1. El comensal selecciona la opción de ver recibo indiviudual.
2. Vuelve al paso 2.

