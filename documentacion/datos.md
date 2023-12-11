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
