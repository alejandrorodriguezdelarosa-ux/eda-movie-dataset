**Análisis Exploratorio de Datos (EDA) del Dataset de Películas**

Este proyecto desarrolla un proceso completo de análisis exploratorio de datos aplicado a un dataset de películas. El trabajo abarca todas las fases necesarias para transformar los datos originales en un conjunto estructurado, homogéneo y preparado para la interpretación visual. El enfoque principal consiste en estudiar el comportamiento de la recaudación en función de variables clave del sector cinematográfico.

1. Objetivo del proyecto

El objetivo principal del análisis es estudiar si la recaudación de las películas se ve afectada por tres factores fundamentales:

El país de origen.

El género principal.

La clasificación por edades.

A partir de este planteamiento, se desarrolla un conjunto de visualizaciones y tablas que permiten evaluar cómo varía la recaudación en función de estos elementos, así como observar diferencias entre mercados y patrones asociados a determinadas categorías.

2. Limpieza y preparación de los datos

Antes de realizar cualquier análisis visual, se diseñó y ejecutó un pipeline de limpieza integral implementado en el archivo cleaning.py. Este proceso incluye:

Normalización de nombres de columnas siguiendo un formato coherente.

Corrección de tipos de datos para variables numéricas, categóricas y temporales.

Tratamiento de valores ausentes mediante imputación razonada (por ejemplo, uso de la moda en variables como país e idioma).

Homogeneización de categorías en columnas como content_rating.

Eliminación de duplicados.

Control y filtrado de valores fuera de rango, especialmente en variables temporales.

Generación de nuevas variables derivadas que enriquecen el análisis:

main_genre, que identifica el género principal a partir de la lista original.

movie_type, que clasifica las películas según su duración.

Tras este proceso, se obtiene un dataset coherente, depurado y listo para su exploración en profundidad.

3. Estructura del Análisis Exploratorio de Datos

El análisis visual se divide en varias tandas de visualizaciones, cada una con un propósito distinto y complementario.

3.1. Visualizaciones básicas

En esta primera fase se inspeccionan las distribuciones y características generales del dataset:

Histogramas de variables como duración, presupuesto, recaudación y puntuación IMDB.

Gráficos de barras sobre categorías clave (género principal, tipo de película, color, entre otras).

Boxplots que permiten observar la variabilidad de la recaudación según el género o la duración según el tipo de película.

Estas visualizaciones proporcionan una visión inicial de las características fundamentales del conjunto de datos.

3.2. Visualizaciones intermedias

Esta fase profundiza en relaciones entre variables y patrones de comportamiento:

Diagramas de dispersión que relacionan presupuesto y recaudación, duración y puntuación IMDB, entre otras variables.

Cálculo y visualización de recaudaciones medias por distintos grupos categóricos.

Mapa de correlaciones diseñado para identificar relaciones significativas entre variables numéricas del dataset.

Esta tanda permite detectar relaciones iniciales que posteriormente se revisan con mayor detalle.

3.3. Visualizaciones avanzadas

En esta etapa se emplean herramientas más detalladas para examinar estructuras internas de los datos:

Pairplots de variables clave que permiten observar tendencias generales y posibles outliers.

Violinplots que muestran la distribución interna de variables numéricas dentro de grupos categóricos.

Visualizaciones con variables transformadas logarítmicamente para manejar rangos muy amplios de recaudación o votos.

Estas herramientas ofrecen una perspectiva más técnica y permiten interpretar mejor fenómenos que no son evidentes en gráficas básicas.

4. Análisis orientado al objetivo principal

Para responder a la pregunta central del proyecto, se emplea una tanda específica de visualizaciones que examina de manera directa las interacciones entre país, género y clasificación por edades. Esta fase incluye:

Boxplots de recaudación por país, que permiten comparar mercados y su comportamiento general.

Gráficos de barras que muestran la recaudación media por género dentro de cada país.

Visualizaciones que relacionan la clasificación por edades con la recaudación, distribuidas por país.

Un conjunto de diagramas combinados donde se observa la interacción país × género × clasificación, lo que permite examinar simultáneamente los tres factores clave del estudio.

Estas visualizaciones son esenciales para interpretar cómo actúan los factores considerados en el objetivo del proyecto.