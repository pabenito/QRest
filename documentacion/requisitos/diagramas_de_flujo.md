# Diagramas de flujo

En este documento se recogen los diagramas de flujo de los casos de uso de la web.

Diferenciamos entre casos de uso del frontend y backend.

- **Casos de uso del frontend**: Los que el usuario realiza haciendo uso de la vista de la aplicación. 
- **Casos de uso del backend**: Los casos de uso que se ejecutan en el backend de la aplicación. Son las acciones atómicas que se pueden realizar en la aplicación.

## Casos de uso del fronted

```mermaid
flowchart LR
    hacer_pedido[Hacer pedido]
    pedir_cuenta[Pedir cuenta]
    ver_recibo[Ver recibo]
    pagar[Pagar]
    hacer_pedido --> hacer_pedido & pedir_cuenta
    pedir_cuenta --> ver_recibo
    ver_recibo --> ver_recibo & pagar
```

## Transiciones web

Transiciones entre las distintas páginas de la web y los casos de uso del backend que activan.

### Sintaxis

Definimos la sintaxis de los diagramas de flujo.

#### Tipos de pantalla

Usamos la forma para indicar el tipo de pantalla que es:

```mermaid
flowchart TD
    pantalla[Pantalla]
    decision{{Modal de decisión}}
    mensaje[/Modal con mensaje/]
```

#### Transiciones y casos de uso

Usamos los mensajes para diferenciar entre la opción en el frontend y el caso de uso que ejecuta:

```mermaid
flowchart LR
    a --Caso de uso de bajo nivel--> b
    a --_Opcion en pantalla_--> b
    a --_Opción en pantalla_: Caso de uso del backend--> b
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
        elemento_complejo{{Elemento Complejo}}
        confirmacion_cuenta{{Confirmación Cuenta}}
    end
    carta --Añadir/Eliminar elemento--> carta
    carta --_Añadir_--> elemento_complejo
    elemento_complejo --Añadir/Eliminar elemento--> carta
    elemento_complejo --_Cancelar_--> carta
    carta --Get pedido--> pedido
    pedido --_Volver a la carta_: Get carta & Get pedido--> carta
    pedido --Confirmar pedido & Get carta--> carta
    carta --_Pedir cuenta_--> confirmacion_cuenta
    confirmacion_cuenta --_Sí_: Generar recibo & Get recibo total--> pago
    confirmacion_cuenta --_No_--> carta
```

### Pedido

```mermaid
flowchart TD
    carta[Carta]
    subgraph g_pedido[Pedido]
        confirmar_pedido{{Confirmar Pedido}}
        pedido[Pedido]
        pedido_confirmado[/Pedido Confirmado/]
    end
    carta --Get pedido--> pedido
    pedido --Añadir/Eliminar elemento--> pedido
    pedido --_Volver a la carta_: Get carta & Get pedido--> carta
    pedido --_Confirmar pedido_--> confirmar_pedido
    confirmar_pedido --_No_--> pedido
    confirmar_pedido --_Sí_: Confirmar pedido--> pedido_confirmado
    pedido_confirmado --_Aceptar_: Get carta--> carta
```

### Recibo & Pago

```mermaid
flowchart TD
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
    pago --_Aceptar_: Tramitar pago & Confirmar pago--> pagado
    pagado --_Ok_: Get recibo total--> recibo_total
```

## Trazabilidad de casos de uso

### General

