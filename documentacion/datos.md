# Secciones

```json
{
  "name": "bebidas",
  "elements": [
    {
      "name": "agua",
      "manager": "camareros",
      "variants": [
        {
          "name": "tamaño",
          "variants": [
            { "price": { "$numberDouble": "1.2" }, "name": "500ml" },
            { "price": { "$numberDouble": "1.8" }, "name": "1l" }
          ]
        },
        {
          "name": "temperatura",
          "variants": [{ "name": "fría" }, { "name": "del tiempo" }]
        }
      ]
    },
    {
      "name": "nestea",
      "manager": "camareros",
      "price": 2
    }
  ]
}
```

```json
{
  "name": "pizzas",
  "elements": [
    {
      "name": "carbonara",
      "manager": "cocina",
      "ingredients": ["tomate", "mozzarella", "champiñones", "bacon"],
      "allergens": ["gluten", "lacteos"],
      "variants": [
        {
          "name": "tamaño",
          "variants": [
            { "price": 8.5, "name": "individual" },
            { "price": 14, "name": "familiar" }
          ]
        }
      ],
      "extras": [
        { "price": 1.5, "name": "albahaca" }
      ]
    }
  ]
}
```

```json
{
  "_id": { "$oid": "658c1acc1d757f02422320fb" },
  "name": "pizzas",
  "elements": [
    {
      "name": "pizza margarita",
      "image": "https://bulma.io/images/placeholders/128x128.png",
      "description": "pizza clásica con tomate, mozzarella y albahaca fresca.",
      "price": { "$numberDouble": "8.5" },
      "manager": "cocina",
      "ingredients": [
        "tomate",
        "mozzarella",
        "albahaca",
        "masa de pizza"
      ],
      "allergens": ["gluten", "lacteos"],
      "variants": [
        {
          "name": "tamaño",
          "variants": [
            {
              "price": { "$numberDouble": "8.5" },
              "name": "individual"
            },
            {
              "price": {
                "$numberDouble": "14.5"
              },
              "name": "familiar"
            }
          ]
        }
      ],
      "extras": [
        {
          "price": { "$numberDouble": "1.5" },
          "name": "champiñones"
        },
        {
          "price": { "$numberInt": "1" },
          "name": "aceitunas negras"
        }
      ],
      "tags": [
        {
          "name": "vegetariano",
          "icon": "https://res.cloudinary.com/dteqcnpp3/image/upload/v1682613571/tags/vegetarian_f5xmq9.png"
        }
      ]
    },
    {
      "name": "Pizza 4 Quesos",
      "image": "https://bulma.io/images/placeholders/128x128.png",
      "description": "Pizza con mozzarella, gorgonzola, parmesano y queso de cabra.",
      "price": { "$numberInt": "9" },
      "manager": "cocina",
      "ingredients": [
        "mozzarella",
        "gorgonzola",
        "parmesano",
        "queso de cabra",
        "masa de pizza"
      ],
      "allergens": ["gluten", "lacteos"],
      "variants": [
        {
          "name": "tamaño",
          "variants": [
            {
              "price": { "$numberInt": "9" },
              "name": "individual"
            },
            {
              "price": {
                "$numberDouble": "15.5"
              },
              "name": "familiar"
            }
          ]
        }
      ],
      "extras": [
        {
          "price": { "$numberInt": "2" },
          "name": "jamón serrano"
        },
        {
          "price": { "$numberInt": "1" },
          "name": "rucula"
        }
      ],
      "tags": [
        {
          "name": "vegetariano",
          "icon": "https://res.cloudinary.com/dteqcnpp3/image/upload/v1682613571/tags/vegetarian_f5xmq9.png"
        }
      ]
    }
  ]
}
```
