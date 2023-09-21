# Data Modeling MongoDB

Fuente: [Vídeo](https://www.youtube.com/watch?v=FSWDz-DHrrk&list=PL4RCxklHWZ9t2KI3XiRLbqsMKB_iXxScv&index=23&t=258s)

## Ideas clave

La información debe almacenarse conjuntamente **si y solo si** se accede conjuntamente.

El alamacenamiento basado en documentos como *json* permite guardar documentos dentro de documentos, y así que la información relacionada se almacene junta y no en documentos separados.  

## MongoDB

### Origen

Cuando comenzaron los discos duros, el coste de alamacenamiento era extremadamente caro, por lo que la normalización de los datos era la mejor opción para evitar duplicidades. Y es en eso en lo que se basan las tablas SQL. 

En cambio hoy día ya no tenemos esa limitación, el almacenamiento es muy barato, así que no tiene sentido seguir usando tablas SQL que almacenen cada campo de forma separada. Lo lógico es almacenar junto lo que se accede de forma conjunta. Así surge mongoDB remplazando las tablas SQL a documentos. 

Las bases de datos SQL están hechas para ahorrar espacio, las bases de datos mongoDB para ahorrar tiempo al desarrollador.

### Tipo

MongoDB no usa *json* para almacenar documentos, sino *bson*, que es una representación en binario de json con información añadida, como el tipo. Así pues permite diferenciar entre por ejemplo, *String* y *Date*. 

### Consultas

En mongoDB no hay consultas SQL sino consultas *mql*. No funcionan de igual forma, sino que sol operaciones que siguen una estructura de pipeline.

### Diferencias

Las diferencias entre las bases de datos relacionales y las basadas en documentos son las siguientes:

| Relacional | Documento  |
| ---------- | ---------- |
| Tabla      | Colección  |
| Fila       | Documento  |
| Columna    | Campo      |

### Modificaciones

Al hacer modificaciones en la base de datos no hace falta migrar esta. Lo mejor para estos casos es añadir un campo versión a la base de datos, de forma que pueda haber conjuntamente datos antiguos y nuevos. 

### Validación

Dado que las bases de datos de documentos como mongoDB no siguen un esquema, podrían insertarse datos que no queremos, para ello se pueden especificar esquemas de validación. 

La validación tiene un *validationLevel* que indica cuándo se activa y un *validationAction* que indica qué se hace. Se puede lanzar una advertencia o bien una excepción.  

## Modelado

Para modelar los datos de la aplicación debemos preguntarnos:

1. ¿Qué hace mi aplicación?
2. ¿Cómo se ven los datos?
3. ¿Con qué herramienta voy a desarrollar la aplicación?
4. ¿Cómo puedo aplicar patrones para el modelado de datos?

### Empotrar vs. referenciar

| Característica | Empotrar       | Referenciar         |
| -------------- | -------------- | ------------------- |
| Duplicidad     | Es posible     | No hay              |
| Consultas      | Una            | Varias              |
| CRUD           | Una operación  | Varias operaciones  |
| Documento      | Largos         | Cortos              |
| Lectura        | Rápida         | Lenta               |
| Escritura      | Lenta          | Rápida              |

Así pues los datos empotrados se usan para datos accedidos conjuntamente, mientras que las referencias cuando esto no es frecuente. 

En general es preferible usar datos empotrados. 

## Patrones

Los patrones se pueden consultar en la [web](https://www.mongodb.com/blog/post/building-with-patterns-a-summary).

## Antipatrones

Se pueden encontrar en la [web](https://www.mongodb.com/developer/products/mongodb/schema-design-anti-pattern-summary/).

Los principales antipatrones son:

- Usar arrays muy largos sin tamaño máximo -> Referenciar si supera cierto número de elementos.
- Tener muchas colecciones -> Probablemente puedas empotrar muchas de estas.
- Índices innecesarios -> Quitar el índice.
- Documentos muy largos -> Referenciar los campos que se accedan por separado.
- Separar datos que se acceden conjutamente -> empotrar en un solo socumento. 

### Reglas

Se pueden consultar las reglas en la [web](https://www.mongodb.com/developer/products/mongodb/mongodb-schema-design-best-practices/).

- Usa datos empotrados a no ser que haya una buena razón para no hacerlo.
- Si tenemos un producto y sus partes, y sus partes se pueden acceder independientemente del producto, es mejor usar referencia en vez de empotrarlos en el producto 
- Evita diseños que oblique a usar *joins* para una misma consulta.
- Si en una relación uno a mucho, los muchos son demasiados, mejor usar usar una referencia de los muchos al uno que un largo array de ids o peor aún, empotrarlos.
- La mejor estructura es la que mejor se adapte cómo tu aplicación represente los datos. 

### Relaciones

| Cardinalidad     | Preferencia  |
| ---------------- | ------------ |
| Uno a Uno        | Clave-valor  |
| Uno a pocos      | Empotrado    |
| Uno a muchos     | Empotrado    |
| Uno a millones   | Referencia   |
| Muchos a muchos  | Referencia   |

### Consejero de esquema

MongoDB Atlas tiene una herramienta llamada *Schema Advisor* que en función de las consultas que recibe la base de datos, recomienda el esquema de datos que mejor se adapte a tus consultas. Se enuentra en el apartado de *Performance Advisor*.
