# Modelos de datos

# Modelo de datos

## Sintaxis

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
      "image": "<https://image.freepik.com/foto-gratis/agua-fria-botella-plastico-tapa-azul-colocada-pasarela-cemento_33789-101.jpg",>
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
      "image": "<https://www.pequerecetas.com/wp-content/uploads/2021/05/limonada-como-se-hace.jpg",>
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



Los pedidos se han diseñado para que funcionen de forma sincronizadas entre distintos usuarios de una misma mesa. 

1. Cuando de sientan personas a la mesa se crea el pedido `order`, con la fecha de inicio `created`.
2. Luego cada vez que alguien añade o elimina un elemento, se envía un `request` al servidor que se retransmite al resto de clientes en la mesa y se añade al pedido. El JS de cada cliente se encargará de modificar la vista en base a esa request.
3. Cuando se confirma la comanda todos los request se compututan y se genera una comanda `command`, moviendo todas las requests de `requests` a `commad.requests`, dejando `requests` vacío.
4. Cuando se selecciona pagar, se computan todas las comandas y se generan lor recibos `receipt`, se hace un recibo total `receipt.total` y un recibo individual por cada usuario de la mesa `receipt.individual`.

De forma que la API de pedidos cuenta con las siguientes llamadas. 

- POST order(zone, table)
- GET orders() 
- GET order(order*)
- POST request(Request: order*, client*, type*, section*, element*, price, variants, extras, ingredients)
- GET requests(order*) // Devuelve `requests`
- DELETE requests(order*) // Elimina `requests`
- POST command() // Computa una comanda con los `requests` 
- GET commands() 
- GET command() // La última comanda
- POST receipt() // Computa los recibos con las comandas `commands`
- GET total_receipt(order, zone, table) // `order` o `table` y `zone` si fuese necesaria. 
- GET individual_receipt(client*, order, zone, table) // `order` o `table` y `zone` si fuese necesaria. 

```
Request:
    id: str
    timestamp*: datetime
    client*: str
    order*: str
    type*: str
    section*: str
    element*: str
    price*: float
    manager*: str
    variants: []
        name*: str
        value*: str
    extras: []
    ingredients: []

Element:
    section*: str
    element*: str
    quantity*: int
    price*: float
    manager*: str
    variants: []
        name*: str
        value*: str
    extras: []
    ingredients: []

Receipt:
    total*: float
    elements: [Element]

Order:
    zone: str
    table: str
    created: datetime
    closed: datetime
    requests: [Request]
    commands: []
        timestamp*: datetime
        requests*: [Request]
        total: Receipt
        individual: []
            client*: str
            receipt: Receipt
    receipt:
        total*:
            paid: datetime
            receipt*: Receipt
        individual: []
            client*: str
            receipt*: Receipt
            paid: datetime
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

## Alérgenos

``` 
[
  {
    "name": "altramuces",
    "icon": "<https://res.cloudinary.com/dteqcnpp3/image/upload/v1682504399/allergens/altramuces_b4jvje.png",>
  },
  {
    "name": "apio",
    "icon": "<https://res.cloudinary.com/dteqcnpp3/image/upload/v1682504398/allergens/apio_pl5hsf.png",>
  },
  {
    "name": "cacahuetes",
    "icon": "<https://res.cloudinary.com/dteqcnpp3/image/upload/v1682504398/allergens/cacahuetes_wgnv6b.png",>
  },
  {
    "name": "crustaceos",
    "icon": "<https://res.cloudinary.com/dteqcnpp3/image/upload/v1682504398/allergens/crustaceos_jbhopr.png",>
  },
  {
    "name": "frutos de cascara",
    "icon": "<https://res.cloudinary.com/dteqcnpp3/image/upload/v1682504398/allergens/frutos_de_cascara_vxancr.png",>
  },
  {
    "name": "gluten",
    "icon": "<https://res.cloudinary.com/dteqcnpp3/image/upload/v1682504398/allergens/gluten_c6tk3b.png",>
  },
  {
    "name": "huevo",
    "icon": "<https://res.cloudinary.com/dteqcnpp3/image/upload/v1682504398/allergens/huevo_v41h5a.png",>
  },
  {
    "name": "lacteos",
    "icon": "<https://res.cloudinary.com/dteqcnpp3/image/upload/v1682504398/allergens/lacteos_wxgwnp.png",>
  },
  {
    "name": "moluscos",
    "icon": "<https://res.cloudinary.com/dteqcnpp3/image/upload/v1682504397/allergens/moluscos_e9wa3o.png",>
  },
  {
    "name": "mostaza",
    "icon": "<https://res.cloudinary.com/dteqcnpp3/image/upload/v1682504397/allergens/mostaza_ib5sik.png",>
  },
  {
    "name": "pescado",
    "icon": "<https://res.cloudinary.com/dteqcnpp3/image/upload/v1682504397/allergens/pescado_nwumbp.png",>
  },
  {
    "name": "sesamo",
    "icon": "<https://res.cloudinary.com/dteqcnpp3/image/upload/v1682504397/allergens/sesamo_xae3sh.png",>
  },
  {
    "name": "soja",
    "icon": "<https://res.cloudinary.com/dteqcnpp3/image/upload/v1682504397/allergens/soja_ictpzn.png",>
  },
  {
    "name": "sulfitos",
    "icon": "<https://res.cloudinary.com/dteqcnpp3/image/upload/v1682504397/allergens/sulfitos_yhraaz.png",>
  },
]
```
