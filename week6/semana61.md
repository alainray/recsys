## Sistemas de Recomendación - IIC3633 - Blog - Alain Raymond
### 2do Semestre 2018

#### Semana 6: Rendle, S. (2010). Factorization machines.

### Resumen

La lectura ofrece una descripción de un modelo alternativo para enfrentar problemas típicos de recomendación como la predicción de ratings o crear listas de recomendaciones. Sin embargo, no está acotado al mundo de los sistemas de recomendación.

El modelo se basa en mezclar las ideas de una regresión en múltiples órdenes de interacción entre variables junto con el enfoque de factorización de matrices.

La intuición es similar a generar una regresión pero en que los valores de los parámetros son el resultado de un producto punto entre vectores proyectados a un espacio latente de menor dimensionalidad.

### Ventajas

* Son más eficientes en rendimiento que una regresión lineal que tome en cuenta múltiples interacciones en parámetros.
  * Requiere mucho menos parámetros a estimar.
  * Se resuelve en tiempo proporcional a la dimensionalidad del input y la dimensionalidad de la factorización.
  * Es configurable el orden de interacciones a modelar y más encima, cada orden es ajustable via la cantidad de dimensiones latentes a trabajar.
* No pierden expresividad respecto a los otros modelos.
* Funcionan muy bien con datos *sparse* a diferencia de las SVMs.
  * No se menciona si funciona bien cuando los datos no son *sparse*.

### Comentarios

* Sólo se presenta una idea intuitiva de por qué funciona cambiar los coeficientes de regresión Beta por el resultado del producto punto de los vectores latentes.
  * Se menciona que variables que se comporten de forma parecida tenderán a mantener valores parecidos de producto punto con otras variables. De la misma manera, variables que no compartan nada entre ellas debieran tender a ser ortogonales entre ellas, llevando a su relación a 0.
* No queda muy claro si la manera en que presentan los datos de entrenamiento (one hot por cada valor de cada variable categórica) es algo que el modelo requiere o sólo una sugerencia.
  * Si es obligatorio y estamos trabajando con muchas variables categóricas o de muchos valores distintos (pensemos en usuarios, items, etc.), no me queda claro que tan factible es mantener esta representación en memoria para ingresarla al modelo.
* El método se hace cargo de explicar cómo trabajar con variables categóricas, pero no menciona como trabajar con aquellas de valores reales. ¿Se tienen que hacer bins con ellas? Y si no hay que hacer nada con ellas, ¿por qué?
  * Entendiendo mejor, al final lo que hace este modelo es modelar vectores para cada "variable" que hay. A diferencia de SVD donde teníamos una representación para cada usuario y otra para cada ítem, las MF son un poco más generales. 
    * Por ejemplo, que el usuario sea "Alain" es una variable, que sea "Juan" es otra. La edad es una variable (que toma valores reales) y que la película sea "Star Wars" es una "variable" que toma un valor 1 o 0.
    * Todo esto tiene que ver con que ponerle valores a las variables categóricas no tiene mucho sentido para predecir. Sin embargo, necesitas de alguna manera de transformarlas a números para poder operar con ellas.
