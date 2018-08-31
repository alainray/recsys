## Sistemas de Recomendación - IIC3633 - Blog - Alain Raymond
### 2do Semestre 2018

#### Semana 4:  Pazzani, M. J., & Billsus, D. (2007). Content-based recommendation systems

### Resumen

La lectura presenta los elementos a modelar para emprender la tarea de implementar un sistema de recomendación basado en contenido. Primero hay que tener una representación del ítem, sea númericamente, features, clases, etc. Luego, de una u otra manera ocupamos la información de la relación entre el usuario y los ítems. Con esto construimos un modelo del usuario o aprovechamos esa historia para filtrar o sugerir recomendaciones, por ejemplo, no recomendar algo ya consumido.

Después se discuten distintos métodos para aprender modelos de usuario como. 
  * Árboles de Decisión e Inducción de Reglas
  * Métodos de Vecinos Cercanos
  * Retroalimentación de Relevancia y el algoritmo de Rocchio
  * Clasificadores lineales (SVM et al)
  * Modelos Probabilísticos y Naive Bayes

Finalmente se habla de las limitaciones y posibles extensiones de estos sistemas.

#### Comentarios
* Hay un enfoque excesivo en texto en el artículo. Para actualizarlo, tendría que pensarse en considerar imágenes, video y sonido como parte del contenido.
* La metodología subyacente sería más o menos la misma.
* Este tipo de algoritmos es malo para detectar atributos de los ítems que son fáciles de detectar para los usuarios. El pareo con algoritmos de filtrado colaborativo es relevante.
* La modelación es muy dependiente del ítem, a diferencia de los métodos de filtrado colaborativo.
* Luego, este tipo de algoritmo parece tener más sentido cuando no es posible aplicar filtrado colaborativo.
  * Por ejemplo, si hay temas de privacidad que no deben ser revelados
* Naive Bayes me gusta porque permite enfrentar problemas de polisemia.
* En esta época sería apropiado incluir las redes neuronales profundas como algoritmo candidato para modelar usuarios o el contenido genéricamente.
  * Aunque tienen gran costo computacional, éste es de preprocesamiento. Luego el modelo aprendido es utilizable en línea.
    * El ejemplo que me parece canónico para esto sería el uso de Word2Vec para modelar la semántica de las palabras en los textos.
