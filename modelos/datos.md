# Modelo de datos

## Syntaxis

```
entidad:
    atributo con tipo (tipo)
    atributo opcional
    atributo obligaroio*
    atributo derivado o inicializdo = valor
    []lista del atributo
```

El tipo se especificará cuando haya ambigüedad. 

## Carta

```
seccion:
    nombre*
    visible*
    []elementos:
        nombre*
        imagen
        descripcion
        precio
        responsable*
        visible* (boolean)
        []ingredientes:
            nombre*
        []alergenos:
            tipo*
            icono*
        []variantes:
            descripcion*
            precio
        []extras:
            descripcion*
            precio
        []etiquetas:
            nombre*
            icono
```

El precio será obligatorio si no hay variaciones con precios

El responsable indica la lista de gestión de comandas a la que llegará el pedido cuando se envíe la comanda. Por ejemplo a "cocina" o "camareros".

Las bebidas no tienen por qué tener definidos ingredientes.

Las etiquetas pueden tener diversos usos, como marcar un elemento como "vegano/vegetariano", "recomendado", "nuevo", "lo más pedido", etc.

La visibilidad podrá ser usada para desactivar secciones y elementos, ya sea por que no queden existencias o para editar como administrador sin que este se muestre.   

## Pedido

pedido:
    mesa
    fecha* = now()
    estado* = creado // creado -> pidiendo -> cerrado -> pagado
    total = sum(comandas.elementos.precios)
    factura = total + IVA 
    []comandas:
        fecha*
        []elementos:
            seccion*
            nombre*
            precio*
            variante
            []ingredientes:
                nombre
            []extras:
                descripción
            nota





