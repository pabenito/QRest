# Diagramas de flujo

En este documento se recoge qué casos de uso se disparan en el backend las acciones en la web.

Los casos de uso de este documento son casos de uso del backend de la aplicación, siendo estas las acciones atómicas que se pueden realizar en la aplicación. En estos no se recogen las acciones del usuario en la vista de la aplicación. 

## Transiciones web

Transiciones entre las distintas páginas de la web y los casos de uso que activan.

### Sintaxis

#### Tipos de pantalla

```mermaid
flowchart TD
    pantalla[Pantalla]
    decision{{Modal de decisión}}
    mensaje[/Modal con mensaje/]
```

#### Transiciones y casos de uso

```mermaid
flowchart LR
    a --Caso de uso que activa--> b
    a --_Opcion en pantalla_--> b
    a --_Opción en pantalla_: Caso de uso que activa--> b
```

### Clientes

```mermaid
flowchart LR
    carta[Carta]
    pedido[Pedido]
    pago[Pago]
    carta --Get pedido--> pedido
    pedido --_VolGet a la carta_: Get carta--> carta
    pedido --Confirmar pedido & Get carta--> carta
    carta --Generar recibo & Get recibo total--> pago
```

### Carta

```mermaid
flowchart LR
    pedido[Pedido]
    pago[Pago]
    subgraph g_carta[Carta]
        carta[Carta]
        elemento_complejo[Elemento Complejo]
        confirmacion_cuenta{{Confirmación Cuenta}}
    end
    carta --Añadir elemento simple--> carta
    carta --Eliminar elemento simple--> carta
    carta --Eliminar elemento complejo--> carta
    carta --_Añadir_--> elemento_complejo
    elemento_complejo --Añadir elemento complejo--> carta
    elemento_complejo --_Cancelar_--> carta
    carta --Get pedido--> pedido
    pedido --_VolGet a la carta_: Get carta--> carta
    pedido --Confirmar pedido & Get carta--> carta
    carta --_Pedir cuenta_--> confirmacion_cuenta
    confirmacion_cuenta --_Sí_: Generar recibo & Get recibo total--> pago
    confirmacion_cuenta --_No_--> carta
```

### Pedido

```mermaid
flowchart LR
    carta[Carta]
    subgraph g_pedido[Pedido]
        confirmar_pedido{{Confirmar Pedido}}
        pedido[Pedido]
        pedido_confirmado[/Pedido Confirmado/]
    end
    carta --Get pedido--> pedido
    pedido --Añadir elemento simple--> pedido
    pedido --Eliminar elemento simple--> pedido
    pedido --Añadir elemento complejo--> pedido
    pedido --Eliminar elemento complejo--> pedido
    pedido --_VolGet a la carta_: Get carta--> carta
    pedido --_Confirmar pedido_--> confirmar_pedido
    confirmar_pedido --_No_--> pedido
    confirmar_pedido --_Sí_: Confirmar pedido--> pedido_confirmado
    pedido_confirmado --_Aceptar_: Get carta--> carta
```

### Pago

```mermaid
flowchart LR
    carta[Carta]
    subgraph g_pago[Pago]
        recibo_total[Recibo Total]
        recibo_individual[Recibo Individual]
        pago[Pago]
        pagado[Pagado]
    end
    carta --Generar recibo & Get recibo total--> recibo_total
    recibo_total --Get recibo individual--> recibo_individual
    recibo_total --_Pagar_--> pago
    recibo_individual --Get recibo total--> recibo_total
    recibo_individual --_Pagar--> pago
    pago --_Cancelar_: Get recibo total--> recibo_total
    pago --_Aceptar_: Tramitar pago--> pagado
    pagado --_Ok_: Get recibo total--> recibo_total
```

## Trazabilidad de casos de uso

### Carta

```mermaid
flowchart LR
    subgraph g_carta[Carta]
        carta[Carta]
        elemento_complejo[Elemento Complejo]
        confirmacion_cuenta[Confirmación Cuenta]
    end
    subgraph casos_de_uso[Casos de uso]
        anadir_elemento_simple[Añadir elemento simple]
        eliminar_elemento_simple[Eliminar elemento simple]
        anadir_elemento_complejo[Añadir elemento Complejo]
        eliminar_elemento_complejo[Eliminar elemento Complejo]
        get_pedido[Get pedido]
        get_recibo_total[Get recibo total]
        generar_recibo[Generar recibo]
    end
    carta --> anadir_elemento_simple
    carta --> eliminar_elemento_simple
    carta --> eliminar_elemento_complejo
    elemento_complejo --> anadir_elemento_complejo
    carta --> get_pedido
    confirmacion_cuenta --> generar_recibo & get_recibo_total
```

### Pedido

```mermaid
flowchart LR
    subgraph g_pedido[Pedido]
        pedido[Pedido]
        confirmar[Confirmar Pedido]
        pedido_confirmado[Pedido Confirmado]
    end
    subgraph casos_de_uso[Casos de uso]
        anadir_elemento_simple[Añadir elemento simple]
        eliminar_elemento_simple[Eliminar elemento simple]
        anadir_elemento_complejo[Añadir elemento Complejo]
        eliminar_elemento_complejo[Eliminar elemento Complejo]
        confirmar_pedido[Confirmar pedido]
        get_carta[Get carta]
    end
    pedido --> anadir_elemento_simple
    pedido --> eliminar_elemento_simple
    pedido --> anadir_elemento_complejo
    pedido --> eliminar_elemento_complejo
    pedido --> get_carta
    confirmar --> confirmar_pedido
    pedido_confirmado --> get_carta
```

### Pago

```mermaid
flowchart LR
    subgraph g_pago[Pago]
        recibo_total[Recibo Total]
        recibo_individual[Recibo Individual]
        pago[Pago]
        pagado[Pagado]
    end
    subgraph casos_de_uso[Casos de uso]
        get_recibo_individual[Get recibo individual]
        get_recibo_total[Get recibo total]
        tramitar_pago[Tramitar pago]
    end
    recibo_total --> get_recibo_individual
    recibo_individual --> get_recibo_total
    pago --> tramitar_pago
    pago --> get_recibo_total
    pagado --> get_recibo_total
```