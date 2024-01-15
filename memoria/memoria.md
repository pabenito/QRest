# QRest

## Resumen

En el contexto del crecimiento global del sector de la restauración, los restaurantes enfrentan desafíos significativos en la modernización de sus sistemas de gestión, especialmente en la gestión de comandas. Las soluciones existentes son a menudo costosas y poco accesibles para pequeñas empresas. El proyecto QRest aborda este desafío mediante el desarrollo de una solución integral y accesible para la gestión de comandas en restaurantes.

QRest es un sistema basado en web que ofrece una gama de funcionalidades clave para la gestión eficiente de restaurantes. Entre estas se incluyen la gestión de comandas a través de códigos QR, pagos, digitalización de menús, pedidos interactivos, y sugerencias basadas en pedidos anteriores. Esta solución integral no solo mejora la eficiencia operativa, sino que también reduce significativamente los costos y barreras de entrada para restaurantes de diversos tamaños.

El impacto de QRest es multifacético, ofreciendo una experiencia mejorada tanto para los clientes como para los propietarios de restaurantes. Los clientes disfrutan de una experiencia de pedido más fluida y personalizada, mientras que los restaurantes se benefician de una gestión más eficiente y una reducción en los costos operativos. Con QRest, los restaurantes pueden implementar un sistema de gestión de comandas moderno y eficiente sin la necesidad de una gran inversión inicial.

Palabras clave: Gestión de restaurantes, QRest, eficiencia operativa, automatización.

## Introducción

En este capítulo se exponen los problemas enfrentados en el sector de la resturación, las soluciones existentes en el ámbito de automatización de gestión de comandas, luego se expone lo que se quiere conseguir con este TFG y finalmente los puntos fuertes de la solución alcanzada.

### Problemas del sector

El sector de la restauración en España y a nivel mundial ha experimentado un notable crecimiento en las últimas décadas. Sin embargo, este crecimiento no se ha visto acompañado de una modernización adecuada en la gestión operativa de los restaurantes, especialmente para los establecimientos pequeños y medianos. La mayoría de estos restaurantes aún dependen de métodos anticuados y manuales para la gestión de comandas, enfrentando limitaciones significativas en su eficiencia operativa y capacidad para competir en un mercado cada vez más digitalizado.

Estos desafíos incluyen sistemas de toma de pedido obsoletos, a menudo basados en papel o dependientes de costosos sistemas PDA con hardware especializado. La digitalización de las cartas es mínima; principalmente basadas en PDFs subidos a servicios de almacenamiento en la nube; y su actualización y personalización resultan engorrosas y poco flexibles. Además, los restaurantes enfrentan ineficiencias en la gestión del tiempo de espera de los clientes, desde la toma del pedido hasta el pago de la cuenta. La falta de un registro informatizado de los pedidos impide realizar análisis y estadísticas que podrían mejorar la experiencia del cliente y la gestión del restaurante.

Otro aspecto crítico es la escasa presencia web de muchos restaurantes, combinada con la complejidad y el costo de mantener un sitio propio. En cuanto a los procesos de pago, la ausencia de métodos de pago online y la dificultad para gestionar pagos separados por cliente representan obstáculos adicionales para una experiencia de cliente óptima.

Esta combinación de factores resalta la necesidad de una solución que aborde estos múltiples desafíos de manera integral, ofreciendo a los restaurantes de todos los tamaños una forma accesible y eficiente de modernizar sus operaciones y mejorar la experiencia tanto para los clientes como para el personal del restaurante.

Esta situación presenta un desafío particularmente agudo para los pequeños restaurantes, que constituyen una parte significativa del sector de la restauración en España y en muchos otros países. Estos establecimientos, a menudo con recursos limitados y sin acceso a las economías de escala que benefician a las grandes cadenas, se encuentran en una posición especialmente vulnerable. La falta de sistemas de gestión eficientes y accesibles financieramente les obliga a lidiar con una gestión operativa ineficiente y obsoleta, lo que no solo reduce su competitividad sino que también puede afectar significativamente la experiencia del cliente y, en última instancia, su viabilidad como negocio.

Para muchos emprendedores y propietarios de pequeños restaurantes, estos desafíos representan barreras importantes al momento de iniciar o mantener su negocio. Se enfrentan a la necesidad de equilibrar la calidad del servicio y la eficiencia operativa con una inversión inicial y costes de mantenimiento limitados. Este conjunto de problemas puede hacer que la apertura y gestión de un restaurante sea una tarea desalentadora, poniendo en riesgo el crecimiento y la sostenibilidad de estos importantes actores del sector gastronómico. La urgencia de abordar estas dificultades subraya la necesidad de una solución como QRest, diseñada para ser accesible y beneficiosa para restaurantes de todos los tamaños, pero especialmente para aquellos pequeños establecimientos que son el corazón de la comunidad culinaria y cultural.

