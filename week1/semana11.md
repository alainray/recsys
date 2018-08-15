## Sistemas de Recomendación - IIC3633 - Blog - Alain Raymond
### 2do Semestre 2018

#### Semana 1:  How not to sort by Average Rating, Evan Miller Blog

### Discusión

La lectura trata sobre tres métodos de rankear items sólo utilizando evaluaciones positivas y negativas. Los métodos listados son tres:
* Total positivos - Total Negativos
* Positivos/Total Evaluaciones
* El límite inferior de un intervalo de confianza del Wilson Score para una variable aleatoria Bernoulli.

Los dos primeros no son recomendados, pues tienen fallos evidentes: el primero falla pues considera equivalentes un producto que tiene 10 ratings positivos que uno que tiene 1000 ratings positivos y 990 negativos. El primer elemento parece seguro que será mejor que el segundo, pero para este algoritmo son iguales. En el segundo caso, podemos considerar mejor un producto que tiene un 100% de evaluaciones con solo una evaluación, versus uno que tiene 999 evaluaciones positivas de un total de 1000. Es evidente que hay mayor certeza que el segundo producto es mejor, pero esta métrica no incluye esa variable.

Para eso entra el tercer método que conjuga tanto la calidad de las evaluaciones como la cantidad. Si hay muy pocas, el intervalo de confianza crecerá y su límite inferior será menor que otros items que tienen más evaluaciones, aunque en rating promedio fuesen inferiores esos otros ítems. Cuando hay muchas evaluaciones, la comparación cada vez más tenderá a ser entre el rating promedio de cada uno de los ítems involucrados.

#### Ventajas

* Fácil de implementar y calcular.
* Funciona bien en dominios con muchas evaluaciones.
* Hace comparables ítems de pocas evaluaciones vs ítems con muchas evaluaciones.
* Aunque haya un usuario nuevo del que no sepamos nada, podemos hacer recomendaciones de ítems.

#### Problemas

* La primera limitación es que sólo aplica a escalas de evaluación de positivo/negativo. Luego, no distingue entre alguien que realmente amó el ítem versus alguien que le pareció razonablemente bueno.
  * Sería deseable poder incluir estas escalas de evaluación para que castigue más las evaluaciones muy malas y premiar las que son muy buenas.
  * Esto último sería similar a lo que se hizo en la ayudantía práctica donde se discretizó un score de 1 a 5 a positivos/negativos con un umbral de corte.
  * Aún así, sigue teniendo el problema de que no podemos evaluar de más de dos formas distintas los scores. Por ejemplo, ponderar cuadráticamente los negativos muy malos, linealmente los positivos/negativos normales y cuadráticamente los positivos muy buenos. 
* Segundo problema, en dominios en que efectivamente haya muy pocos ratings por ítem, el Wilson Score puede no ser tan apropiado pues el intervalo de confianza inferior tendrá un valor muy bajo. 
  * Ahí probablemente es mejor simplemente utilizar cantidad de evaluaciones positivas versus negativas, pues el mero hecho de tener más evaluaciones ya nos dice algo relevante del item en un dominio así.
*  El tercer problema -y que afecta a todos los métodos- es que no sabe qué hacer frente a un ítem nuevo. No puede decir nada al respecto.
