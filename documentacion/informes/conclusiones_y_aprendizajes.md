# Conclusiones y aprendizajes

- Para definir el grado de detalle de los casos de uso hay que preguntarse cual es la finalidad. ¿Son casos de uso para el equipo de desarrollo? Entonces puedes incluir mucho detalle de cada operación que realiza el sistema, sino no hace falta tanto detalle, mantenlo simple.
- Los principios SOLID está bien tenerlos presentes a la hora de programar.
- Es muy importante la documentación antes de programar. Es la diferencia entre ser ingeniero y ser programador.
- Merece la pena hacer tests antes de programar, ahorra mucho tiempo a la larga.
- Es muy importante definir una semántica tanto para la documentación como para el código.
- Definir una buena arquitectura en capas es crucial para reducir el acoplamiento y duplicidad.
- El método optimistic concurrency control (OCC) está muy bien porque es simple. Pero obliga a llevar un control de errores muy cuidado, ya que cuando hay colisiones se produciran errores que normalmente no se producirían.
- El uso de excepciones desacopla el control de flujo de la lógica de negocio.
- El método OCC asegura la atomicidad. Eso junto a un control de errores cuando hay conflicto es suficiente, no hace falta ver todas las posibilidades de los conflictos que puede haber.
- En el método OCC no hay problema en hacer muchos get, ya que no cambian el estado de la base de datos. Eso permite desacoplar los get. Por ejemplo haciendo un get_version en vez de devolverlo como tupla de otros métodos get.
- Hay que diferenciar entre los casos de uso de un usuario usando el frontend y los casos de uso que permite el backend.
- Es esencial mantener los casos de uso del backend lo más reducido posible, ya que reduce la complejidad y posibilidades de errores inesperados.
- La capa de persistencia debe ser tipo CRUD. Puedes tener CRUD para cada atributo de un documento. Es conveniente mantener al mínimo el CRUD, es decir, si para un cierto atributo solo necesitas hacer POST, no hagas todo el CRUD, haz solo el POST.
- Los casos de prueba deben segir los principios SMART. Puedes parametrizarlos.
- Se pueden hacer mocks de funciones concretas, aunque sean importadas, para módulos concretos.
- El `with` de python se puede definir con las funcines __enter__ y __exit__ de una clase.
- El `yield` de python define un generador y lo que hace es como un return cada vez que ejecuta `yield`, pero que cuando se le devuelve el contro sigue por donde iba. Es muy útil para algunas cosas. Si se usa con los `fixture` de pytest no hay que devolver el control explícitamente.
- 
