# Casos de Uso

Este documento recoge los casos de uso que contempla QRest en sus distintos ámbitos, desde el punto de vista de los usuarios desde la vista de la aplicación. 

Diferenciamos en dos catergorías de casos de uso, de alto y bajo nivel:

- **Casos de uso de alto nivel**: Aquellos del alto nivel de abstracción que se compone de otros casos de uso de bajo nivel.
- **Casos de uso de bajo nivel**: Aquellas acciones concretas que puede hacer un usuario en la aplicación.

## Glosario

### Actores

- **Empleado**: Entendido como una persona que opera el restaurante.
- **Comensal**: Dicho de un cliente que está sentado en la mesa que. Comparte pedido con los comensales de la misma mesa.

### Pantallas

- **Entrada**: Métodos para acceder a la pantalla en cuestión. Puede ser otra pantalla u otro método.
- **Salida**: Pantallas a las que se puede acceder desde la pantalla en cuestión.
- **Ruta**: Punto de acceso en la API.

### Carta

**Elemento**: Cualquier bebida, entrante, plato, postre, etc. de la carta que puede añadirse al pedido.

**Elemento simple**: Aquel que no hay que elegir nada. Es decir, no tiene variantes, ni extras opcionales, ni se le pueden quitar ingradientes. Ejemplo: Nestea.

**Elemento complejo**: Aquel para el que hay que elegir algo. Tiene variantes o extras o se pueden eliminar ingredientes.

## Pantallas

```mermaid
flowchart LR
    carta[Carta]
    pedido[Pedido]
    recibo_total[Recibo Total]
    recibo_individual[Recibo Individual]
    pago[Pago]
    carta --> pedido
    pedido --> carta
    carta --> recibo_total
    recibo_total --> recibo_individual & pago
    recibo_individual --> recibo_total & pago
    pago --> recibo_total
```

### Carta

Es la **pantalla inicial**. Se ven los elementos de la carta del restaurante y pueden añadir o eliminar unidades de cualquier elemento de la carta. Todos los comensales de una misma mesa están asociados al mismo pedido y ven en tiempo real cualquer actualización (añadir o eliminar unidades de algún elemento) que haga cualquier otro comensal de la misma mesa.

- **Ruta**: mesa/{Identificador de la mesa}
- **Entrada**: QR, Pantalla Pedido.
- **Salidas**: Pantalla Pedido, Pantalla Recibo Total.

### Pedido

Se ven todos los elementos que han pedido los comensales de la mesa. Esto incluye el elemento concreto; con sus variantes, extras, e ingredientes eliminados, en caso de elementos complejos; y la cantidad.

- **Ruta**: mesa/{Identificador de la mesa}/pedido
- **Entrada**: Pantalla Carta.
- **Salidas**:
  - Carta.
  - Pedido Confirmado.

### Recibo Total

En esta pantalla se ve el recibo del pedido de toda la mesa en todas las comandas. Además del estdo de pago de cada elemento y quíen lo ha pedido.

- **Ruta**: mesa/{Identificador de la mesa}/recibo
- **Entrada**: Pantalla Carta.
- **Salidas**:
  - Recibo Individual.
  - Pago.

### Recibo Recibo Individual

En esta pantalla se ve el recibo del total del comensal en todas las comandas. Además del estdo de pago de cada elemento y quíen lo ha pedido.

- **Ruta**: mesa/{Identificador de la mesa}/recibo/{comensal}
- **Entrada**: Pantalla Recibo total.
- **Salidas**:
  - Recibo Total.
  - Pago.

### Pago

En esta pantalla se tramita el pago.

- **Ruta**: mesa/{Identificador de la mesa}/pago/{comensal}
- **Entrada**: Pantalla Recibo total.
- **Salida**: Recibo Total.


## Casos de uso

