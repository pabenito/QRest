# Diagramas de flujo

## Web

### Clientes

```mermaid
flowchart LR
        carta[Carta]
        pedido[Pedido]
        pago[Pago]
    carta --Ver pedido--> pedido
    pedido --_Volver a la carta_: Ver carta--> carta
    pedido --Confirmar pedido & Ver carta--> carta
    carta --Generar recibo & Ver recibo total--> pago
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
    carta --Ver pedido--> pedido
    pedido --_Volver a la carta_: Ver carta--> carta
    pedido --Confirmar pedido & Ver carta--> carta
    carta --_Pedir cuenta_--> confirmacion_cuenta
    confirmacion_cuenta --_Sí_: Generar recibo & Ver recibo total--> pago
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
    carta --Ver pedido--> pedido
    pedido --Añadir elemento simple--> pedido
    pedido --Eliminar elemento simple--> pedido
    pedido --Añadir elemento complejo--> pedido
    pedido --Eliminar elemento complejo--> pedido
    pedido --_Volver a la carta_: Ver carta--> carta
    pedido --_Confirmar pedido_--> confirmar_pedido
    confirmar_pedido --_No_--> pedido
    confirmar_pedido --_Sí_: Confirmar pedido--> pedido_confirmado
    pedido_confirmado --_Aceptar_: Ver carta--> carta
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
    carta --Generar recibo & Ver recibo total--> recibo_total
    recibo_total --Ver recibo individual--> recibo_individual
    recibo_total --_Pagar_--> pago
    recibo_individual --Ver recibo total--> recibo_total
    recibo_individual --_Pagar--> pago
    pago --_Cancelar_: Ver recibo total--> recibo_total
    pago --_Aceptar_: Tramitar pago--> pagado
    pagado --_Ok_: Ver recibo total--> recibo_total
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
        ver_pedido[Ver pedido]
        ver_recibo_total[Ver recibo total]
        generar_recibo[Generar recibo]
    end
    carta --> anadir_elemento_simple
    carta --> eliminar_elemento_simple
    carta --> eliminar_elemento_complejo
    elemento_complejo --> anadir_elemento_complejo
    carta --> ver_pedido
    confirmacion_cuenta --> generar_recibo & ver_recibo_total
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
        ver_carta[Ver carta]
    end
    pedido --> anadir_elemento_simple
    pedido --> eliminar_elemento_simple
    pedido --> anadir_elemento_complejo
    pedido --> eliminar_elemento_complejo
    pedido --> ver_carta
    confirmar --> confirmar_pedido
    pedido_confirmado --> ver_carta
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
        ver_recibo_individual[Ver recibo individual]
        ver_recibo_total[Ver recibo total]
        tramitar_pago[Tramitar pago]
    end
    recibo_total --> ver_recibo_individual
    recibo_individual --> ver_recibo_total
    pago --> tramitar_pago
    pago --> ver_recibo_total
    pagado --> ver_recibo_total
```

### Ver

En la práctica cada caso de uso ver lo que hace es llamar a un caso de uso de tipo GET que se usa para generar el HTML de la nueva pantalla y transitar a ella. 

```mermaid
flowchart TB
    subgraph casos_de_uso[Ver]
        ver_carta[Ver carta]
        ver_pedido[Ver pedido]
        ver_recibo_total[Ver recibo total]
        ver_recibo_individual[Ver recibo individual]
    end
    subgraph casos_de_uso[Casos de uso]
        get_carta[Get pedido]
        get_pedido[Get pedido]
        get_recibo_total[Get recibo total]
        get_recibo_individual[Get recibo individual]
    end
    ver_carta --> get_carta
    ver_pedido --> get_pedido
    ver_recibo_total --> get_recibo_total
    ver_recibo_individual --> get_recibo_individual
```