## Sistemas de Recomendación - IIC3633 - Blog - Alain Raymond
### 2do Semestre 2018

#### Semana 1:  How not to sort by Average Rating, Evan Miller Blog

### Discusión

La lectura trata sobre tres métodos de rankear items sólo utilizando evaluaciones positivas y negativas. Los métodos listados son tres:
* Total positivos - Total Negativos
* Positivos/Total Evaluaciones
* El límite inferior de un intervalo de confianza del Wilson Score para una variable aleatoria Bernoulli.

Los dos primeros no son recomendados, pues tienen fallos evidentes: el primero falla pues considera equivalentes un producto que tiene 100 ratings positivos que uno que tiene 1000 ratings positivos y 990 negativos. El primer elemento parece seguro que será mejor que el segundo, pero para este algoritmo son iguales. En el segundo caso, podemos considerar mejor un producto que tiene un 100% de evaluaciones con solo una evaluación, versus uno que tiene 999 evaluaciones positivas de un total de 1000. Es evidente que hay mayor certeza que el segundo producto es mejor, pero esta métrica no incluye esa variable.

Para eso entra el tercer método que conjuga tanto la calidad de las evaluaciones como la cantidad. Si hay muy pocas, el intervalo de confianza crecerá y su límite inferior será menor que otros items que tienen más evaluaciones, aunque en rating promedio fuesen inferiores esos otros ítems. Cuando hay muchas evaluaciones cada vez más la comparación tenderá a ser entre el rating promedio de cada uno de los ítems involucrados.

* Problemas
En qué dominios funciona bien el tercer método? Cuando haya gran cantidad de 
