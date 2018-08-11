## Sistemas de Recomendación - IIC3633 - Blog - Alain Raymond
### 2do Semestre 2018

#### Semana 1:  Schafer, J. B., Frankowski, D., Herlocker, J., & Sen, S. (2007). Collaborative filtering recommender systems.

### Discusión
La lectura trata sobre los métodos de Filtrado Colaborativo y describe e.

En particular, se discute el uso de un algoritmo basado en los ratings de usuarios para predecir el rating de un cierto item para un cierto usuario.

Para esto, se utiliza una métrica de similaridad entre usuarios, que pondera los ratings de los usuarios que sí han evaluado el ítem y con eso se logra la predicción.

Sin embargo, este método adolece del problema que si un usuario no ha evaluado items en común con usuarios que sí han evaluado el ítem a predecir, entonces no es posible generar la métrica de similaridad.

### Propuesta de solución
Para mitigar este problema, se propone un método para predecir las similaridades desconocidas. 

Para esto utilizaremos el algoritmo de UB-CF base pero el item al que lo aplicaremos serán las similaridades desconocidas. Luego, la idea es predecir para un usuario U<sub>1</sub> que no posee una similaridad con otro usuario U<sub>2</sub>, basándose en las similaridades de los usuarios que sí conocen a U<sub>1</sub> y U<sub>2</sub>.

A medida que vamos obteniendo nuevas similaridades podemos volver a correr el algoritmo hasta que ya no hayan más similaridades desconocidas o no haya cambios en la matriz de similaridades.

#### Pseudocódigo
El pseudocódigo para el algoritmo sería:

1. Inicializar matriz de similaridades S.
2. Crear matriz de trabajo S' con los mismos valores de S.
3. Recorrer cada elemento S'<sub>i,j</sub> del triángulo superior de S'.
   - Si S'<sub>i,j</sub> tiene Similaridad distinta de 0, pasar al siguiente elemento.
   - Si S'<sub>i,j</sub> tiene valor 0, entonces calcular nueva Similaridad para elemento S'<sub>i,j</sub> y asignársela al elemento S<sub>i,j</sub>.
     - La fórmula para calcular la Similaridad es: <br>
![Fórmula Similaridad](https://github.com/alainray/recsys/blob/master/similarity_semana1.PNG)
     - Donde R'<sub>i</sub> y C'<sub>j</sub> son la i-ésima fila y j-ésima columna respectivamente de S'.
     - Utilizamos el producto punto pues representa exactamente la suma ponderada expresada en el algoritmo original.
     - Restamos 1 del denominador para eliminar el peso de la diagonal.
4. Al finalizar, en caso de haberse realizado cambios en las similaridades en esta corrida:
   1. Copiar valores de S en S'.
   2. Volver a 3.
5. Fin.


### Ejemplo de implementación
1. Para la siguiente matriz de entrada S:

```
 [1.000 0.500 0.000 0.000 0.000 0.300]
 [0.500 1.000 0.400 0.600 -0.300 -0.100]
 [0.000 0.400 1.000 -0.300 0.000 0.400]
 [0.000 0.600 0.000 1.000 0.200 0.000]
 [0.000 0.000 0.000 0.200 1.000 0.000]
 [0.300 -0.100 0.400 0.000 0.000 1.000]
```
* Si representamos las relaciones de similaridad existentes en esta matriz como un grafo, el resultado sería:
 
 ![Grafo Similaridad 1a iteración](https://github.com/alainray/recsys/blob/master/similarity_graph.PNG)

2. Corremos el algoritmo. El estado de S después de 1 iteración es:
```
 [1.000 0.500 0.640 0.375 0.000 0.300]
 [0.500 1.000 0.400 0.600 0.600 -0.100]
 [0.640 0.400 1.000 0.300 0.000 0.400]
 [0.375 0.600 0.300 1.000 0.200 -0.300]
 [0.000 0.600 0.000 0.200 1.000 0.050]
 [0.300 -0.100 0.400 -0.300 0.050 1.000]
```
 * El grafo de similaridad de S ahora sería:
 
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
 * Finalmente, llegamos a la siguiente configuración:
 
 ![Grafo Similaridad 1a iteración](https://github.com/alainray/recsys/blob/master/similarity_graph_it2.PNG)
 
Podemos ver que hemos completado S con todas las similaridades desconocidas, extrapoladas a partir de las similaridades conocidas.

A continuación, un link a una [implementación en Python del algoritmo propuesto](https://github.com/alainray/recsys/blob/master/semana1_similarity.py).

### Sobre el algoritmo
#### Características

* El algoritmo es independiente del método utilizado para calcular las similaridades.
* El uso del valor 0 para representar los valores desconocidos es afortunado, pues permite hacer directamente el producto punto entre 
filas y columnas, al eliminar los términos asociados a la diagonal.
* El algoritmo no garantiza poblar completamente la matriz de similaridades. Sin embargo, sí garantiza que las secciones conexas del grafo de similaridades se conviertan en cliques.

#### Supuestos

* Se asume que es razonable estimar la similaridad entre un usuario U<sub>1</sub> y U<sub>2</sub> basándose en las similaridades de usuarios que poseen similaridad con ambos.
   * De cierta manera, se asume que las similaridades son ratings de un usuario a otro en una escala de -1 a 1.
#### Problemas
* Debe recorrer la mitad de la matriz por cada iteración, lo que para las matrices de tamaño grande puede ser prohibitivo. Aunque este problema ya se encuentra presente en el método original de UB-CF.
  * Se puede arreglar para que guarde en memoria un arreglo con las posiciones que requieren cálculo. Esto permitiría recorrer la matriz una sola vez.
* Se utiliza una copia de la matriz original para trabajar, lo que puede ser prohibitivo en dimensiones grandes.
* Puede generar similaridades fuera del rango de [-1,1] cuando se trabaja con ponderadores tanto negativos y positivos.
  * Tres posibles respuestas:
    * No hacer nada.
    * Forzar los valores a estar en el rango [-1,1].
    * Considerar la similaridad como desconocida. _Opción utilizada en esta implementación_.
  * Sin embargo, es altamente probable que los vecinos que ocupemos para calcular las similaridades sean aquellos con quienes tengamos correlación positiva.
    * En ese caso, el problema desaparece.
    * Por ahora, el algoritmo está implementado considerando todos los vecinos.
 