### Problemas de soluciones existentes

El mercado actual de sistemas de gestión para restaurantes ofrece una gama de soluciones que se pueden clasificar en dos categorías principales: hardware especializado y sistemas basados en web + QR. Cada una de estas categorías incluye varias opciones, cada una con sus características y desafíos únicos.

En la categoría de hardware especializado, encontramos soluciones como las pantallas de pedido centralizadas, ejemplificadas por las utilizadas en cadenas como McDonalds. Estos sistemas, aunque eficientes para modelos de servicio rápido en barra, presentan desafíos significativos en términos de costos elevados y especialización, lo que los hace inaccesibles para la mayoría de los restaurantes independientes o pequeñas franquicias. Además, su aplicación se limita a ciertos modelos de negocio, excluyendo a aquellos con un enfoque más tradicional o servicio en mesa.

Otra opción dentro del hardware especializado son los dispositivos móviles como los ofrecidos por PilarBox. Aunque estos sistemas mejoran la movilidad y la eficiencia del personal, suelen implicar una inversión considerable en hardware, además de la logística y el tiempo necesarios para mantener los dispositivos cargados y operativos, lo que puede ser un desafío en entornos de alta demanda.

Por otro lado, los sistemas basados en web + QR representan una alternativa tecnológicamente más sencilla, pero con sus propias limitaciones. Los QR estáticos, por ejemplo, pueden estar ubicados en las mesas o incluidos en tarjetas o servilleteros, como lo hace Qamarero. Sin embargo, estos sistemas plantean problemas de seguridad, ya que los clientes pueden seguir accediendo al sistema desde fuera del restaurante si conservan el QR o el enlace. Además, en restaurantes con mesas modulares o configuraciones cambiantes, pueden generar confusión tanto para los clientes como para el personal.

Los QR generados por pedido, como los utilizados por Yasaka y el Servicio QbaR, ofrecen una solución a algunos de estos problemas al crear un QR único para cada grupo de clientes. Sin embargo, esto requiere la generación constante de nuevos códigos y un nivel de atención personalizada para cada cliente que ingresa, lo que puede ser un proceso tedioso y lento durante los períodos de alta afluencia.

Finalmente, la variante de QR estático con contraseña, utilizada por ejemplos como Sushi Som, intenta abordar los problemas de seguridad, pero introduce una nueva capa de complejidad y potencial incomodidad tanto para los clientes, que deben obtener y recordar una contraseña, como para el personal, que debe comunicarla y gestionar su uso.

En resumen, aunque cada una de estas soluciones ofrece ventajas en ciertos aspectos, también presentan una serie de inconvenientes que limitan su eficacia y aceptación general en la industria de la restauración. Estos problemas son especialmente pronunciados en restaurantes más pequeños y establecimientos independientes, donde los costos, la complejidad y las limitaciones operativas pueden hacer que la implementación de estos sistemas sea impracticable.

### Motivación

La iniciativa para desarrollar QRest se originó a partir de experiencias personales significativas, complementadas por un fuerte interés en los desafíos técnicos. La concepción del proyecto surgió tras una visita al restaurante Yasaka, donde observé un sistema de pedidos basado en web y QR específico para el establecimiento, pero con claras deficiencias: una interfaz de usuario poco atractiva, falta de sincronización de pedidos y ausencia de funcionalidad para pagos individuales. Este escenario motivó una profunda reflexión y la decisión de investigar y desarrollar una solución más eficiente y adaptable para una variedad de restaurantes. Desde enero de 2023, he dedicado tiempo a explorar las soluciones existentes en el mercado, observando una evolución continua y la aparición de nuevas opciones a lo largo del año.

A nivel personal, mi interés en el desarrollo web y el desafío de abordar un problema complejo y relevante fueron catalizadores cruciales. Mi experiencia como cliente frecuente en restaurantes proporcionó una perspectiva única sobre las necesidades y desafíos en este sector. Adicionalmente, la posibilidad de transformar QRest en un emprendimiento viable post-TFG resonó con mis aspiraciones profesionales. El proyecto también representó una oportunidad excepcional para aplicar de forma práctica los conocimientos adquiridos en mi formación en Ingeniería del Software.

