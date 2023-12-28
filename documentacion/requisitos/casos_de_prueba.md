# Casos de prueba del Backend

## Pedido

### Estructura de datos

```
class Variant(BaseModel):
    name: str
    value: str


class Element(BaseModel):
    section: str
    element: str
    quantity: int
    clients: list[str]
    variants: Optional[list[Variant]] = None
    extras: Optional[list[str]] = None
    ingredients: Optional[list[str]] = None


class ReceiptElement(Element):
    price: float


class Command(BaseModel):
    timestamp: datetime
    elements: list[Element]

class Order(BaseModel):
    id: str
    current_command: Optional[list[Element]] = None
    commands: Optional[list[Command]] = None
    receipt: Optional[list[ReceiptElement]] = None
    to_be_paid: Optional[list[ReceiptElement]] = None
    paid: Optional[bool] = None
```

### Semantica

- **Elemento**: Cualquier bebida, entrante, plato, postre, etc. de la carta que puede añadirse al pedido.
- **Pedido** (`Order`): Se refiere a la estrucutra de datos asociada a una mesa del restaurante mientras hay comensales en ella, donde se almacena la comanda actual (sin confirmal), el total de comandas confirmadas y el recibo cuando se pide la cuenta. Nótese que cada vez que nuevos comensales se sientan el la misma mesa se crea una nueva estrucuta de datos (el pedido).
- **Comanda actual** (`current command`): Se refiere al conjundo de elementos que han pedido los comensales pero que todavía no han sido confirmados y por tanto no se ha enviado a cocina.
- **Comanda confirmada** (`commands`): Comanda que ha sido confirmada por los comensales y que se ha enviado a cocina. Se llama comanda confirmada independientemente de que se haya servido ya o no. 
- **Generar comanda**: Cuando se han añadido elemento de la comanda actual, de forma que no está vacía.
- **Confirmar comanda**: Cuando la comanda actual se añade al conjunto de comandas del pedido `commands`. Quedadndo la comanda actual vacía.
- **Pedido existe**: Se refiere a que hay algún pedido cuyo identificador coincida con el introducido.
- **Comanda actual existe**: Se refiere a que el atributo comanda actual existe en el pedido, aunqu sea una lista vacía.

### Caso 1: Obtener la comanda actual cuando existe el pedido y hay comanda actual

Este caso se intenta ver la comanda actual de un pedido existe previamente y para el cual hay una comanda actual. Devolvemos la comanda actual.

- **Método**: Ver comanda actual (`get_current_command`).
- **Escenario**: Pedido existe y comanda actual existe.
- **Tipo**: Éxito.

#### Caso de prueba

- **Dado que** se crea nuevo pedido con identificador _{id}_.
- **Y** se añade el elemento _{elemento}_ al la comanda actual del pedido con identificador _{id}_
- **Cuando** se solicita ver la comanda actual del pedido con identificador _{id}_.
- **Entonces** el sistema devuelve un HTTP Status 200 (OK)
- **Y** el sistema devuelve el elemento _{elemento}_.

#### Ejemplos

##### Un elemento simple

- _{id}_: "abc"
- _{element}_:

```json
{
    "section": "bebidas",
    "element": "nestea",
    "quantity": 1,
    "clients": ["marcos"]
}
```

Resultado: `[{element}]`

##### Un elemento complejo

- _{id}_: "abc"
- _{element}_:

```json
[
    {
        "section": "pizzas",
        "element": "carbonara",
        "quantity": 3,
        "variants": [
            {
                "name": "tamaño",
                "value": "familiar"
            }
        ],
        "extras": ["albahaca"],
        "ingredients": ["bacon"],
        "clients": ["paula", "marta", "paco"]
    }
]
```

Resultado: `[{element}]`

#### Test en Python
`test_get_current_command__when_current_command_exists__then_return_current_command()`

### Caso 2: Obtener la comanda actual cuando no existe el pedido

Este caso se intenta ver la comanda actual de un pedido que no existe. Devolvemos HTTP Status 404 (Not Found).

- **Método**: Ver comanda actual (`get_current_command`).
- **Escenario**: Pedido no existe.
- **Tipo**: Error.

#### Caso de prueba

- **Dado que** no existe ningun pedido cuyo identificado sea _{id}_.
- **Cuando** se solicita ver la comanda actual del pedido con identificador _{id}_.
- **Entonces** el sistema devuelve un HTTP Status 404 (Not Found).

#### Ejemplos

- _{id}_: "abc"

#### Test en Python
`test_get_current_command__when_order_does_not_exists__then_http_status_404_not_found()`

### Caso 3: Obtener la comanda actual cuando no hay comanda actual

Este caso se intenta ver la comanda actual de un pedido existe previamente, pero para el cual no existe la comanda actual. Devolvemos una lista vacía.

- **Método**: Ver comanda actual (`get_current_command`).
- **Escenario**: Comanda actual no existe.
- **Tipo**: Éxito.

