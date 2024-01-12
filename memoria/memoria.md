# QRest

## Resumen

En el contexto del crecimiento global del sector de la restauración, los restaurantes enfrentan desafíos significativos en la modernización de sus sistemas de gestión, especialmente en la gestión de comandas. Las soluciones existentes son a menudo costosas y poco accesibles para pequeñas empresas. El proyecto QRest aborda este desafío mediante el desarrollo de una solución integral y accesible para la gestión de comandas en restaurantes.

QRest es un sistema basado en web que ofrece una gama de funcionalidades clave para la gestión eficiente de restaurantes. Entre estas se incluyen la gestión de comandas a través de códigos QR, pagos online, digitalización de menús, pedidos interactivos, y sugerencias basadas en pedidos anteriores. Esta solución integral no solo mejora la eficiencia operativa, sino que también reduce significativamente los costos y barreras de entrada para restaurantes de diversos tamaños.

El impacto de QRest es multifacético, ofreciendo una experiencia mejorada tanto para los clientes como para los propietarios de restaurantes. Los clientes disfrutan de una experiencia de pedido más fluida y personalizada, mientras que los restaurantes se benefician de una gestión más eficiente y una reducción en los costos operativos. Con QRest, los restaurantes pueden implementar un sistema de gestión de comandas moderno y eficiente sin la necesidad de una gran inversión inicial.

Palabras clave: Gestión de restaurantes, QRest, pedidos en línea, eficiencia operativa, automatización.

## Introducción

En este capítulo se exponen las motivaciones detrás de la realización de este proyecto, así como los objetivos que se buscan alcanzar mediante su ejecución. Además, se detalla la estructura del presente documento, que conforma la memoria del Trabajo de Fin de Grado (TFG), y se listan los entregables asociados a este trabajo.

### Problemas del sector

El sector de la restauración en España y a nivel mundial ha experimentado un notable crecimiento en las últimas décadas. Sin embargo, este crecimiento no se ha visto acompañado de una modernización adecuada en la gestión operativa de los restaurantes, especialmente para los establecimientos pequeños y medianos. La mayoría de estos restaurantes aún dependen de métodos anticuados y manuales para la gestión de comandas, enfrentando limitaciones significativas en su eficiencia operativa y capacidad para competir en un mercado cada vez más digitalizado.

Estos desafíos incluyen sistemas de toma de pedido obsoletos, a menudo basados en papel o dependientes de costosos sistemas PDA con hardware especializado. La digitalización de las cartas es mínima, y su actualización y personalización resultan engorrosas y poco flexibles. Además, los restaurantes enfrentan ineficiencias en la gestión del tiempo de espera de los clientes, desde la toma del pedido hasta el pago de la cuenta. La falta de un registro informatizado de los pedidos impide realizar análisis y estadísticas que podrían mejorar la experiencia del cliente y la gestión del restaurante.

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

Finalmente, la variante de QR estático con contraseña, utilizada por ejemplos como Sushi Son, intenta abordar los problemas de seguridad, pero introduce una nueva capa de complejidad y potencial incomodidad tanto para los clientes, que deben obtener y recordar una contraseña, como para el personal, que debe comunicarla y gestionar su uso.

En resumen, aunque cada una de estas soluciones ofrece ventajas en ciertos aspectos, también presentan una serie de inconvenientes que limitan su eficacia y aceptación general en la industria de la restauración. Estos problemas son especialmente pronunciados en restaurantes más pequeños y establecimientos independientes, donde los costos, la complejidad y las limitaciones operativas pueden hacer que la implementación de estos sistemas sea impracticable.

### Motivación

La motivación para el desarrollo del proyecto QRest tiene sus raíces en experiencias personales y en un interés técnico profundo. La idea surgió tras una experiencia en un restaurante llamado Yasaka. Allí, me encontré con un sistema de pedidos basado web y QRs generados para cada pedido, diseñado específicamente para ese establecimiento, pero con notables deficiencias: una interfaz de usuario poco atractiva, falta de sincronización de los pedidos y la ausencia de una opción para realizar pagos separados. Este encuentro me llevó a la reflexión y eventual decisión de explorar la posibilidad de desarrollar una solución aplicable a una gama más amplia de restaurantes. Desde enero de 2023, comencé a investigar las soluciones ya existentes en el mercado, notando una evolución constante y el surgimiento de nuevas opciones durante el año.