Técnicamente, la emergencia de soluciones de gestión para restaurantes en 2023 abrió un campo de investigación e innovación. La meta de desarrollar una aplicación escalable, capaz de resolver los problemas operativos de restaurantes de diferentes tamaños, en particular los más pequeños o recientemente inaugurados, era altamente atractiva. El proyecto requería la integración de varios aspectos técnicos complejos, incluyendo transacciones en bases de datos, sincronización en tiempo real con websockets, el uso de bases de datos NoSQL, y el desarrollo de modelos de datos complejos. Asimismo, se enfatizó en la privacidad y seguridad de los datos, implementando técnicas como el almacenamiento local en el navegador del usuario.

Desde la perspectiva de la ingeniería del software, el desafío de desarrollar una aplicación en un área naciente con limitadas referencias preexistentes fue una tarea considerable. Este proceso implicó adoptar metodologías adecuadas de desarrollo de software, definir requisitos claros, elaborar casos de uso y pruebas, y aplicar APIs y principios de programación orientada a objetos en Python y JavaScript, así como el uso de frameworks de desarrollo web. Además, la estructuración y el refactoring del proyecto fueron componentes clave para su éxito.

En conclusión, QRest es fruto de un equilibrio entre motivaciones personales y desafíos técnicos, resultando en una solución innovadora para los retos de la industria restaurantera y un proyecto de crecimiento personal y aplicación práctica de habilidades en ingeniería del software.

### Objetivos

Los objetivos del proyecto QRest se clasifican en tres categorías principales: personales, profesionales y específicos del proyecto, cada una contribuyendo al éxito y la realización integral del proyecto.

**Objetivos Personales:**
Mis metas personales se centran en el logro de un Trabajo de Fin de Grado que no solo me desafíe y emocione, sino que también represente un hito en mi desarrollo personal y profesional. Este proyecto es una plataforma para la realización de un emprendimiento post-TFG, ofreciendo una oportunidad única para aplicar y ampliar mi conocimiento en el desarrollo web y enriquecer mi portafolio profesional con una aplicación full-stack robusta y bien desarrollada.

**Objetivos Profesionales:**
Desde un punto de vista profesional, los objetivos están alineados con el fortalecimiento y la expansión de habilidades técnicas específicas. Esto incluye mejorar en el desarrollo de frontend, particularmente en JavaScript y CSS; dominar la sincronización en tiempo real utilizando Websockets; profundizar en MongoDB; entender las transacciones en bases de datos; explorar la arquitectura de software en aplicaciones web; diseñar y desarrollar APIs eficientes; y reforzar la programación orientada a

 objetos en Python y JavaScript. Además, se busca implementar metodologías ágiles en un proyecto de esta envergadura.

**Objetivos del Proyecto:**
Los objetivos específicos del proyecto incluyen el desarrollo de una solución que supere las limitaciones de las soluciones existentes en el mercado. Entre estos se encuentran la implementación de una sincronización efectiva de pedidos, la facilitación de pagos individuales, y la creación de una carta digital flexible y dinámica. Además, se pretende desarrollar un sistema de sugerencias basado en preferencias y pedidos anteriores, garantizar la privacidad y seguridad de los datos de los clientes, y manejar eficientemente la diversidad de situaciones en un restaurante real. Otro aspecto importante es la propuesta de soluciones innovadoras para los problemas de los sistemas basados en QR estáticos y con contraseña, y la minimización de la necesidad de hardware especializado en los restaurantes.

Estos objetivos delinean un compromiso con el desarrollo de una solución integral que responda a las necesidades de los clientes y los restaurantes, utilizando los conocimientos y habilidades adquiridos en el campo del desarrollo de software.

### Solución Propuesta para QRest

El objetivo del proyecto QRest es desarrollar una solución integral que aborde eficientemente una amplia gama de problemas enfrentados tanto por los restaurantes como por sus clientes. La solución buscará resolver estos problemas de manera económica, flexible, y con una mínima intrusión en los flujos de trabajo existentes.