```mermaid
flowchart LR
    subgraph g_carta[Carta]
        carta[Carta]
        elemento_complejo[Elemento Complejo]
        confirmacion_cuenta[Confirmación Cuenta]
    end
    subgraph g_pedido[Pedido]
        pedido[Pedido]
        pedido_confirmado[Pedido Confirmado]
        confirmar[Confirmar Pedido]
    end
    subgraph g_pago[Pago]
        recibo_total[Recibo Total]
        pago[Pago]
        recibo_individual[Recibo Individual]
        pagado[Pagado]
    end
    subgraph casos_de_uso_carta[Casos de uso Carta]
        get_carta[Get carta]
        anadir_eliminar_elemento[Añadir/Eliminar elemento]
    end
    subgraph casos_de_uso_pedido[Casos de uso Pedido]
        get_pedido[Get pedido]
        confirmar_pedido[Confirmar pedido]
    end
    subgraph casos_de_uso_recibo[Casos de uso Recibo]
        get_recibo_individual[Get recibo individual]
        get_recibo_total[Get recibo total]
        generar_recibo[Generar recibo]
    end
    subgraph casos_de_uso_pago[Casos de uso Pago]
        tramitar_pago[Tramitar pago]
        confirmar_pago[Confirmar pago]
    end
    carta --> anadir_eliminar_elemento
    elemento_complejo --> anadir_eliminar_elemento
    carta --> get_pedido
    confirmacion_cuenta --> generar_recibo & get_recibo_total
    pedido --> anadir_eliminar_elemento
    pedido --> get_carta
    confirmar --> confirmar_pedido
    pedido_confirmado --> get_carta
    recibo_total --> get_recibo_individual
    recibo_individual --> get_recibo_total
    pago --> tramitar_pago
    pago --> confirmar_pago
    pago --> get_recibo_total
    pagado --> get_recibo_total
```

### Carta

```mermaid
flowchart LR
    subgraph g_carta[Carta]
        carta[Carta]
        elemento_complejo[Elemento Complejo]
        confirmacion_cuenta[Confirmación Cuenta]
    end
    subgraph casos_de_uso_carta[Casos de uso Carta]
        anadir_eliminar_elemento[Añadir/Eliminar elemento]
    end
    subgraph casos_de_uso_pedido[Casos de uso Pedido]
        get_pedido[Get pedido]
    end
    subgraph casos_de_uso_recibo[Casos de uso Recibo]
        get_recibo_total[Get recibo total]
        generar_recibo[Generar recibo]
    end
    carta --> anadir_eliminar_elemento
    elemento_complejo --> anadir_eliminar_elemento
    carta --> get_pedido
    confirmacion_cuenta --> generar_recibo & get_recibo_total
```

### Pedido

```mermaid
flowchart LR
    subgraph g_pedido[Pedido]
        pedido[Pedido]
        pedido_confirmado[Pedido Confirmado]
        confirmar[Confirmar Pedido]
    end
    subgraph casos_de_uso_carta[Casos de uso Carta]
        get_carta[Get carta]
        anadir_eliminar_elemento[Añadir/Eliminar elemento]
    end
    subgraph casos_de_uso_pedido[Casos de uso Pedido]
        confirmar_pedido[Confirmar pedido]
    end
    pedido --> anadir_eliminar_elemento
    pedido --> get_carta
    confirmar --> confirmar_pedido
    pedido_confirmado --> get_carta
```

### Pago

```mermaid
flowchart LR
    subgraph g_pago[Pago]
        recibo_total[Recibo Total]
        pago[Pago]
        recibo_individual[Recibo Individual]
        pagado[Pagado]
    end
    subgraph casos_de_uso_recibo[Casos de uso Recibo]
        get_recibo_total[Get recibo total]
        get_recibo_individual[Get recibo individual]

    end
    subgraph casos_de_uso_pago[Casos de uso Pago]
        tramitar_pago[Tramitar pago]
        confirmar_pago[Confirmar pago]
    end
    recibo_total --> get_recibo_individual
    recibo_individual --> get_recibo_total
    pagado --> get_recibo_total
    pago --> tramitar_pago
    pago --> confirmar_pago
    pago --> get_recibo_total
```

## Trazabilidad de casos de uso y repositorios

### General