```mermaid
flowchart LR
  comensal[[Comensal]]
  subgraph casos_de_uso[Casos de uso]
    subgraph casos_de_uso_hacer_pedido[Hacer pedido]
      hacer_pedido([Hacer pedido])
      subgraph casos_de_uso_de_bajo_nivel_hacer_pedido[Casos de uso de bajo nivel]
        anadir_al_pedido([Añadir elemento al pedido])
        eliminar_del_pedido([Eliminar elemento del pedido])
        ver_pedido([Ver Pedido])
        ver_carta([Ver Carta])
        anadir_al_pedido_sin_modificarlo([Añadir elemento al pedido sin modificarlo])
        anadir_al_pedido_modificandolo([Añadir elemento al pedido modificándolo])
        confirmar_pedido([Confirmar pedido])
      end
    end
    subgraph casos_de_uso_pagar[Pagar]
      pagar([Pagar])
      subgraph casos_de_uso_de_bajo_nivel_pagar[Casos de uso de bajo nivel]
        pagar_total([Pagar total])
        pagar_individual([Pagar individual])
        tramitar_pago([Tramitar pago])
      end
    end
    pedir_cuenta([Pedir cuenta])
  end
  comensal --uses--> hacer_pedido & pedir_cuenta & pagar
  hacer_pedido -.includes.-> anadir_al_pedido & eliminar_del_pedido & ver_pedido & ver_carta & confirmar_pedido
  anadir_al_pedido_sin_modificarlo & anadir_al_pedido_modificandolo ==extends==> anadir_al_pedido
  pagar_total & pagar_individual ==extends==> pagar
  pagar_total & pagar_individual -.includes.-> tramitar_pago
```

### Alto nivel

Los casos de uso de alto nivel son:

```mermaid
flowchart LR
  comensal[[Comensal]]
  hacer_pedido([Hacer pedido])
  pagar([Pagar])
  pedir_cuenta([Pedir cuenta])
  comensal --uses--> hacer_pedido & pedir_cuenta & pagar
```

Que se representan en el siguiente diagrama de flujo:

```mermaid
flowchart LR
    hacer_pedido[Hacer pedido]
    pedir_cuenta[Pedir cuenta]
    pagar[Pagar]
    hacer_pedido --> hacer_pedido
    hacer_pedido --> pedir_cuenta
    pedir_cuenta --> pagar
```

#### Hacer pedido

```mermaid
flowchart LR
  comensal[[Comensal]]
  hacer_pedido([Hacer pedido])
  anadir_al_pedido([Añadir elemento al pedido])
  eliminar_del_pedido([Eliminar elemento del pedido])
  ver_pedido([Ver Pedido])
  ver_carta([Ver Carta])
  confirmar_pedido([Confirmar pedido])
  anadir_al_pedido_sin_modificarlo([Añadir elemento al pedido sin modificarlo])
  anadir_al_pedido_modificandolo([Añadir elemento al pedido modificándolo])
  comensal --uses--> hacer_pedido
  hacer_pedido --includes--> anadir_al_pedido & eliminar_del_pedido & ver_pedido & ver_carta & confirmar_pedido
  anadir_al_pedido_sin_modificarlo & anadir_al_pedido_modificandolo ==extends==> anadir_al_pedido
```

- **Precondición**: Pantalla Carta.
- **Postcondición de éxito**: 

**Escenario Principal**:

1. El comensal navega por la carta.
2. El comensal ejecuta _Añadir un elemento al pedido_ o _Eliminar un elemento del pedido_.
3. El comensal ejecuta _Ver pedido_.
4. El comensal ejecuta _Confirmar pedido_ de forma satisfactioria.

**Escenarios Alternativos**:

3a. El comensal vuelve a modificar el peiddo:

1. Vuelve al paso 2.

4a. El comensal vuelve a la carta:
  
1. El comensal selecciona _Volver a la carta_.
2. El sitema ejecuta _Ver Carta_.
3. Vuelve al paso 1.

4b. El comensal modifica el peido.

1. El comensal ejecuta _Añadir un elemento sin modificar_ o _Eliminar un elemento del pedido_.
2. Vuelve al paso 4.

#### Pagar

```mermaid
flowchart LR
  comensal[[Comensal]]
      pagar([Pagar])
        pagar_total([Pagar total])
        pagar_individual([Pagar individual])
        tramitar_pago([Tramitar pago])
  comensal --uses--> pagar
  pagar_total & pagar_individual ==extends==> pagar
  pagar_total & pagar_individual -.includes.-> tramitar_pago
```

### Casos de uso de bajo nivel

#### Ver Pedido

- **Precondición**: Pantalla Carta.
- **Postcondición**: Pantalla Pedido.