**Problemas del Restaurante a Resolver:**
1. **Errores en la Toma de Comandas:** Implementar un sistema que reduzca los errores humanos en la toma de pedidos.
2. **Optimización del Tiempo del Personal:** Minimizar el tiempo dedicado por los camareros a tomar comandas, llevar la cuenta y cobrar, liberando así más tiempo para la atención al cliente y otras tareas.
3. **Automatización del Flujo de Trabajo:** Reducir errores relacionados con procesos manuales mediante la automatización de tareas como la gestión de pedidos y reservas.
4. **Presencia y Funcionalidad Web:** Proveer a los restaurantes de una página web propia y funcional que incluya una carta digitalizada fácilmente modificable.
5. **Registro de Pedidos:** Mantener un registro digitalizado y automatizado de todos los pedidos para una mejor gestión y análisis.
6. **Mejora en el Servicio de Pedidos a Domicilio y Reservas:** Digitalizar y simplificar los procesos de pedidos a domicilio y reservas de mesas, reemplazando los métodos telefónicos tradicionales.
7. **Gestión Efectiva de los Estados de los Pedidos:** Implementar un sistema que permita a los restaurantes y al personal ver y gestionar eficientemente el estado de los pedidos de cada mesa.

**Problemas del Cliente a Resolver:**
1. **Reducción de Tiempos de Espera:** Agilizar los procesos de pedir comandas, solicitar la cuenta y realizar el pago.
2. **Facilitación de Pedidos y Reservas:** Permitir a los clientes realizar pedidos a domicilio y reservas de mesas de manera online y sencilla.
3. **Prevención de Malentendidos y Facilidad en la División de Cuentas:** Ofrecer un sistema claro y preciso para evitar malentendidos en los pedidos y facilitar la división y el pago por separado de la cuenta.
4. **Seguimiento del Pedido:** Proporcionar a los clientes la capacidad de ver el estado actual de su pedido.

**Requisitos de la Solución Propuesta:**
1. **Digitalización Flexible de la Carta:** Un sistema que permita a los restaurantes actualizar y modificar fácilmente su carta digital.
2. **Pedidos Directos por Parte del Cliente:** Habilitar a los clientes para que realicen pedidos directamente desde sus dispositivos, mejorando la eficiencia y la experiencia del usuario.
3. **Sistema de Gestión de Comandas Adaptable:** Desarrollar un sistema que se ajuste a los diferentes flujos de trabajo de cada restaurante, evitando la necesidad de adaptaciones significativas en sus operaciones actuales.
4. **Registro Integral de Pedidos:** Asegurar un registro completo y automatizado de todos los pedidos para facilitar la gestión y el análisis.
5. **Recomendaciones Personalizadas:** Ofrecer recomendaciones tanto al restaurante como al cliente, basadas en pedidos anteriores y preferencias.
6. **Pagos Flexibles y Online:** Integrar opciones de pago por separado, online y en caja, para mayor comodidad y eficiencia.
7. **Reservas de Mesa Online y Pedidos a Domicilio:** Facilitar las reservas de mesas y los pedidos a domicilio a través de la web del restaurante.
8. **Sincronización de Pedidos en Mesas Compartidas:** Asegurar que los pedidos de clientes que comparten mesa estén sincronizados y gestionados eficazmente.
9. **Privacidad de Datos del Cliente:** Garantizar la seguridad y privacidad de los datos del cliente.
10. **Estado del Pedido y Flexibilidad en los Pedidos:** Permitir a los clientes ver el estado de su pedido y ofrecer flexibilidad en la modificación de sus pedidos, adaptándose a sus necesidades en tiempo real.
11. **Bajo Coste y Mínimo Hardware Necesario:** Desarrollar una solución que requiera una inversión inicial mínima y poco hardware adicional por parte del restaurante, haciéndola accesible incluso para establecimientos con recursos limitados.
12. **Integración y Sincronización de Servicios:** Asegurar que todos los componentes del sistema, desde la toma de pedidos hasta el pago y la gestión de reservas, estén integrados y sincronizados para una operatividad fluida y eficiente.
13. **Facilidad de Uso y Accesibilidad:** Crear una interfaz de usuario intuitiva y accesible tanto para el personal del restaurante como para los clientes, garantizando una experiencia de usuario agradable y sin complicaciones.
14. **Adaptabilidad a Diversos Modelos de Restaurante:** Diseñar la solución de manera que se pueda adaptar fácilmente a diferentes tipos y tamaños de restaurantes, desde pequeñas cafeterías hasta grandes cadenas, asegurando así una amplia aplicabilidad.

En resumen, la solución propuesta por QRest busca ofrecer una experiencia de restaurante mejorada y más eficiente, abordando los desafíos actuales tanto para el personal como para los clientes. Este sistema integral no solo mejorará la operatividad del restaurante y la satisfacción del cliente, sino que también impulsará la transformación digital en la industria de la restauración.

### Puntos Fuertes de QRest Frente a Competidores

