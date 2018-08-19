
## Sistemas de Recomendación - IIC3633 - Blog - Alain Raymond
### 2do Semestre 2018

#### Semana 2: Koren, Y., Bell, R., & Volinsky, C. (2009). Matrix factorization techniques for recommender systems

### Discusión
La lectura presenta el método de predicción de ratings de factorización de matrices, sus ventajas, debilidades y extensiones posibles para hacerlo más versátil.

#### SVD

El método de factorización de matrices consiste en utilizar el método de **SVD** (_Singular Value Decomposition_) para resolver el problema de predicción. A diferencia de los métodos de UB-CF o IB-CF, SVD de cierta manera ocupa la información de ambos al mismo tiempo.

La idea es que la matriz R de Ratings puede ser descompuesta en tres matrices U, S y V. La matriz U y V representarían proyecciones de los usuarios e items en un espacio distinto en que ciertas características latentes - pero desconocidas- de R, explicarían los ratings de la matriz R. 

Luego, si es posible obtener las matrices U, S y V, la predicción consistirá simplemente en ver la casilla R<sub>i,j</sub> después de multiplicarlas.

La primera bondad del método es que la cantidad de factores latentes total es similar en cantidad al tamaño de filas y columnas. En los casos que nos interesan, éstos puedes ser de cientos de miles o millones. Sin embargo, es poco probable que haya tal cantidad de factores relevantes a la hora de considerar el rating. Luego, el método consiste en generar una **reducción de la dimensionalidad** en los factores latentes llevándola al nivel de decenas o centenas. Luego, los vectores son proyectados a esta espacio de menor dimensionalidad y la predicción se convierte en la multiplicación de estas nuevas matrices U, S y V de menor dimensionalidad. 

Como estamos reduciendo la dimensionalidad, la reconstrucción de la matriz original no es perfecta. Sin embargo, esto último no es necesariamente malo: al hacer esto estamos quedándonos sólo con los factores más relevantes, luego tenderá a desaparecer el ruido de las predicciones asociado a conjuntos de factores latentes menos relevantes. Además, se reforzará la importancia de los factores latentes de más peso, con lo que obtenemos predicciones más limpias.

Esto resuelve la predicción, sin embargo, adolece de ciertos problemas:

* Funciona mucho mejor cuando los valores desconocidos son pocos. Sin embargo, este no suele ser el caso y las matrices son _sparse_.
* El cálculo directo de la descomposición SVD es muy costoso.

#### Mejorando SVD

Se presenta un algoritmo mejor, que utiliza la noción de que la predicción de ratings es simplemente el producto punto entre un vector representativo del usuario y otro del ítem y la reducción de dimensionalidad. 

Se transforma el problema de factorizar matrices a un problema de optimización, utilizando solamente los datos conocidos de ratings. Se trata de minimizar la diferencia entre los ratings y el producto punto del vector representativo del usuario y del vector representativo del item. Además se le agregan ciertas términos para regularización, pero esto es menos importante.

Esto es mucho más rápido que factorizar matrices y la predicción se transforma en multiplicar los vectores representativos que son solución del problema de optimización entre sí.

Luego se habla de cómo extender el modelo para que soporte:

* Sesgos de usuario o ítem
* Confianza en la predicción.
* Sesgos temporales.
* Atributos del usuario (Demografía, género, etc.)
* Más...

#### Ventajas:

* Rápido, simple de implementar.
* Fácilmente extensible a nivel de modelación.
  * Esto es lo que más me gusta de este algoritmo, pues permite desglosar la predicción de un rating de cuanta manera a uno se le pueda ocurrir.
* Más preciso que métodos de Filtrado Colaborativo basado en Usuarios o Ítems.

#### Desventajas
* Difícil explicar cuáles son los criterios o factores latentes relevantes.
  * Esto es probablemente lo peor del modelo, pues si bien me permite predecir fidedignamente evaluaciones, se vuelve difícil tomar decisiones proactivamente para mejorar mi oferta de productos, pues no es claro que se debe cambiar realmente.
  * Sin embargo, por el poder de modelación que ofrece el método, es posible reducir esta incertidumbre al poder entender cómo cambian los ratings respecto a variables modeladas no directamente asociadas a los factores latentes.
* No resuelve el problema del nuevo usuario o nuevo ítem.
  * Al menos no con esta implementación.
