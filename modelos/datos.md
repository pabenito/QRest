# Modelo de datos

## Syntaxis

```
atributo opcional
atributo obligaroio*
```

El tipo se especificará cuando haya ambigüedad. 

## Carta

```
{
  name*: str,
  visible: bool,
  elements: [
    {
      name*: str,
      image: url,
      description: str,
      price: float,
      manager*: str,
      visible: bool,
      ingredients: [str],
      allergens: [str],
      variants: [
        {
          name*: str,
          variants*: [
            {
              description*: str,
              image: str,
              price: float
            }
          ]
        }
      ],
      extras: [
        {
          description*: str,
          price: float
        }
      ],
      tags: [
        {
          name*: str,
          icon: str
        }
      ]
    }
  ]
}
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
  "name": "Bebidas",
  "visible": true,
  "elements": [
    {
      "name": "Agua",
      "image": "https://image.freepik.com/foto-gratis/agua-fria-botella-plastico-tapa-azul-colocada-pasarela-cemento_33789-101.jpg",
      "manager": "camareros",
      "visible": true,
      "variants": [
        {
          "name": "Tamaño",
          "variants": [
            {
              "description": "500mL",
              "price": 1
            },
            {
              "description": "1,5L",
              "price": 2
            }
          ]
        }
      ]
    },
    {
      "name": "Limonada",
      "image": "https://www.pequerecetas.com/wp-content/uploads/2021/05/limonada-como-se-hace.jpg",
      "description": "Limonada de la casa",
      "price": 3,
      "manager": "camareros",
      "visible": true,
      "ingredients": [
        "Limón",
        "Azúzar"
      ],
      "extras": [
        {
          "description": "Hiebabuena",
          "price": 1
        }
      ]
    }
  ]
}
```

``` 
{
  "name": "Coca-cola",
  "price": 2.5,
  "manager": "camareros",
  "visible": true,
  "variants": [
    {
      "name": "Tipo",
      "variants": [
        {
          "description": "normal"
        },
        {
          "description": "Zero"
        },
        {
          "description": "Zero Zero"
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






