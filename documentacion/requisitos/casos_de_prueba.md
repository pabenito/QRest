# Casos de prueba del Backend

## Pedido

### Estructura de datos

```
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
- **pedido existe**: Se refiere a que hay algún pedido cuyo identificador coincida con el introducido.

### Caso 1: Obtener la comanda actual cuando existe

- **Método**: Ver comanda actual (`get_current_command`).

#### Caso de prueba

- **Dado que** se crea nuevo pedido con identificador _{id}_.
- **Y** el comensal _{comensal}_ añade _{unidades}_ unidades del elemento _{elemento}_ de la sección _{seccion}_ al la comanda actual.
- **Cuando** se solicita ver la comanda actual del pedido con identificador `{id}`
- **Entonces** el sistema devuelve la comanda actual que contiene _{unidades}_ unidades del elemento _{elemento}_ de la sección _{sección}_ y en cuya lista de clientes es hay _{unidades}_ veces el identificador del comensal _{comensal}_

#### Parámetros

#### Un elemento simple

- **{id}**: "abc"
- **{elemento}**: "carbonara"
- **{sección}**: "pizzas"
- **{unidades}**: 1

Resultado:

```json
[
  {
    "section": "pizzas",
    "element": "carbonara",
    "quantity": 1,
    "clients": ["paula"]
  }
]
```