#### Caso de prueba

- **Dado que** se crea nuevo pedido con identificador _{id}_
- **Y** no se ha añadido ningún elemento a la comanda actual.
- **Cuando** se solicita ver la comanda actual del pedido con identificador _{id}_.
- **Entonces** el sistema devuelve un HTTP Status 200 (OK)
- **Y** el sistema devuelve una lista vacía.

#### Ejemplos

- _{id}_: "abc"

Resultado: `[]`

#### Test en Python
`test_get_current_command__when_current_command_does_not_exists__then_return_empty_list()`

### Caso 4: Confirmar la comanda actual cuando existe el pedido y hay comanda actual

En este caso, la comanda actual de un pedido existente se confirma y se añade a la lista de comandas confirmadas del pedido. La comanda actual se vacía después de confirmarla.

- **Método**: Confirmar comanda actual (`confirm_current_command`).
- **Escenario**: Pedido y comanda actual existen.
- **Tipo**: Éxito.

#### Caso de prueba

- **Dado que** se crea un nuevo pedido con identificador _{id}_.
- **Y** se añade el elemento _{elemento}_ a la comanda actual del pedido con identificador _{id}_
- **Y** la fecha actual es _{timestamp}_.
- **Cuando** se solicita confirmar la comanda actual del pedido con identificador _{id}_.
- **Entonces** el sistema añade la comanda actual a la lista de comandas confirmadas confirmadas
- **Y** el sistema vacía la comanda actual
- **Y** el sistema devuelve un HTTP Status 200 (OK)
- **Y** el sistema devuelve la commanda que se ha añadido a la lista de comandas confirmadas.

#### Ejemplos

##### Un elemento simple

- _{timestamp}_: 2023-10-30 15:30:45.123456
- _{id}_: "abc"
- _{element}_:

```json
{
    "section": "bebidas",
    "element": "nestea",
    "quantity": 1,
    "clients": ["marcos"]
}
```

Resultado: 

```json
{
    "timestamp": "{timestamp}",
    "elements": ["{element}"]
}
```

##### Un elemento complejo

- _{timestamp}_: 2023-10-30 15:30:45.123456
- _{id}_: "abc"
- _{element}_:

```json
{
    "section": "pizzas",
    "element": "carbonara",
    "quantity": 3,
    "variants": [
        {
            "name": "tamaño",
            "value": "familiar"
        }
    ],
    "extras": ["albahaca"],
    "ingredients": ["bacon"],
    "clients": ["paula", "marta", "paco"]
}
```

Resultado: 

```json
{
    "timestamp": "{timestamp}",
    "elements": ["{element}"]
}
```

#### Test en Python
`test_confirm_current_command__when_command_exists__then_return_command()`

### Caso 5: Confirmar la comanda actual cuando no existe el pedido

Este caso trata de confirmar una comanda para un pedido que no existe. Devolvemos HTTP Status 404 (Not Found).

- **Método**: Confirmar comanda actual (`confirm_current_command`).
- **Escenario**: Pedido no existe.
- **Tipo**: Error.

#### Caso de prueba

- **Dado que** no existe ningún pedido con ese identificador.
- **Cuando** se solicita confirmar la comanda actual del pedido con identificador _{id}_.
- **Entonces** el sistema devuelve un HTTP Status 404 (Not Found).

#### Ejemplos

- _{id}_: "abc"

#### Test en Python
`test_confirm_current_command__when_order_does_not_exists__then_http_status_404_not_found()`

### Caso 6: Confirmar la comanda actual cuando la comanda actual no existe

Este caso trata de confirmar una comanda para un pedido que sí existe, pero no tiene una comanda actual. En este caso, se devuelve un HTTP Status 400 (Bad Request).

- **Método**: Confirmar comanda actual (`confirm_current_command`).
- **Escenario**: Comanda actual no existe.
- **Tipo**: Error.

#### Caso de prueba

- **Dado que** se crea un nuevo pedido con identificador _{id}_.
- **Y** no se ha añadido ningún elemento a la comanda actual.
- **Cuando** se solicita confirmar la comanda actual del pedido con identificador _{id}_.
- **Entonces** el sistema devuelve un HTTP Status 400 (Bad Request).

#### Ejemplos

- _{id}_: "abc"

#### Test en Python
`test_confirm_current_command__when_current_command_does_not_exists__then_http_status_400_bad_request()`

### Caso 7: Añadir un elemento cuando el elemento es correcto, es nuevo y su cantidad es mayor que cero

En este caso, se añade un elemento nuevo a la comanda actual de un pedido existente. El elemento es válido y su cantidad es mayor que cero.

- **Método**: Añadir elemento (`add_element`).
- **Escenario**: Elemento es correcto, es nuevo y su cantidad es mayor que cero.
- **Tipo**: Éxito.

#### Caso de prueba

