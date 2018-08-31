## Sistemas de Recomendación - IIC3633 - Blog - Alain Raymond
### 2do Semestre 2018

#### Semana 4:  Pazzani, M. J., & Billsus, D. (2007). Content-based recommendation systems

### Resumen

La lectura presenta los elementos a modelar para emprender la tarea de implementar un sistema de recomendación basado en contenido. Primero hay que tener una representación del ítem, sea númericamente, features, clases, etc. Luego, de una u otra manera ocupamos la información de la relación entre el usuario y los ítems. Con esto construimos un modelo del usuario o aprovechamos esa historia para filtrar o sugerir recomendaciones, por ejemplo, no recomendar algo ya consumido.

Después se discuten distintos métodos para aprender modelos de usuario como. 
  * Árboles de Decisión e Inducción de Reglas
  * Métodos de Vecinos Cercanos
  * Retroalimentación de Relevancia y el algoritmo de Rocchio
  * Clasificadores lineales (por ejemplo, SVM)
  * Modelos Probabilísticos y Naive Bayes

Finalmente se habla de las limitaciones y posibles extensiones de estos sistemas.

#### Comentarios
* Hay un enfoque excesivo en texto en el artículo. Para actualizarlo, tendría que pensarse en considerar imágenes, video y sonido como parte del contenido.
* La metodología subyacente sin embargo, sería más o menos la misma: generar features a partir de estos nuevos medios, calcular distancias entre ítems.
  * Sin embargo, ¿es trivial la generación de features o modelación de estos tipos de entrada? ¿Cómo se manejan los problemas de temporalidad, contexto y el aumento significativo en recursos necesarios para ejecutar estos algoritmos? El espacio de las palabras es probablemente más fácil de manejar que el de contenido multimedia.
   * Probablemente, el uso de algoritmos basados en contenido de manera on-line con contenido multimedia es un desafío importante.
* Este tipo de algoritmos es malo para detectar atributos de los ítems que son fáciles de detectar para los usuarios. 
  * El pareo con algoritmos de filtrado colaborativo se vuelve relevante.
  * Quizás con la introducción de las redes profundas, este problema se pueda mitigar. Por ejemplo, detección de sentimientos que en su momento solo seres humanos podían hacer de forma decente.
* La modelación es muy dependiente del ítem, a diferencia de los métodos de filtrado colaborativo donde uno se abstrae de eso.
  * Más difícil transferir aprendizaje de un dominio a otro. Se debe hacer con más cuidado.
* Este tipo de algoritmo parece tener más sentido cuando no es posible aplicar filtrado colaborativo.
  * Por ejemplo, si el sparsity es demasiado grande y no hay muchos vínculos entre distintos usuarios.
* Naive Bayes me gusta porque permite enfrentar problemas de polisemia.
* En esta época sería apropiado incluir las redes neuronales profundas como algoritmo candidato para modelar usuarios o el contenido genéricamente.
  * Aunque tienen gran costo computacional, éste es de preprocesamiento. Luego el modelo aprendido es utilizable en línea.
    * El ejemplo que me parece canónico para esto sería el uso de Word2Vec para modelar la semántica de las palabras en los textos.