```mermaid
flowchart LR
    subgraph casos_de_uso_carta[Casos de uso Carta]
        get_carta[Get carta]
        anadir_eliminar_elemento[Añadir/Eliminar elemento]
    end
    subgraph casos_de_uso_recibo[Casos de uso Recibo]
        get_recibo_individual[Get recibo individual]
        get_recibo_total[Get recibo total]
        generar_recibo[Generar recibo]
    end
    subgraph casos_de_uso_pedido[Casos de uso Pedido]
        get_pedido[Get pedido]
        confirmar_pedido[Confirmar pedido]
    end
    subgraph casos_de_uso_pago[Casos de uso Pago]
        confirmar_pago[Confirmar pago]
    end
    subgraph repositorio_carta[Repositorio Carta]
        _get_carta[Get Carta]
    end
    subgraph repositorio_pedido[Repositorio Pedido]
        _get_pedido[Get pedido]
        get_comandas[Get comandas]
        get_recibo[Get recibo]
        anadir_comanda[Añadir comanda]
        crear_recibo[Crear recibo]
        eliminar_pedido[Eliminar pedido]
    end
    subgraph repositorio_elemento_pedido[Repositorio Elemento Pedido]
        _get_pedido[Get pedido]
        anadir_elemento_pedido[Añadir nuevo elemento al pedido]
        actualizar_elemento_pedido[Actualizar elemento del pedido]
        eliminar_elemento_pedido[Eliminar elemento del pedido]
    end
    get_carta --> _get_carta
    anadir_eliminar_elemento --> anadir_elemento_pedido & actualizar_elemento_pedido & eliminar_elemento_pedido
    get_pedido --> _get_pedido
    confirmar_pedido --> _get_pedido & eliminar_pedido & anadir_comanda
    get_recibo_total --> get_recibo
    get_recibo_individual --> get_recibo
    generar_recibo --> get_comandas & crear_recibo
    confirmar_pago --> get_recibo & crear_recibo
```

### Carta

```mermaid
flowchart LR
    subgraph casos_de_uso_carta[Casos de uso Carta]
        get_carta[Get carta]
        anadir_eliminar_elemento[Añadir/Eliminar elemento]
    end
    subgraph repositorio_carta[Repositorio Carta]
        _get_carta[Get Carta]
    end
    subgraph repositorio_elemento_pedido[Repositorio Elemento Pedido]
        anadir_elemento_pedido[Añadir nuevo elemento al pedido]
        actualizar_elemento_pedido[Actualizar elemento del pedido]
        eliminar_elemento_pedido[Eliminar elemento del pedido]
    end
    get_carta --> _get_carta
    anadir_eliminar_elemento --> anadir_elemento_pedido & actualizar_elemento_pedido & eliminar_elemento_pedido
```

### Pedido

```mermaid
flowchart LR
    subgraph casos_de_uso_pedido[Casos de uso Pedido]
        get_pedido[Get pedido]
        confirmar_pedido[Confirmar pedido]
    end
    subgraph repositorio_pedido[Repositorio Pedido]
        _get_pedido[Get pedido]
        anadir_comanda[Añadir comanda]
        eliminar_pedido[Eliminar pedido]
    end
    get_pedido --> _get_pedido
    confirmar_pedido --> _get_pedido & eliminar_pedido & anadir_comanda
```

### Recibo

```mermaid
flowchart LR
    subgraph casos_de_uso_recibo[Casos de uso Recibo]
        get_recibo_individual[Get recibo individual]
        get_recibo_total[Get recibo total]
        generar_recibo[Generar recibo]
    end
    subgraph repositorio_pedido[Repositorio Pedido]
        get_comandas[Get comandas]
        get_recibo[Get recibo]
        crear_recibo[Crear recibo]
    end
    get_recibo_total & get_recibo_individual --> get_recibo
    generar_recibo --> get_comandas & crear_recibo
```

### Pago

```mermaid
flowchart LR
    subgraph casos_de_uso_pago[Casos de uso Pago]
        confirmar_pago[Confirmar pago]
    end
    subgraph repositorio_pedido[Repositorio Pedido]
        get_recibo[Get recibo]
        crear_recibo[Crear recibo]
    end
    confirmar_pago --> get_recibo & crear_recibo
```