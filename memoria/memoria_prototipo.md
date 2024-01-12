# QRest

## Introducción

### Motivación

- Gran sector de la restauración en españa
- Sector poco automatizado
- Mismos problemas:
    - Toma de pedido: 
        - Toman pedido en libreta 
        - Costosos sistemas PDA con hardware especializado
    - Carta:
        - No digitalización de la carta
        - Carta guardada como PDF que hay que descargarse
        - Dificil actualizar la carta.
        - No hay flexibilidad de modificar la carta fácilmente.
        - No hay recomendaciones 
        - No hay sugerencias
        - No hay facilidad para volver a pedir lo que ya pediste
    - Tiempo de espera:
        - El cliente tiene que esperar a que el camarero pase por la mesa
        - El cliente tiene que esperar para pedir la cuenta
    - No hay registro:
        - No se lleva un registro de los platos más pedidos
        - No se lleva registro informatizado de los pedidos
        - No se hacen estadísticas
    - Web:
        - La mayoría de restaurantes no tienen web
        - Los restaurantes que tiene web tienen que buscar su propio dominio, hosting y mantenimiento.
        - Las web son costosas.
    - Pagos:
        - No suelen tener métodos de pago online.
        - No se suele llevar registro de qué ha pedido cada cliente, va todo la misma cuenta.
        - No se puede a veces pagar por separado.
        - No se puede consultar qué es lo que ha pedido cada persona.

### Análisis de soluciones en el mercado

Las opciones presentes en el mercado suelen caer en las siquientes categorías, pondremos un ejemplo de cada uno:

- Hardware especializado:
    - Pantalla de pedido centralizada: 
        - Ejemplo: McDonals
        - Problemas: 
            - Súper costoso y especializado.
            - Solo lo tienen actualmente franquicias.
            - Solo funciona para modelo de recoger en barra.
    - Hardware móvil: 
        - Ejemplo: PilarBox
        - Problemas:
            - Hardware costoso
            - Hay que cargar los dispositivos.
- Web + QR:
    - QR estático:
        - Variantes: En la mesa, tarjetita o en el servilletero.
        - Ejemplo: Qamarero. (En tarjetitas asociadas a una mesa)
        - Problemas:
            - Seguridad: Cuando vuelves a casa si sigues teniendo el QR o el enlace puedes pedir desde casa a la mesa aunque ya no estés allí.
            - Si están en la mesa y las mesas son modulares hay que ponerse en consenso de qué QR usar pedir.
            - Si las mesas se mueven ocasiona confusión para los camareros de donde está la mesa.
    - QR por pedido:
        - Funcionamiento: Cada vez que entra un cliente al restaurante se genera un QR para ese pedido.
        - Ejemplo: Yasaka, Servicio QbaR 
        - Problemas:
            - Tener que estar generando un QR nuevo por cada cliente (grupo de clientes) que entra.
            - Tener que atender a cada cliente que entra.
    - QR estático + contraseña:
        - Ejemplo: Sushi Son
        - Funcinamiento: Genera una contraseña diaria que el cliente tiene que usar.
        - Problemas:
            - Los mismos que los QR estático con la diferencia que el problema dura lo que dure la contraseña.
            - Incomodidad para el cliente, el tener que estar preguntando la contraseña.
            - Los camareros tienen que estar informando de la contraseña.            

Basicamente no encontramos una solución que llegue a resolver todos los problemas. Todos tienen algunas ventajas e inconvenientes.

Lista de opciones:

- Servicio QbaR: https://www.servicioqbar.com/
- PilarBox: https://pilarbox.com/
- McDonalds: https://mcdonalds.es/
- Burguer King: https://www.bk.com/
- Yasaka: https://yasaka.es/
- Qamarero: https://www.qamarero.com/


