# Manual de usuario de QRest

El manual de usuario de QRest muestra todo el flujo de un comensal desde que se sienta en la mesa hasta que paga.

## Supuesto

Para ello vamos a poner el siguiente supuesto:

1. Pedro y Lucía llegan a un bar con el sistema QRest.
2. Pedro y Lucía se sientan en la mesa.
3. Pedro coge su teléfono y escanéa el QR en la mesa.
4. En el teléfono de pedro se muestra una pantalla con un QR para compartir.
5. Lucía saca su teléfono y escanéa el QR del teléfono de Pedro.
6. En el teléfono de Lucía se muestra también la pantalla con el QR para compartir.
7. Pedro y Lucía seleccionan la opción _Ir a la Carta_
8. En los teléfonos de ambos se muestra la carta.
9. Pedro pide una Coca-Cola y Lucía un Sprite.
10. Pedro selecciona la opción _Ver pedido_.
11. En el teléfono de Pedro se muestra el resumen del pedido.
12. Pedro selecciona la opción de _Volver a la carta_.
13. Lucía selecciona la opción de _Ver pedido_.
14. En el teléfono de Lucía se muestra el resumen del pedido.
15. Lucía añade una Coca-Cola.
16. Lucía seleccina la opción _Pedir_.
17. El teléfono de Lucía muestra la carta con un mensaje de confirmación. Ambas cartas se muestran sin elementos por pedir.
18. Pedro selecciona la opción _Pedir cuenta_.
19. Ambos teéfonos muestran lo que queda por pagar total.
20. Lucía selecciona la opción _Ver por pagar individual_.
21. El teléfono de Lucía muestra solo lo que ella ha pedido.
22. Lucía selecciona la opción _Pagar_.
23. El teléfono de Lucía muestra una ventana emergente indicando que pague en caja. Y en el teléfono del empleado del restaurante se muestra que Lucía quiere pagar su parte.
24. Lucía se dirige a la caja para pagar.
25. El empleado del restaurante selecciona la opción _Pagado_ sobre el pedido de Lucía.
26. En el teléfono de Lucía se muestra lo que queda por pagar total con un mensaje confirmando que se ha padago su parte. Mientras que en el teléfono del empleado del restaurante ya no se muestra como pediente de pago el recibo de Lucía.
27. Pedro selecciona la opción _Pagar_.
28. El teléfono de Pedro muestra una ventana emergente indicando que pague en caja. Y en el teléfono del empleado del restaurante se muestra que Pedro quiere pagar su parte.
28. Pedro se dirige a pagar en Caja.
29. El empleado del restaurante selecciona la opción _Pagado_ sobre el pedido de Pedro.
30. En el teléfono de Pedro se muestra lo que queda por pagar total, que es vacío, con un mensaje confirmando que se ha pagado lo que quedaba por pagar. Mientras que en el teléfono del empleado del restaurante ya no se muestra como pediente de pago el pedido de Pedro y Lucía.

## Ejemplo

### Llegada al bar

Pedro y Lucía llegan a un bar, el cual dispone del servicio de gestión de comandas QRest. Ambos se sientan en la mesa, donde ven el QR que tiene que escanear para ver la carta. Pedro coge su teléfono y escanéa el QR en la mesa. En el teléfono de pedro se muestra una pantalla con un QR para compartir. Lucía saca su teléfono y escanéa el QR del teléfono de Pedro. En el teléfono de Lucía se muestra también la pantalla con el QR para compartir.

![Sincronización con QR - Pedro (izquierda) | Lucía (derecha)](./img/manual/1_sincronizacion.png)

### Añadir al pedido

Pedro y Lucía seleccionan la opción _Ir a la Carta_. En los teléfonos de ambos se muestra la carta. Pedro pide una Coca-Cola y Lucía un Sprite. Pedro selecciona la opción _Ver pedido_.

![Seleccionan _Ir a la Carta_ - Pedro (izquierda) | Lucía (derecha)](./img/manual/2_ir_a_carta.png)
![Muestr carta - Pedro (izquierda) | Lucía (derecha)](./img/manual/3_carta.png)
![Pedro pide una Coca-Cola - Pedro (izquierda) | Lucía (derecha)](./img/manual/4_pedro_coca_cola.png)
![Lucía pide un Sprite - Pedro (izquierda) | Lucía (derecha)](./img/manual/5_lucia_sprite.png)
![Pedro selecciona _Ver pedido_](./img/manual/6_pedro_ver_pedido.png)

