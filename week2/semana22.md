
## Sistemas de Recomendación - IIC3633 - Blog - Alain Raymond
### 2do Semestre 2018

#### Semana 2:  Collaborative Filtering for Implicit Feedback Datasets

### Discusión

La lectura introduce una modificación al algoritmo de Factorización de Matrices para que pueda trabajar con datos de feedback implícito. El problema de los datos de feedback implícito es que la matriz R de evaluaciones no existe directamente, ni necesariamente tiene la misma semántica que cuando hablamos de feedback explícito. ¿Por qué? Pues mientras con feedback explícito sabemos si un ítem gustó o no, el feedback implícito no es claro si algo no gusta o simplemente no fue visto, o fue visto no por gusto.

#### Características del Algoritmo

Para resolver esto se plantea que: 

* El rating será considerado como la proporción del tiempo que fue visto/consumido el ítem.
  * Esto nos permitirá modelar la Confianza en la predicción y la Preferencia del ítem.
* Se desglosará el rating es dos valores distintos:
  * La Confianza en la predicción.
    * Esto ataca el problema de la ambigûedad que se generará con los ratings de la matriz Anterior.
    * Se modela como una función lineal en el rating: 1 + alpha*r<sub>i,j</a>
    * Se puede modelar de otras maneras también.
  * La Preferencia por el ítem.
    * Esto será lo que queremos predecir.
    * En el modelo base, es modelada como una variable binaria, 1 si R<sub>i,j</sub> >= a un cierto umbral, 0 en otro caso.
    * Por supuesto, se puede modelar de formas más sofisticadas si es necesario.
* Se plantea el mismo problema de optimización que para el modelo de Factorización de Matrices, ligeramente modificado:

![Fórmula Problema de Optimización IF-MF](https://github.com/alainray/recsys/blob/master/week2/pics/IF-MF-Formula.png)
  * Nótese la inclusión del factor C<sub>i,j</sub>, lo discutiremos más adelante.
* La solución del problema de optimización no puede ser resuelta vía SGD dada la cantidad de variables.
  * A diferencia del caso de evaluaciones explícitas, la matriz de Ratings no puede ser considerada _sparse_.
  * Se utiliza un método parecido a ALS, en que se fija el valor de un set de variables - el vector de ítems o el de usuario - para simplificar el problema de optimización, para luego repetir el proceso con el otro set de variables.
  
#### Sobre la Confianza
* Por la manera en que está modelada la Confianza, el comportamiento que esperaríamos de los vectores de solución sería:
  * A mayor Confianza, mejor tiene que ser la predicción de preferencia pues su participación en la función de costo es más grande.
  * Con menor Confianza, la predicción de preferencia tenderá a ser peor, pues importan menos a la función de costo.
* Luego, la Confianza genera distorsiones deseadas en la solución de predicción.
  
#### Resultados relevantes
* Se genera un modelo extensible para aplicar las técnicas de Factorización de Matrices a datos de retroalimentación implícita.
  * No es difícil pensar cómo utilizar este modelo para representar compras de productos o para recomendar páginas web utilizando vistas.
* Se logra generar una forma de explicar las predicciones obtenidas de manera similar a como se hace para IB-CF, a través de la similaridad con otros ítems.
* El modelo -dado que está basado en el algoritmo de Factorización de Matrices- posee todas las posibilidades de extensión que este método posee:
  * Modelación de sesgos de usuario e item.
  * Modelación de variables de usuario (demográficas, etarias, etc.)
  * Etc...
* Además, el modelo es eficiente en computación.
 