- **Dado que** se crea un nuevo pedido con identificador _{id}_.
- **Y** el elemento _{elemento}_ es correcto
- **Y** la cantidad del elemento _{elemento}_ es mayor que cero.
- **Cuando** se solicita añadir _{elemento}_ al pedido con identificador _{id}_.
- **Entonces** el sistema añade el elemento a la comanda actual.
- **Y** el sistema devuelve un HTTP Status 200 (OK).
- **Y** el sistema devuelve el nuevo elemento añadido.

#### Ejemplos

##### Un elemento simple

- _{id}_: "abc"
- _{element}_:

```json
{
    "section": "bebidas",
    "element": "nestea",
    "quantity": 1,
    "clients": ["marcos"]
}
```

Resultado: `{element}`

##### Un elemento complejo

- _{id}_: "abc"
- _{element}_:

```json
[
    {
        "section": "pizzas",
        "element": "carbonara",
        "quantity": 3,
        "variants": [
            {
                "name": "tamaño",
                "value": "familiar"
            }
        ],
        "extras": ["albahaca"],
        "ingredients": ["bacon"],
        "clients": ["paula", "marta", "paco"]
    }
]
```

Resultado: `{element}`

#### Test en Python
`test_add_element__when_element_is_correct_and_element_is_new_and_element_quantity_is_grater_than_zero__then_added_to_the_order_and_return_new_element()`

### Caso 8: Añadir un elemento cuando el elemento es correcto, ya existe en la comanda y la suma de las cantidades es mayor que cero

Este caso es para añadir un elemento que ya existe en la comanda actual. En este caso, se sumará la cantidad al elemento existente.

- **Método**: Añadir elemento (`add_element`).
- **Escenario**: Elemento es correcto, ya existe y la suma de las cantidades es mayor que cero.
- **Tipo**: Éxito.

#### Caso de prueba

- **Dado que** se crea un nuevo pedido con identificador _{id}_
- **Y** el elemento _{elemento nuevo}_ es correcto
- **Y** existe un elemento _{elmento actual}_ en la comanda actual
- **Y** el elemento _{elmento actual}_ es el mismo que el elemento _{elemento nuevo}_
- **Y** la cantidad del elemento _{elemento actual}_ es _{cantidad elemento actual}_ 
- **Y** la cantidad del elemento _{elemento nuevo}_ es _{cantidad elemento nuevo}_
- **Y** la suma _{cantidad elemento actual}_ y _{cantidad elemento nuevo}_ es mayor que 0
- **Y** la lista de clientes de _{elmento actual}_ es _{lista de clientes elemento actual}_
- **Y** la lista de clientes de _{elmento nuevo}_ es _{lista de clientes elemento nuevo}_
- **Cuando** se solicita añadir _{elemento nuevo}_ al pedido con identificador _{id}_.
- **Entonces** el sistema actualiza la cantidad _{cantidad elemento actual}_ sumándole la cantidad _{cantidad elemento actual}_
- **Y** el sistema actualiza la lista de clientes _{lista de clientes elemento actual}_ añadiendo los elementos de la lista de clientes _{lista de clientes elemento nuevo}_
- **Y** el sistema devuelve un HTTP Status 200 (OK)
- **Y** el sistema devuelve el elemento {elemento actual} actualizado.

#### Ejemplos

##### Un elemento simple

- _{id}_: "abc"
- _{cantidad elemento actual}_: 1
- _{cantidad elemento nuevo}_: 2
- _{lista de clientes actual}_: `["marcos"]`
- _{lista de clientes nuevo}_: `["lola", "antonio"]`
- _{elemento actual}_:

```json
{
    "section": "bebidas",
    "element": "nestea",
    "quantity": "{cantidad elemento actual}",
    "clients": "{lista de clientes actual}"
}
```
- _{elemento nuevo}_:
```json
{
    "section": "bebidas",
    "element": "nestea",
    "quantity": "{cantidad elemento nuevo}",
    "clients": "{lista de clientes nuevo}"
}
```

Resultado: 
```json
{
    "section": "bebidas",
    "element": "nestea",
    "quantity": "{cantidad elemento actual} + {cantidad elemento nuevo}",
    "clients": "{lista de clientes actual} union {lista de clientes nuevo}"
}
```

##### Un elemento complejo

- _{id}_: "abc"
- _{element}_:

```json
[
    {
        "section": "pizzas",
        "element": "carbonara",
        "quantity": 3,
        "variants": [
            {
                "name": "tamaño",
                "value": "familiar"
            }
        ],
        "extras": ["albahaca"],
        "ingredients": ["bacon"],
        "clients": ["paula", "marta", "paco"]
    }
]
```

- _{id}_: "abc"
- _{cantidad elemento actual}_: 3
- _{cantidad elemento nuevo}_: 2
- _{lista de clientes actual}_: `["paula", "marta", "paco"]`
- _{lista de clientes nuevo}_: `["lola", "antonio"]`
- _{elemento actual}_:

```json
{
    "section": "pizzas",
    "element": "carbonara",
    "variants": [
        {
            "name": "tamaño",
            "value": "familiar"
        }
    ],
    "extras": ["albahaca"],
    "ingredients": ["bacon"],
    "quantity": "{cantidad elemento actual}",
    "clients": "{lista de clientes actual}"
}
```
- _{elemento nuevo}_:
```json
{
    "section": "pizzas",
    "element": "carbonara",
    "variants": [
        {
            "name": "tamaño",
            "value": "familiar"
        }
    ],
    "extras": ["albahaca"],
    "ingredients": ["bacon"],
    "quantity": "{cantidad elemento nuevo}",
    "clients": "{lista de clientes nuevo}"
}
```

Resultado: 
```json
{
    "section": "bebidas",
    "element": "nestea",
    "quantity": "{cantidad elemento actual} + {cantidad elemento nuevo}",
    "clients": "{lista de clientes actual} union {lista de clientes nuevo}"
}
```

#### Test en Python
`test_add_element__when_element_is_correct_and_element_is_alerady_exists_and_the_sum_of_both_quantities_is_grater_than_zero__then_element_quantity_is_updated_to_the_sum_of_them_and_return_updated_element()`

### Caso 9: Añadir un elemento cuando el elemento es correcto, ya existe en la comanda y la suma de las cantidades es menor o igual a cero

Este caso es para añadir un elemento que ya existe en la comanda actual. Si la suma de las cantidades resulta en cero o menor, se devuelve un HTTP Status 400 (Bad Request).

- **Método**: Añadir elemento (`add_element`).
- **Escenario**: Elemento es correcto, ya existe y la suma de las cantidades es menor o igual a cero.
- **Tipo**: Error.

#### Caso de prueba

- **Dado que** se crea un nuevo pedido con identificador _{id}_
- **Y** el elemento _{elemento nuevo}_ es correcto
- **Y** existe un elemento _{elemento actual}_ en la comanda actual
- **Y** el elemento _{elemento actual}_ es el mismo que el elemento _{elemento nuevo}_
- **Y** la cantidad del elemento _{elemento actual}_ es _{cantidad elemento actual}_ 
- **Y** la cantidad del elemento _{elemento nuevo}_ es _{cantidad elemento nuevo}_
- **Y** la suma _{cantidad elemento actual}_ y _{cantidad elemento nuevo}_ es menor o igual a 0
- **Cuando** se solicita añadir un elemento _{elemento nuevo}_ al pedido con identificador _{id}_.
- **Entonces** el sistema devuelve un HTTP Status 400 (Bad Request).

#### Ejemplos

- _{id}_: "abc"
- _{cantidad elemento actual}_: 1
- _{cantidad elemento nuevo}_: -1
- _{elemento actual}_:

```json
{
    "section": "bebidas",
    "element": "nestea",
    "quantity": "{cantidad elemento actual}",
    "clients": ["marcos"]
}
```
- _{elemento nuevo}_:
```json
{
    "section": "bebidas",
    "element": "nestea",
    "quantity": "{cantidad elemento nuevo}",
    "clients": ["lola"]
}
```

#### Test en Python
`test_add_element__when_element_is_correct_and_element_is_alerady_exists_and_the_sum_of_both_quantities_is_less_or_equals_to_zero__then_http_status_400_bad_request()`

### Caso 10: Añadir un elemento cuando el pedido no existe

Este caso se da cuando se intenta añadir un elemento a un pedido que no existe.

- **Método**: Añadir elemento (`add_element`).
- **Escenario**: Pedido no existe.
- **Tipo**: Error.

#### Caso de prueba

- **Dado que** no existe ningun pedido cuyo identificado sea _{id}_.
- **Cuando** se solicita añadir un elemento al pedido con identificador _{id}_.
- **Entonces** el sistema devuelve un HTTP Status 404 (Not Found).

#### Ejemplos

- _{id}_: "abc"

#### Test en Python
`test_add_element__when_order_does_not_exists__then_http_status_404_not_found()`

### Caso 11: Añadir un elemento cuando el elemento es inválido

Este caso trata de añadir un elemento inválido a la comanda actual de un pedido existente. Podría ser que el elemento no tiene todos los campos necesarios, o los valores de los campos son incorrectos.

- **Método**: Añadir elemento (`add_element`).
- **Escenario**: El elemento es inválido.
- **Tipo**: Error.

#### Caso de prueba

- **Dado que** se crea un nuevo pedido con identificador _{id}_.
- **Y** el elemento _{elemento}_ es inválido.
- **Cuando** se solicita añadir _{elemento}_ al pedido con identificador _{id}_.
- **Entonces** el sistema devuelve un HTTP Status 422 (Unprocessable Entity).

#### Ejemplos

##### Falta campo requerido

- _{id}_: "abc"
- _{element}_:

```json
{
    "section": "bebidas",
    "quantity": 1,
    "clients": ["marcos"]
}
```