**Escenario principal**:

1. El comensal selecciona _Ver pedido_.
2. El sistema redirige a la pantalla _Pedido_.
3. El sistema hace una llamada a la _API_ para recoger los datos del _Pedido_.
4. El sistema genera el HTML de la pantalla _Pedido_.
5. El JS del HTML resalta los elementos que han sido pedidos por el comensal.
6. El sistema muestra al comensal la pantalla de _Pedidos_.  

#### Ver Carta

- **Precondición**: Ninguna.
- **Postcondición**: Pantalla Carta.

**Escenario principal**:

1. El sistema redirige a la pantalla _Carta_.
2. El sistema hace una llamada a la _API_ para recoger los datos de la _Carta_.
3. El sistema hace una llamada a la _API_ para recoger los datos del _Pedido_.
4. El sistema genera el HTML de la pantalla _Carta_.
5. El JS del HTML filtra segun alérgenos del comensal y resalta las sugerencias.
6. El sistema muestra al comensal la pantalla de _Carta_.  

#### Confirmar Pedido

- **Precondición**: Pantalla Pedido.
- **Postcondición de éxito**: Pantalla Carta.

**Escenario principal**:

1. El comensal selecciona _Confirmar pedido_.
2. El sistema muestra un modal para pedirle al usuario que confirme la decisión.
3. El comensal selecciona _Aceptar_.
4. El sistema llama a la _API_ para confirmar el pedido.
5. El sistema ejecuta _Ver Carta_.

**Escenario alternativo**:

3a. El comensal cancela la confirmación del pedido.

1. El comensal selecciona _Cancelar_.
2. El sistema cierra el modal. (Sigue en la pantalla _Pedido_).

#### Añadir elemento al pedido sin modificar

- **Precondición**: Pantalla Carta ó Pedido.
- **Postcondicines**: 
  - Se ha añadido una unidad del elemento al pedido.
  - Se ha incrementado una unidad de ese elemento en las vistas de los comensales.

**Escenario principal**:

1. El comensal selecciona '+' sobre el elemento a añadir.
2. El sistema llama a la API para añadir el elemento al pedido con la información del elemento y el identificador del cliente. 
3. El JS incrementa en 1 la cantidad de ese elemento.
4. El sistema retransmite al JS del resto de comensales la petición para que incrementen en 1 ese elemento.

#### Añadir elemento al pedido modificándolo

- **Precondición**: Pantalla Carta.
- **Postcondicines de éxito**: 
  - Se ha añadido `cantidad` unidades del elemento al pedido.
  - Se ha incrementado en `cantidad` unidades de ese elemento en las vistas de los comensales.

**Escenario principal**:

1. El comensal selecciona '+' sobre el elemento a añadir.
2. El sistema muestra un modal para seleccionar las variantes, extras e ingredientes.
3. El comensal selecciona las variantes que quiera (si las hay), selecciona los extras que quiera (si los hay) y deselecciona los ingredientes no deseados (si los hay).
4. El comensal introduce la cantidad.
5. El comensal selecciona _Aceptar_. 
6. El sistema llama a la API para añadir el elemento al pedido con la información del elemento, la cantidad y el identificador del cliente. 
7. El JS incrementa en `cantidad` la cantidad de ese elemento.
8. El sistema retransmite al JS del resto de comensales la petición para que incrementen en `cantidad` ese elemento.

**Escenario alternativo**:

[3-5]a. El comensal cierra el modal.

1. El comensal selecciona _Cancelar_.
2. El sistema cierra el modal. (Sigue en la pantalla Carta).

#### Eliminar elemento del pedido

- **Precondición**: Pantalla Carta ó Pedido.
- **Postcondicines**: 
  - Se ha eliminado una unidad del elemento del pedido.
  - Se ha decrementado en una unidad ese elemento en las vistas de los comensales.

**Escenario principal**:

1. El comensal selecciona '-' sobre el elemento a eliminar.
2. El sistema llama a la API para eliminar el elemento al pedido con la información del elemento y el identificador del cliente. 
3. El JS decrementa en 1 la cantidad de ese elemento.
4. El sistema retransmite al JS del resto de comensales la petición para que decrementen en 1 ese elemento.

