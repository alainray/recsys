## Sistemas de Recomendación - IIC3633 - Blog - Alain Raymond
### 2do Semestre 2018

#### Semana 1:  Schafer, J. B., Frankowski, D., Herlocker, J., & Sen, S. (2007). Collaborative filtering recommender systems.

La lectura trata sobre los métodos de Filtrado Colaborativo y describe e.

En particular, se discute el uso de un algoritmo basado en los ratings de usuarios para predecir el rating de un cierto item para un cierto usuario.

Para esto, se utiliza una métrica de similaridad entre usuarios, que pondera los ratings de los usuarios que sí han evaluado el ítem y con eso se logra la predicción.

Sin embargo, este método adolece del problema que si un usuario no ha evaluado items en común con usuarios que sí han evaluado el ítem a predecir, entonces no es posible generar la métrica de similaridad.

Para mitigar este problema, propongo un método para predecir las similaridades desconocidas. Para esto simplemente asumiremos que las similaridades desconocidas son el equivalente a un item cuyo rating debe ser predecido y ocuparemos el mismo algoritmo de predicción de evaluaciones descrito en la lectura.

A medida que vamos obteniendo nuevas similaridades podemos volver a correr el algoritmo hasta que ya no hayan más similaridades desconocidas o no haya cambios en la matriz de similaridades.


El pseudocódigo para el algoritmo sería:

1. Inicializar matriz de similaridades S.
2. Crear matriz de trabajo S' con los mismos valores de S.
3. Recorrer cada elemento S'<sub>i,j</sub> del triángulo superior de S'.
   - Si S'<sub>i,j</sub> tiene Similaridad distinta de 0, pasar al siguiente elemento.
   - Si S'<sub>i,j</sub> tiene valor 0, entonces calcular nueva Similaridad para elemento S'<sub>i,j</sub> y asignársela al elemento S<sub>i,j</sub>.
     - La fórmula para calcular la Similaridad es: <br>
![Fórmula Similaridad](https://github.com/alainray/recsys/blob/master/similarity_semana1.PNG)
     - Donde R'<sub>i</sub> y C'<sub>j</sub> son la i-ésima fila y j-ésima columna respectivamente de S'.
     - Restamos 1 del denominador para eliminar el peso de la diagonal.
4. Al finalizar, en caso de haberse realizado cambios en las similaridades en esta corrida:
   1. Copiar valores de S en S'.
   2. Volver a 3.
5. Fin.

##Ejemplo de implementación
1. Para la siguiente matriz de entrada S:

```
 [1.000 0.500 0.000 0.000 0.000 0.300]
 [0.500 1.000 0.400 0.600 -0.300 -0.100]
 [0.000 0.400 1.000 -0.300 0.000 0.400]
 [0.000 0.600 0.000 1.000 0.200 0.000]
 [0.000 0.000 0.000 0.200 1.000 0.000]
 [0.300 -0.100 0.400 0.000 0.000 1.000]
```
Cuyo grafo de similaridades sería:
 
 ![Grafo Similaridad 1a iteración](https://github.com/alainray/recsys/blob/master/similarity_graph.PNG)

2. S después de 1 iteración:
```
 [1.000 0.500 0.640 0.375 0.000 0.300]
 [0.500 1.000 0.400 0.600 0.600 -0.100]
 [0.640 0.400 1.000 0.300 0.000 0.400]
 [0.375 0.600 0.300 1.000 0.200 -0.300]
 [0.000 0.600 0.000 0.200 1.000 0.050]
 [0.300 -0.100 0.400 -0.300 0.050 1.000]
```
 El grafo de similaridad de S ahora sería:
 
 ![Grafo Similaridad 1a iteración](https://github.com/alainray/recsys/blob/master/similarity_graph_it1.PNG)
 
3. S después de 2 iteraciones:
```
[[1.000 0.500 0.640 0.375 0.459 0.300]
 [0.500 1.000 0.400 0.600 0.600 -0.100]
 [0.640 0.400 1.000 0.300 0.376 0.400]
 [0.375 0.600 0.300 1.000 0.200 -0.300]
 [0.459 0.600 0.376 0.200 1.000 0.050]
 [0.300 -0.100 0.400 -0.300 0.050 1.000]]
```
 El grafo de similaridad de S ahora sería:
 
 ![Grafo Similaridad 1a iteración](https://github.com/alainray/recsys/blob/master/similarity_graph_it2.PNG)
 
Podemos ver que hemos completado S con todas las similaridades desconocidas, extrapoladas a partir de las similaridades conocidas.

A continuación, el link a una [implementación en Python del algoritmo propuesto](https://github.com/alainray/recsys/blob/master/semana1_similarity.py).