##### Cantidad cero

- _{id}_: "abc"
- _{element}_:

```json
{
    "section": "bebidas",
    "element": "nestea",
    "quantity": 0,
    "clients": ["marcos"]
}
```

#### Test en Python

`test_add_element__when_element_is_not_correct__then_http_status_422_unprocessable_entity()`

### Caso 12: Añadir un elemento cuando el elemento no existe

Este caso trata de añadir un elemento que no existe a la comanda actual de un pedido existente. Puede ser que la sección no exista o que el elemento dentro de la sección no exista

- **Método**: Añadir elemento (`add_element`).
- **Escenario**: El elemento no existe.
- **Tipo**: Error.

#### Caso de prueba

- **Dado que** se crea un nuevo pedido con identificador _{id}_.
- **Y** el elemento _{elemento}_ no existe.
- **Cuando** se solicita añadir _{elemento}_ al pedido con identificador _{id}_.
- **Entonces** el sistema devuelve un HTTP Status 404 (Not Found).

#### Ejemplos

##### Sección no existe

- _{id}_: "abc"
- _{element}_:

```json
{
    "section": "seccion que no existe",
    "element": "nestea",
    "quantity": 1,
    "clients": ["marcos"]
}
```

##### Cantidad cero

- _{id}_: "abc"
- _{element}_:

```json
{
    "section": "bebidas",
    "element": "elemento que no existe",
    "quantity": 0,
    "clients": ["marcos"]
}
```

#### Test en Python

`test_add_element__when_element_does_not_exists__then_http_status_404_not_found()`

## Recibo

### Caso de prueba 1: Generar el recibo cuando hay comandas una comanda confirmada

En este caso se intenta generar un recibo para un pedido que existe y que tiene una comanda confirmada. El recibo se genera a partir de la comanda confirmada.

**Método**: Generar recibo (`generate_receipt`).
**Escenario**: Pedido existe y hay una comanda confirmada.
**Tipo**: Éxito.

#### Caso de prueba

- **Dado que** se crea un nuevo pedido con identificador _{id}_.
- **Y** el cliente _{cliente]_ añade el elemento _{elemento}_ a la comanda actual del pedido con identificador _{id}_.
- **Y** se confirma la comanda actual del pedido con identificador _{id}.
- **Y** el precio de del elemento _{elemento}_ es de _{precio}_. 
- **Cuando** se solicita generar el recibo del pedido con identificador _{id}_.
- **Entonces** el sistema genera el recibo _{recibo}_ a partir de la comanda confirmada.
- **Y** el sistema devuelve un HTTP Status 200 (OK).

#### Ejemplos

##### Un elemento simple

- _{id}_: "abc"
- _{cliente}_: "marcos"
- _{precio}_: 2.5
- _{elemento}_:

```json
{
    "section": "bebidas",
    "element": "nestea",
    "quantity": 1,
    "clients": {cliente}
}
```

- _{Recibo}_:

```json
[
    {
        **{element},
        "clients": [{cliente}],
        "price": {precio},
    }
]
```

##### Un elemento complejo

- _{id}_: "abc"
- _{cliente}_: "marcos"
- _{precio}_: 2.5
- _{elemento}_:

```json
[
    {
        "section": "pizzas",
        "element": "carbonara",
        "quantity": 1,
        "variants": [
            {
                "name": "tamaño",
                "value": "familiar"
            }
        ],
        "extras": ["albahaca"],
        "ingredients": ["bacon"],
        "clients": [{cliente}]
    }
]
```

- _{recibo}_:

```json
[
    {
        **{element},
        "clients": [{cliente}],
        "price": {precio},
    }
]
```

### Caso de prueba 2: Generar el recibo cuando hay varias comandas confirmadas

En este caso se intenta generar un recibo para un pedido que existe y que tiene varias comandas confirmadas. El recibo se genera a partir de las comandas confirmadas.

**Método**: Generar recibo (`generate_receipt`).
**Escenario**: Pedido existe y hay varias comandas confirmadas.
**Tipo**: Éxito.

#### Caso de prueba

- **Dado que** se crea un nuevo pedido con identificador _{id}_.
- **Y** el cliente _{cliente}_ añade el elemento _{elemento}_ a la comanda actual del pedido con identificador _{id}_.
- **Y** se confirma la comanda actual del pedido con identificador _{id}_.
- **Y** el cliente _{cliente}_ añade el elemento _{elemento}_ a la comanda actual del pedido con identificador _{id}_.
- **Y** se confirma la comanda actual del pedido con identificador _{id}_.
- **Cuando** se solicita generar el recibo del pedido con identificador _{id}_.
- **Entonces** el sistema genera el recibo _{recibo}_ a partir de las comandas confirmadas.

#### Ejemplos

##### Un elemento simple

- _{id}_: "abc"
- _{cliente}_: "marcos"
- _{precio}_: 2.5
- _{elemento}_:

```json
{
    "section": "bebidas",
    "element": "nestea",
    "quantity": 2,
    "clients": {cliente}
}
```

- _{Recibo}_:

```json
[
    {
        **{element},
        "clients": [{cliente}],
        "price": 2 * {precio},
    }
]
```

##### Un elemento complejo

- _{id}_: "abc"
- _{cliente}_: "marcos"
- _{precio}_: 2.5
- _{elemento}_:

```json
[
    {
        "section": "pizzas",
        "element": "carbonara",
        "quantity": 2,
        "variants": [
            {
                "name": "tamaño",
                "value": "familiar"
            }
        ],
        "extras": ["albahaca"],
        "ingredients": ["bacon"],
        "clients": [{cliente}]
    }
]
```

- _{recibo}_:

```json
[
    {
        **{element},
        "clients": [{cliente}],
        "price": 2 * {precio},
    }
]
```

### Caso de prueba 3: Generar el recibo cuando no hay comandas confirmadas

En este caso se intenta generar un recibo para un pedido que existe y que no tiene comandas confirmadas. Se revolverá un error con codigo HTTP 400 (Bad Request).

**Método**: Generar recibo (`generate_receipt`).
**Escenario**: Pedido existe y no hay comandas confirmadas.
**Tipo**: Error.

#### Caso de prueba

- **Dado que** se crea un nuevo pedido con identificador _{id}_.
- **Cuando** se solicita generar el recibo del pedido con identificador _{id}_.
- **Entonces** el sistema devuelve un HTTP Status 400 (Bad Request).

#### Ejemplo

- _{id}_: "abc"

### Caso de prueba 4: Generar el recibo cuando el pedido no existe

En este caso se intenta generar un recibo para un pedido que no existe. Se revolverá un error con codigo HTTP 404 (Not Found).

**Método**: Generar recibo (`generate_receipt`).
**Escenario**: Pedido no existe.
**Tipo**: Error.

#### Caso de prueba

- **Dado que** no existe ningún pedido con identificador _{id}_.
- **Cuando** se solicita generar el recibo del pedido con identificador _{id}_.
- **Entonces** el sistema devuelve un HTTP Status 404 (Not Found).

#### Ejemplo

- _{id}_: "abc"

## Ver por pagar

### Caso de prueba 1: Ver por pagar total completo 

En este caso se intenta ver lo que queda por pagar en total cuando todavía no se ha pagado nada. En este caso debe devolver lo mismo que el recibo total.

**Método**: Ver recibo (get_to_be_paid)
**Escenario**: Ver por pagar total cuando no se ha pagado nada todavía.
**Tipo**: Éxito

#### Caso de prueba

- **Dado que** se crea un nuevo pedido con identificador _{id}_.
- **Y** el cliente _{cliente}_ añade el elemento _{elemento}_ a la comanda actual del pedido con identificador _{id}_.
- **Y** el cliente _{cliente}_ añade el elemento _{elemento}_ a la comanda actual del pedido con identificador _{id}_.
- **Y** se confirma la comanda actual del pedido con identificador _{id}_.
- **Y** se genera el recibo del pedido con identificador _{id}_.
- **Cuando** se solicita ver el total de lo que queda por pagar del pedido con identificador _{id}_.
- **Entonces** el sistema devuelve lo que queda por pagar _{por_pagar}_, que corresponde con el recibo total.

#### Ejemplo

- _{id}_: "abc"
- _{cliente}_: "marcos"
- _{precio}_: 2.5
- _{elemento}_:

```json
{
    "section": "bebidas",
    "element": "nestea",
    "quantity": 1,
    "clients": [{cliente}]
}
```

- _{por_pagar}_:

```json
[
    {
        "section": "bebidas",
        "element": "nestea",
        "quantity": 2,
        "clients": [{cliente}, {cliente}],
        "price": {precio},
        "total": 2 * {precio},
    }
]
```

### Caso de prueba 2: Ver por pagar total parcial

En este caso se intenta ver lo que queda por pagar en total cuando todavía ya se ha pagado algo. En este caso debe devolver lo mismo que el recibo total menos lo que se ha pagado ya.

**Método**: Ver recibo (get_to_be_paid)
**Escenario**: Ver por pagar total cuando no se ha pagado nada todavía.
**Tipo**: Éxito

#### Caso de prueba

- **Dado que** se crea un nuevo pedido con identificador _{id}_.
- **Y** el cliente _{cliente1}_ añade el elemento _{elemento1}_ a la comanda actual del pedido con identificador _{id}_.
- **Y** el cliente _{cliente2}_ añade el elemento _{elemento2}_ a la comanda actual del pedido con identificador _{id}_.
- **Y** se confirma la comanda actual del pedido con identificador _{id}_.
- **Y** se genera el recibo del pedido con identificador _{id}_.
- **Y** se paga _{pagado}_ del pedido con identificador _{id}_.
- **Cuando** se solicita ver el total de lo que queda por pagar del pedido con identificador _{id}_.
- **Entonces** el sistema devuelve lo que queda por pagar _{por_pagar}_, que corresponde con el recibo total menos lo que se ha pagado ya _{pagado}_.