En el plano personal, mi interés en el desarrollo web y el deseo de enfrentar un reto significativo en este ámbito fueron factores decisivos. La experiencia como cliente de restaurantes me proporcionó una perspectiva única sobre las necesidades y desafíos en este sector. La idea de llevar QRest más allá de un proyecto académico y convertirlo en un negocio viable también jugó un papel importante en mi decisión. Además, el proyecto representaba una oportunidad excepcional para aplicar los conocimientos adquiridos en la carrera de Ingeniería del Software en un contexto práctico y realista.

Desde un enfoque técnico, la reciente aparición de soluciones de gestión para restaurantes representó una oportunidad para la investigación y la innovación. La posibilidad de desarrollar una aplicación que pudiera escalar a diferentes tipos de restaurantes, especialmente aquellos de menor tamaño o recién inaugurados, era especialmente atractiva. El proyecto implicaba la integración de múltiples aspectos técnicos: desde transacciones en bases de datos y sincronización en tiempo real mediante websockets, hasta el uso de bases de datos NoSQL y la construcción de modelos de datos complejos capaces de reflejar la variedad de situaciones en un restaurante real. Además, se puso especial énfasis en la privacidad y seguridad de los datos, empleando técnicas como el almacenamiento local de datos del usuario.

A nivel de ingeniería del software, enfrentar el reto de desarrollar una aplicación en un área emergente con pocas referencias existentes fue una tarea significativa. Esto implicó la adopción de metodologías de desarrollo de software adecuadas, la definición de requisitos claros, la elaboración de casos de uso, la implementación de pruebas, y la aplicación de APIs, programación orientada a objetos en Python y JavaScript, y el uso de frameworks de desarrollo web. Además, la estructuración y refactorización de un proyecto de esta magnitud fueron componentes clave para su éxito.

En resumen, QRest es el resultado de una combinación de motivaciones personales y técnicas, representando tanto una solución innovadora para los desafíos en la industria de la restauración como un proyecto personal de crecimiento y aplicación práctica de habilidades y conocimientos en ingeniería del software.

### Objetivos

En el desarrollo del proyecto QRest, he establecido una serie de objetivos divididos en tres categorías clave: personales, profesionales y del proyecto.

#### Objetivos Personales

Los objetivos personales se centran en mi crecimiento y satisfacción a lo largo de este proyecto. Incluyen:

- Realizar un Trabajo de Fin de Grado que despierte un verdadero entusiasmo y compromiso personal.
- Crear una base para el desarrollo de un negocio a partir del proyecto QRest.
- Fomentar mi desarrollo personal y profesional a través de este desafío.
- Adquirir conocimientos profundos en desarrollo web.
- Desarrollar una aplicación full-stack que no solo cumpla con los requisitos del TFG, sino que también enriquezca mi portafolio profesional.

#### Objetivos Profesionales

En el ámbito profesional, los objetivos se alinean con el desarrollo de habilidades y conocimientos específicos en áreas técnicas clave:

- Mejorar mis habilidades en frontend, especialmente en JavaScript y CSS.
- Aprender y aplicar técnicas de sincronización en tiempo real usando Websockets.
- Profundizar mi entendimiento y habilidad en el uso de MongoDB.
- Desarrollar una comprensión integral de las transacciones en bases de datos.
- Explorar y aplicar conceptos de arquitectura de software específicos para aplicaciones web.
- Diseñar y desarrollar APIs funcionales y eficientes.
- Reforzar mi conocimiento en programación orientada a objetos, tanto en Python como en JavaScript.
- Implementar y seguir metodologías ágiles en el contexto de un proyecto de gran escala.

#### Objetivos del Proyecto

Los objetivos del proyecto QRest se centran en abordar y resolver los problemas identificados en las soluciones existentes en el mercado:

- Asegurar una sincronización efectiva de los pedidos entre clientes.
- Facilitar los pagos separados para mejorar la experiencia del usuario.
- Crear una carta digital que sea flexible, dinámica y fácil de actualizar.
- Implementar un sistema de sugerencias basado en preferencias y pedidos anteriores de los clientes.
- Garantizar la privacidad y seguridad de los datos de los clientes.
- Desarrollar un modelo de datos que pueda manejar toda la casuística de un restaurante real.
- Ofrecer una gestión de comandas eficiente y flexible para el personal del restaurante.
- Proponer soluciones innovadoras a los problemas de los sistemas basados en QR estáticos y con contraseña.
- Minimizar la necesidad de hardware costoso o especializado por parte de los restaurantes.

Estos objetivos reflejan un compromiso con el desarrollo de una solución integral que aborde las necesidades tanto de los clientes como de los restaurantes, utilizando los conocimientos y habilidades adquiridos en el campo del desarrollo de software.
