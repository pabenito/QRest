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

### Ejemplos

Bebidas

```
{
  "nombre": "Bebidas",
  "visible": true,
  "elementos": [
    {
      "nombre": "Agua",
      "imagen": "https://image.freepik.com/foto-gratis/agua-fria-botella-plastico-tapa-azul-colocada-pasarela-cemento_33789-101.jpg",
      "responsable": "camareros",
      "visible": true,
      "variantes": [
        {
          "nombre": "Tamaño",
          "variantes": [
            {
              "descripcion": "500mL",
              "precio": 1
            },
            {
              "descripcion": "1,5L",
              "precio": 2
            }
          ]
        }
      ]
    },
    {
      "nombre": "Limonada",
      "imagen": "https://www.pequerecetas.com/wp-content/uploads/2021/05/limonada-como-se-hace.jpg",
      "descripcion": "Limonada de la casa",
      "precio": 3,
      "responsable": "camareros",
      "visible": true,
      "ingredientes": [
        "Limón",
        "Azúzar"
      ],
      "extras": [
        {
          "descripcion": "Hiebabuena",
          "precio": 1
        }
      ]
    }
  ]
}
```

``` 
{
  "nombre": "Coca-cola",
  "precio": 2.5,
  "responsable": "camareros",
  "visible": true,
  "variantes": [
    {
      "nombre": "Tipo",
      "variantes": [
        {
          "descripcion": "normal"
        },
        {
          "descripcion": "Zero"
        },
        {
          "descripcion": "Zero Zero"
        }
      ]
    }
  ]
}
```

## Pedido

```
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
```

### Ejemplo

```
pedido:
  mesa: 1
  fecha: 23-3-16 15:06 200ms 
  estado: pidiendo 
  total: 5$  
  comadas:
    fecha: 23-3-16 15:14 600ms 
    elementos:
      - 1:
        seccion: Bebidas
        nombre: Agua fría 
        precio: 1$
        variante: pequeña 
        nota: Con hielo 
      - 2: 
        seccion: Bebidas
        nombre: Limonada  
        precio: 4$
        extras:
          - Hierbabuena
```






