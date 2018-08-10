## Sistemas de Recomendación - IIC3633 - Blog - Alain Raymond
### 2do Semestre 2018

#### Semana 1:  Schafer, J. B., Frankowski, D., Herlocker, J., & Sen, S. (2007). Collaborative filtering recommender systems.

La lectura trata sobre los métodos de Filtrado Colaborativo y describe e.

En particular, se discute el uso de un algoritmo basado en los ratings de usuarios para predecir el rating de un cierto item para un cierto usuario.

Para esto, se utiliza una métrica de similaridad entre usuarios, que pondera los ratings de los usuarios que sí han evaluado el ítem y con eso se logra la predicción.

Sin embargo, este método adolece del problema que si un usuario no ha evaluado items en común con usuarios que sí han evaluado el ítem a predecir, entonces no es posible generar la métrica de similaridad.

Para mitigar este problema, propongo un método para predecir las similaridades desconocidas. Para esto simplemente asumiremos que las similaridades desconocidas son el equivalente a un item cuyo rating debe ser predecido y ocuparemos el mismo algoritmo de predicción de evaluaciones descrito en la lectura.

A medida que vamos obteniendo nuevas similaridades podemos volver a correr el algoritmo hasta que ya no hayan más similaridades desconocidas o no haya cambios en la matriz de similaridades.