#### Ejemplo

- _{id}_: "abc"
- _{cliente1}_: "marcos"
- _{cliente2}_: "lola"
- _{precio}_: 2.5
- _{elemento1}_:
```json
{
    "section": "bebidas",
    "element": "nestea",
    "quantity": 1,
    "clients": {cliente1}
}
```
- _{elemento2}_:
```json
{
    "section": "bebidas",
    "element": "coca-cola",
    "quantity": 1,
    "clients": {cliente2}
}
```
- _{pagado}_: [_{elemento1}_]
- _{por_pagar}_: [_{elemento2}_]

### Caso de prueba 4: Ver por pagar individual

En este caso se intenta ver lo que queda por pagar de forma indiviudal, es decir, para un comensal concreto. Se debe devolver los elementos que ha pedido el cliente concreto.

**Método**: Ver recibo (get_to_be_paid)
**Escenario**: Ver por pagar individual cuando no se ha pagado nada todavía.
**Tipo**: Éxito

#### Caso de prueba

- **Dado que** se crea un nuevo pedido con identificador _{id}_.
- **Y** el cliente _{cliente1}_ añade el elemento _{elemento1}_ a la comanda actual del pedido con identificador _{id}_.
- **Y** el cliente _{cliente2}_ añade el elemento _{elemento2}_ a la comanda actual del pedido con identificador _{id}_.
- **Y** se confirma la comanda actual del pedido con identificador _{id}_.
- **Y** se genera el recibo del pedido con identificador _{id}_.
- **Cuando** se solicita ver lo que queda por pagar para el cliente _{cliente1}_.
- **Entonces** el sistema devuelve el elemento _{elemento1}_.

#### Ejemplo

- _{id}_: "abc"
- _{cliente1}_: "marcos"
- _{cliente2}_: "lola"
- _{precio}_: 2.5
- _{elemento1}_:
```json
{
    "section": "bebidas",
    "element": "nestea",
    "quantity": 1,
    "clients": {cliente1}
}
```
- _{elemento2}_:
```json
{
    "section": "bebidas",
    "element": "coca-cola",
    "quantity": 1,
    "clients": {cliente2}
}
```
- _{por_pagar}_: [_{elemento1}_]

### Caso de prueba 3: Ver por pagar total cuando no se ha generado recibo

En este caso se intenta ver lo que queda por pagar cuando no se ha generado el recibo. Se debe devolver un error con código HTTP 400 (Bad Request).

- **Método**: Ver recibo (get_to_be_paid)
- **Escenario**: Ver por pagar total cuando no se ha generado recibo.
- **Tipo**: Error

#### Caso de prueba

- **Dado que** se crea un nuevo pedido con identificador _{id}_.
- **Cuando** se solicita ver el total de lo que queda por pagar del pedido con identificador _{id}_.
- **Entonces** el sistema devuelve un HTTP Status 400 (Bad Request).

### Caso de prueba 5: Ver por pagar individual cuando no se ha generado recibo

En este caso se intenta ver lo que queda por pagar de forma individual cuando no se ha generado el recibo. Se debe devolver un error con código HTTP 400 (Bad Request).

- **Método**: Ver recibo (get_to_be_paid)
- **Escenario**: Ver por pagar individual cuando no se ha generado recibo.
- **Tipo**: Error

#### Caso de prueba

- **Dado que** se crea un nuevo pedido con identificador _{id}_.
- **Cuando** se solicita ver lo que queda por pagar para el cliente _{cliente1}_.
- **Entonces** el sistema devuelve un HTTP Status 400 (Bad Request).

## Pagar

### Caso de prueba 1: Pagar total completo

En este caso se intenta pagar todo lo que queda por pagar cuando todavía no se ha pagado nada. Tras realizar el pago, se debe vaciar la lista de elementos por pagar.

**Método**: Pagar (pay)
**Escenario**: Pagar total cuando no se ha pagado nada todavía.
**Tipo**: Éxito

#### Caso de prueba

- **Dado que** se crea un nuevo pedido con identificador _{id}_.
- **Y** el cliente _{cliente1}_ añade el elemento _{elemento1}_ a la comanda actual del pedido con identificador _{id}_.
- **Y** el cliente _{cliente2}_ añade el elemento _{elemento2}_ a la comanda actual del pedido con identificador _{id}_.
- **Y** se confirma la comanda actual del pedido con identificador _{id}_.
- **Y** se genera el recibo del pedido con identificador _{id}_.
- **Y** se solicita pagar el total de lo que queda por pagar del pedido con identificador _{id}_.
- **Cuando** se solicita ver el total de lo que queda por pagar del pedido con identificador _{id}_.
- **Entonces** el sistema devuelve una lista vacía.
- **Y** el sistema devuelve un HTTP Status 200 (OK).