### Pedir

En el teléfono de Pedro se muestra el resumen del pedido. Pedro selecciona la opción de _Volver a la carta_. Lucía selecciona la opción de _Ver pedido_. En el teléfono de Lucía se muestra el resumen del pedido. Lucía añade una Coca-Cola. Lucía seleccina la opción _Pedir_. El teléfono de Lucía muestra la carta con un mensaje de confirmación. Ambas cartas se muestran sin elementos por pedir.

![Pedro resumen del pedido y volver carta - Pedro (izquierda) | Lucía (derecha)](./img/manual/6_pedro_volver_carta.png)
![Lucía resumen del pedido y pedir - Pedro (izquierda) | Lucía (derecha)](./img/manual/7_lucia_pedir.png)
![Confirmación de comanda confirmada - Pedro (izquierda) | Lucía (derecha)](./img/manual/8_comanda_confirmada.png)

### Pedir cuenta

Pedro selecciona la opción _Pedir cuenta_. Ambos teléfonos muestran lo que queda por pagar total. Lucía selecciona la opción _Ver por pagar individual_.

![Pedro pedir cuenta - Pedro (izquierda) | Lucía (derecha)](./img/manual/9_pedro_pedir_cuenta.png)
![Por pagar y Lucía ver individual - Pedro (izquierda) | Lucía (derecha)](./img/manual/10_lucia_individual.png)

### Lucía paga

El teléfono de Lucía muestra solo lo que ella ha pedido. Lucía selecciona la opción _Pagar_. El teléfono de Lucía muestra una ventana emergente indicando que pague en caja. Y en el teléfono del empleado del restaurante se muestra que Lucía quiere pagar su parte. Lucía se dirige a la caja para pagar. El empleado del restaurante selecciona la opción _Pagado_ sobre el pedido de Lucía. En el teléfono de Lucía se muestra lo que queda por pagar total con un mensaje confirmando que se ha padago su parte. Mientras que en el teléfono del empleado del restaurante ya no se muestra como pediente de pago el recibo de Lucía.

![Lucía pagar - Pedro (izquierda) | Lucía (derecha)](./img/manual/11_lucia_pagar.png)
![Lucía esperando a pagar - Pedro (izquierda) | Lucía (derecha)](./img/manual/12_lucia_esperando_pagar.png)
![Empleado pagado - Pedro (izquierda) | Lucía (derecha)](./img/manual/13_empleado_pagado.png)

### Pedro paga

Pedro selecciona la opción _Pagar_. El teléfono de Pedro muestra una ventana emergente indicando que pague en caja. Y en el teléfono del empleado del restaurante se muestra que Pedro quiere pagar su parte. Pedro se dirige a pagar en Caja. El empleado del restaurante selecciona la opción _Pagado_ sobre el pedido de Pedro. En el teléfono de Pedro se muestra lo que queda por pagar total, que es vacío, con un mensaje confirmando que se ha pagado lo que quedaba por pagar. Mientras que en el teléfono del empleado del restaurante ya no se muestra como pediente de pago el pedido de Pedro y Lucía.

![Pedro pagar - Pedro (izquierda) | Lucía (derecha)](./img/manual/14_pedro_pagar.png)
![Pedro esperando a pagar - Pedro (izquierda) | Lucía (derecha)](./img/manual/15_pedro_esperando_pagar.png)
![Empleado pagado - Pedro (izquierda) | Lucía (derecha)](./img/manual/16_empleado_pagado.png)

## Conclusión

En este ejemplo hemos podido observar el uso de la aplicación con todas sus funcionalidades, exceptuando las pantallas de Recibo total e individual, que hemos decidido no incluirlas en la aplicación final, aunque se pueden acceder a través de /mesa/{id}/recibo.

En este supuesto solo se ha hecho una comanda, pero se pueden hacer tantas comandas como se desee, simplemente volviendo a pedir las veces que se quiera antes de pedir la cuenta.

Con este ejemplo a modo de manual de usuario se pretende que cualquier cliente pueda hacer un uso de la aplicación siguiendo paso a paso este supuesto práctico.