QRest se distingue de sus competidores en el mercado de gestión de restaurantes a través de una combinación única de características de diseño, funcionalidad de producto e ingeniería. Cada uno de estos aspectos contribuye a crear una solución más robusta, flexible y centrada en el usuario.


**Características del Producto:**
1. **Pedidos Directos por Parte del Cliente:** Los clientes pueden realizar sus pedidos directamente, reduciendo errores y tiempos de espera.
2. **Privacidad de Datos de los Clientes:** QRest pone un énfasis especial en la seguridad y privacidad de los datos del cliente.
3. **Opciones de Recibo y Pago Individuales o Totales:** La solución ofrece flexibilidad en la facturación y el pago, adaptándose a las necesidades de diferentes grupos de clientes.
4. **Recomendaciones Personalizadas y Sugerencias del Restaurante:** Basadas en etiquetas y en pedidos anteriores, QRest proporciona recomendaciones útiles tanto para repetir pedidos como para probar nuevos platos, lo que mejora la experiencia del cliente y puede incrementar las ventas.
5. **Pagos en Caja con Confirmación de Pago:** Permite una mayor flexibilidad y comodidad en el proceso de pago, facilitando tanto los pagos individuales como los totales.
6. **Sincronización de Pedidos en Mesas Compartidas:** Esta característica asegura que todos los pedidos de una mesa estén perfectamente sincronizados, mejorando la eficiencia del servicio.
7. **Flexibilidad para Modificar la Carta Digital:** Ofrece a los restaurantes la capacidad de adaptar y actualizar su carta fácilmente, lo que es esencial para responder rápidamente a cambios en la oferta o la demanda.
8. **Seguridad en la API:** QRest se compromete a mantener altos estándares de seguridad en su API, protegiendo tanto los datos del restaurante como los del cliente.

**Aspectos de Ingeniería:**
1. **Arquitectura en Capas al Estilo Clean Architecture:** Esta estructura asegura que el sistema sea escalable, mantenible y fácil de modificar, lo que es crucial para adaptarse a las necesidades cambiantes del mercado y de los clientes.
2. **Tests de Integración:** Estos tests garantizan que todos los componentes del sistema funcionen juntos de manera efectiva y sin errores, lo que es vital para la fiabilidad del sistema.
3. **Estructura de Datos para Toda la Casuística de Restaurantes:** La capacidad de QRest para manejar una amplia gama de situaciones en diferentes tipos de restaurantes lo distingue de otras soluciones más limitadas.
4. **Transacciones Seguras de Casos de Uso:** Esto asegura que todas las operaciones realizadas en el sistema sean seguras y confiables.
5. **Metodología Ágil Basada en Sprints:** Permite una rápida adaptación y mejora del producto, asegurando que QRest pueda evolucionar según las necesidades del mercado y los usuarios.
6. **Uso de LocalStorage para Datos del Cliente:** Mejora la privacidad del cliente al almacenar datos localmente sin enviarlos al servidor, un enfoque único que refuerza la seguridad de los datos.

**Aspectos de deseables para la aplicación comercial (diseñados pero no implementados):**
1. **Generación Segura y Cómoda de Pedidos con QR:** Ofrecer un sistema de pedidos basado en QR que es tanto seguro como fácil de usar, mejorando la experiencia del cliente y la eficiencia del restaurante.
2. **Flujo Flexible de Gestión de Comandas:** El sistema permite a los restaurantes adaptar la gestión de comandas a sus flujos de trabajo específicos, proporcionando una mayor flexibilidad en comparación con sistemas más rígidos.
3. **Conexión con la Impresora de Tickets mediante Librería JS:** Esta característica asegura una integración fluida con los sistemas de impresión existentes, facilitando la transición a QRest.
4. **Búsquedas en la Carta con Filtros:** Permitir a los usuarios buscar fácilmente en la carta y aplicar filtros, mejorando la experiencia de navegación.
5. **Frontend con Elementos Complejos y Personalizables:** La interfaz de usuario avanzada de QRest es tanto visualmente atractiva como funcional, con elementos complejos para una mejor experiencia del usuario.
6. **Frontend para Modificar la Carta:** Ofrecer a los restaurantes la capacidad de modificar fácilmente su carta, proporcionando una solución dinámica y adaptable.

En resumen, QRest se diferencia claramente de sus competidores a través de su enfoque en la seguridad, la flexibilidad, la experiencia del usuario y la robustez técnica. Estos puntos fuertes posicionan a QRest no solo como una solución efectiva para los desafíos actuales de los restaurantes, sino también como un sistema preparado para adaptarse y evolucionar con las tendencias futuras en la industria de la restauración.


