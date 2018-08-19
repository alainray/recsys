
## Sistemas de Recomendación - IIC3633 - Blog - Alain Raymond
### 2do Semestre 2018

#### Semana 2:  Collaborative Filtering for Implicit Feedback Datasets

### Discusión

La lectura introduce una modificación al algoritmo de Factorización de Matrices para que pueda trabajar con datos de feedback implícito. Para esto se plantean dos ideas importantes:

* El rating será considerado como la proporción del tiempo que fue visto/consumido el ítem.
* Se desglosará el rating es dos valores distintos:
  * La Confianza en la predicción.
  * La preferencia por el ítem.

#### Características

* La solución del problema de optimización no puede ser resuelta vía SGD dada la cantidad de variables.
  * A diferencia del caso de evaluaciones explícitas, la matriz de Ratings no puede ser considerada _sparse_.
  * Se utiliza un método parecido a ALS, en que se fija el valor de un set de variables - el vector de ítems o el de usuario - para simplificar el problema de optimización, para luego repetir el proceso con el otro set de variables.
  
#### Sobre la Confianza
* Por la manera en que está modelada la confianza, el comportamiento que esperaríamos de los vectores de solución sería:
  * A mayor Confianza, mejor tiene que ser la predicción de preferencia pues su participación en la función de costo es más grande.
  * Con menor Confianza, la predicción de preferencia tenderá a ser peor.
  
#### Resultados relevantes
* Se genera un modelo extensible para aplicar las técnicas de Factorización de Matrices a datos de retroalimentación implícita.
  * No es difícil pensar cómo utilizar este modelo para representar compras de productos o para recomendar páginas web utilizando vistas.
* Se logra generar una forma de explicar las predicciones obtenidas de manera similar a como se hace para IB-CF, a través de la similaridad con otros ítems.
* El modelo -dado que está basado en el algoritmo de Factorización de Matrices- posee todas las posibilidades de extensión que este método posee:
  * Modelación de sesgos de usuario e item.
  * Modelación de variables de usuario (demográficas, etarias, etc.)
  * Etc...
* Además, el modelo es eficiente en computación.
 
