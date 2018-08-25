## Sistemas de Recomendación - IIC3633 - Blog - Alain Raymond
### 2do Semestre 2018

#### Semana 3:  Shani, Guy, and Asela Gunawardana. “Evaluating recommendation systems.”

### Resumen

La lectura trata sobre prácticas y consideraciones a la hora de evaluar sistemas de recomendaciones.
#### Tipos de Experimento
Primero, se plantean los tipos de experimentos que se pueden efectuar con sistemas recomendadores:

* **Offline**: se realizan en base a datasets y se modela el comportamiento del usuario. No requiere interacción con el usuario.
   * **Ventajas**:
     * Relativamente barato.
   * **Desventajas**:
     * Muy susceptible al modelo de usuario que se plantee. Potencialmente, podría arruinar el rendimiento del recomendador si se hace mal.
     * Poco eficaz para determinar 
* **Estudios de Usuario**: se muestrea a un subgrupo de los usuarios finales del sistema y explícitamente se les pide retroalimentación respecto al sistema.
  * **Ventajas**:
    * Se puede obtener información muy detallada del usuario y retroalimentación para mejorar el recomendador.
    * Es el único método que permite extraer información cualitativa directamente del usuario.
  * **Desventajas**:
    * Es mucho más caro.
    * Hay que tener cuidado en la construcción del experimento para no inducir sesgos en las respuestas de los usuarios. 
* **Online**: los usuarios son parte del experimento sin saberlo y prueban el sistema de recomendación directamente.
  * **Ventajas**:
     * Permite ver el comportamiento del usuario directamente frente a distintas configuraciones del recomendador.
  * **Desventajas**:
     * Relativamente caro, pues debe ser implementado y puesto en producción.
     * Si algo sale mal, es posible que el recomendador disuada a los usuarios de consumir el producto o la herramienta asociada al producto.

#### Propiedades de los sistemas de recomendación

A la vez, se plantean las distintas propiedades en que se puede enfocar un sistema de recomendación, más allá de la precisión.

* **Preferencia de Usuario**: tomar en cuenta la opinión del usuario sobre los sistemas de recomendación, con algún método.
* **Precisión**: qué tan precisamente (según alguna métrica) estamos prediciendo ratings o listas de recomendación para nuestros usuarios.
* **Cobertura**: cuánto del espacio de ítems o usuarios podemos alcanzar con nuestras recomendaciones. 
* **Confianza (Confidence)**: cuánto podemos confiar estadísticamente en los resultados de los sistemas de recomendación.
* **Fiabilidad (Trust)**: qué tanto el usuario siente que puede confiar en la calidad de las recomendaciones que el sistema le propone.
* **Novedad**: cuan novedosas son las recomendaciones que hace el sistema de recomendación. Novedoso en el sentido de que el usuario no haya experimentado el ítem antes.
* **Serendipia**: ligeramente distinto al anterior. Se refiere a qué tan inesperadas son las recomendaciones que hace el sistema.
  * Todo momento de serendipia es novedoso, pero no todo momento novedoso es un momento de serendipia.
* **Diversidad**: qué tan distintas son las recomendaciones entre ellas.
* **Utilidad**: qué tanto aporta el sistema de recomendación en alguna métrica deseada. Por ejemplo, ingresos, vistas en una página web, tiempo total de atención, etc.
* **Riesgo**: que el sistema considere variables de aversión/inclinación al riesgo en sus recomendaciones. 
* **Robustez**: qué tan susceptible es el sistema a potenciales ataques por usuarios maliciosos. 
* **Privacidad**: el sistema debe considerar no revelar preferencias personales de sus usuarios.
* **Adaptatividad**: cuánto puede modificar sus recomendaciones el sistema a cambios en el contexto importantes. Por ejemplo, sugerencias de noticias dado que sucedió algún evento.
* **Escalabilidad**: cuánto rendimiento puede ofrecer el sistema en distintas métricas como throughput, cantidad de usuarios concurrentes, tiempos de respuesta, etc.
 
 ### Comentarios

* El texto ofrece buenas y razonablemente concretas pautas para guiarse a la hora de medir un sistema de recomendación.
  * En particular, me parece interesante ver todas las otras dimensiones a considerar más allá de la precisión.
    * Esto me hace pensar que el mundo de los sistemas recomendadores tiene más cercanía con el mundo de las ciencias sociales (o al menos con teorías de comportamiento) que el resto del mundo de aprendizaje de máquina.
  * Además, la descripción del proceso de experimentación a implementación me parece valiosa.
    * El paso de Experimentos Offline durante una fase exploratorio, a Estudios de Usuario para ajustar (si tenemos los recursos) y finalmente cuando ya tenemos candidatos serios pasar a Experimentación Online, es sensato.
* La *Serendipia* en particular parece una medida muy difícil de medir fiablemente. Menos aún de implementar en un sistema recomendador con algún nivel decente de rendimiento.
* No sé si el criterio de Escalabilidad es algo propiamente de los sistemas recomendadores. Si bien entiendo que efectivamente puedes tomar decisiones respecto al rendimiento del recomendador para obtener mejor escalabilidad, me parece más una decisión técnica que del sistema de recomendación en sí.
* Es terrible pensar que no hay sistema de recomendación que no sea susceptible a ataques. En particular, -dependiendo del costo que éstos impliquen- pueden significar una distorsión significativa de los resultados de los sistemas recomendadores, convirtiéndolos de herramientas útiles a simplemente sistemas encubiertos de publicidad o propaganda. Esto aniquila el propósito de que existan.