#### Ejemplo

- _{id}_: "abc"
- _{cliente1}_: "marcos"
- _{cliente2}_: "lola"
- _{precio}_: 2.5
- _{elemento1}_:
```json
{
    "section": "bebidas",
    "element": "nestea",
    "quantity": 1,
    "clients": {cliente1}
}
```
- _{elemento2}_:
```json
{
    "section": "bebidas",
    "element": "coca-cola",
    "quantity": 1,
    "clients": {cliente2}
}
```

### Caso de prueba 2: Pagar parcial con por pagar total completo

En este caso se intenta pagar parte de lo que queda por pagar partiendo del recibo toal. Tras realizar el pago, se debe devolver lo que queda por pagar, que debe corresponder con el recibo total menos lo que se ha pagado.

**Método**: Pagar (pay)
**Escenario**: Pagar parcial cuando no se ha pagado nada todavía.
**Tipo**: Éxito

#### Caso de prueba

- **Dado que** se crea un nuevo pedido con identificador _{id}_.
- **Y** el cliente _{cliente1}_ añade el elemento _{elemento1}_ a la comanda actual del pedido con identificador _{id}_.
- **Y** el cliente _{cliente2}_ añade el elemento _{elemento2}_ a la comanda actual del pedido con identificador _{id}_.
- **Y** se confirma la comanda actual del pedido con identificador _{id}_.
- **Y** se genera el recibo del pedido con identificador _{id}_.
- **Y** se solicita pagar el elemento _{elemento1}_ del pedido con identificador _{id}_.
- **Cuando** se solicita ver el total de lo que queda por pagar del pedido con identificador _{id}_.
- **Entonces** el sistema devuelve lo que queda por pagar, que es el elemento _{elemento2}_.

#### Ejemplo

- _{id}_: "abc"
- _{cliente1}_: "marcos"
- _{cliente2}_: "lola"
- _{precio}_: 2.5
- _{elemento1}_:
```json
{
    "section": "bebidas",
    "element": "nestea",
    "quantity": 1,
    "clients": {cliente1}
}
```
- _{elemento2}_:
```json
{
    "section": "bebidas",
    "element": "coca-cola",
    "quantity": 1,
    "clients": {cliente2}
}
```

### Caso de prueba 3: Pagar parcial con por pagar total parcial

En este caso se intenta pagar parte de lo que queda por pagar habiendose pagado ya algo. Tras realizar el pago, se debe devolver lo que queda por pagar, que debe corresponder con el recibo total menos lo que ya se había pagado menos lo que se ha pagado ahora.

**Método**: Pagar (pay)
**Escenario**: Pagar parcial cuando no ya se ha pagado algo.
**Tipo**: Éxito

#### Caso de prueba

- **Dado que** se crea un nuevo pedido con identificador _{id}_.
- **Y** el cliente _{cliente1}_ añade el elemento _{elemento1}_ a la comanda actual del pedido con identificador _{id}_.
- **Y** el cliente _{cliente2}_ añade el elemento _{elemento2}_ a la comanda actual del pedido con identificador _{id}_.
- **Y** se confirma la comanda actual del pedido con identificador _{id}_.
- **Y** se genera el recibo del pedido con identificador _{id}_.
- **Y** se solicita pagar el elemento _{elemento1}_ del pedido con identificador _{id}_.
- **Y** se solicita pagar el elemento _{elemento2}_ del pedido con identificador _{id}_.
- **Cuando** se solicita ver el total de lo que queda por pagar del pedido con identificador _{id}_.
- **Entonces** el sistema devuelve lo que queda por pagar, que es una lista vacía.
- **Y** el sistema devuelve un HTTP Status 200 (OK).

#### Ejemplo

- _{id}_: "abc"
- _{cliente1}_: "marcos"
- _{cliente2}_: "lola"
- _{precio}_: 2.5
- _{elemento1}_:
```json
{
    "section": "bebidas",
    "element": "nestea",
    "quantity": 1,
    "clients": {cliente1}
}
```
- _{elemento2}_:
```json
{
    "section": "bebidas",
    "element": "coca-cola",
    "quantity": 1,
    "clients": {cliente2}
}
```

### Caso de prueba 4: Pagar total cuando no se ha generado recibo

En este caso se intenta pagar todo lo que queda por pagar cuando no se ha generado el recibo. Se debe devolver un error con código HTTP 400 (Bad Request).

**Método**: Pagar (pay)
**Escenario**: Pagar total cuando no se ha generado recibo.
**Tipo**: Error

#### Caso de prueba

- **Dado que** se crea un nuevo pedido con identificador _{id}_.
- **Cuando** se solicita pagar el total de lo que queda por pagar del pedido con identificador _{id}_.
- **Entonces** el sistema devuelve un HTTP Status 400 (Bad Request).




