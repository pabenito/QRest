# Casos de Uso

Este documento recoge los casos de uso que contempla QRest en sus distintos ámbitos, desde el punto de vista de los usuarios desde la vista de la aplicación. 

Diferenciamos en dos catergorías de casos de uso, de alto y bajo nivel:

- **Casos de uso de alto nivel**: Aquellos del alto nivel de abstracción que se compone de otros casos de uso de bajo nivel.
- **Casos de uso de bajo nivel**: Aquellas acciones concretas que puede hacer un usuario en la aplicación.

## Glosario

## Sintaxis

- **(-> Pantalla _)**: Accede a la pantalla indicada.

### Actores

- **Empleado**: Entendido como una persona que opera el restaurante.
- **Comensal**: Dicho de un cliente que está sentado en la mesa que. Comparte pedido con los comensales de la misma mesa.

### Pantallas

- **Entrada**: Métodos para acceder a la pantalla en cuestión. Puede ser otra pantalla u otro método.
- **Salida**: Pantallas a las que se puede acceder desde la pantalla en cuestión.
- **Ruta**: Punto de acceso en la API.

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
        ver_pedido([Ver pedido])
        volver_a_la_carta([Volver a la carta])
        anadir_al_pedido_simple([Añadir elemento simple al pedido])
        anadir_al_pedido_complejo([Añadir elemento complejo al pedido])
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
    confirmar_pedido([Confirmar pedido])
    pedir_cuenta([Pedir cuenta])
  end
  comensal --use--> hacer_pedido & confirmar_pedido & pedir_cuenta & pagar
  hacer_pedido -.includes.-> anadir_al_pedido & eliminar_del_pedido & ver_pedido & volver_a_la_carta
  co
  anadir_al_pedido_simple & anadir_al_pedido_complejo ==extends==> anadir_al_pedido
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
  confirmar_pedido([Confirmar pedido])
  pedir_cuenta([Pedir cuenta])
  comensal --uses--> hacer_pedido & confirmar_pedido & pedir_cuenta & pagar
```

Que se representan en el siguiente diagrama de flujo:

```mermaid
flowchart LR
    hacer_pedido[Hacer pedido]
    confirmar_pedido[Confirmar pedido]
    pedir_cuenta[Pedir cuenta]
    pagar[Pagar]
    hacer_pedido --> confirmar_pedido
    confirmar_pedido --> hacer_pedido
    confirmar_pedido --> pedir_cuenta
    pedir_cuenta --> pagar
```

#### Hacer pedido

```mermaid
flowchart LR
  comensal[[Comensal]]
  hacer_pedido([Hacer pedido])
  anadir_al_pedido([Añadir elemento al pedido])
  eliminar_del_pedido([Eliminar elemento del pedido])
  ver_pedido([Ver pedido])
  volver_a_la_carta([Volver a la carta])
  anadir_al_pedido_simple([Añadir elemento simple al pedido])
  anadir_al_pedido_complejo([Añadir elemento complejo al pedido])
  comensal --use--> hacer_pedido
  hacer_pedido --includes--> anadir_al_pedido & eliminar_del_pedido & ver_pedido & volver_a_la_carta

  anadir_al_pedido_simple & anadir_al_pedido_complejo ==extends==> anadir_al_pedido
```

#### Pagar

```mermaid
flowchart LR
  comensal[[Comensal]]
      pagar([Pagar])
        pagar_total([Pagar total])
        pagar_individual([Pagar individual])
        tramitar_pago([Tramitar pago])
  comensal --use--> pagar
  pagar_total & pagar_individual ==extends==> pagar
  pagar_total & pagar_individual -.includes.-> tramitar_pago
```


### 
