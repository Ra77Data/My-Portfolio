# 📊 Age Structure Analysis of CONICET Researchers (2022)

## 📜 Project Summary

This project conducts a demographic analysis of the age distribution of researchers at the **National Scientific and Technical Research Council (CONICET)** of Argentina, using public data from the year 2022.

The objective is to understand the age structure of the scientific research career within the country's main science organization. The analysis segments researchers by their category (from Assistant to Superior) to visualize and quantify how age correlates with advancement in a scientific career.

## 🚀 Main Findings

The analysis reveals a well-defined age structure and a clear progression as the hierarchy in the research career increases.

* **Overall Average Age:** The average age of a CONICET researcher in 2022 is **47.7 years**.

* **Correlation between Age and Category:** A strong positive correlation is observed between the researcher's category and their age. Initial categories, such as "Assistant Researcher," group the youngest professionals, while the "Superior Researcher" category is composed of the most experienced and older scientists.

* **Statistical Summary by Category:** Below is the statistical detail of age for each researcher category:

| researcher_category | Count | Mean | Std. Dev. | Min | 25% | 50% (Median) | 75% | Max |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Assistant Researcher** | 12095 | 40.12 | 4.88 | 29.0 | 37.0 | 40.0 | 43.0 | 66.0 |
| **Adjunct Researcher** | 9845 | 47.79 | 5.86 | 34.0 | 44.0 | 47.0 | 51.0 | 78.0 |
| **Independent Researcher** | 4872 | 56.41 | 6.84 | 41.0 | 51.0 | 56.0 | 61.0 | 88.0 |
| **Principal Researcher** | 2102 | 65.02 | 7.21 | 48.0 | 60.0 | 65.0 | 70.0 | 91.0 |
| **Superior Researcher** | 309 | 73.08 | 7.02 | 55.0 | 68.0 | 73.0 | 78.0 | 91.0 |

---

## 🛠️ Methodology

The analysis was carried out using Python in a Jupyter notebook (`CONICET_edades.ipynb`), following these steps:

1.  **Data Loading and Cleaning:** The `personas_2022.csv` dataset was loaded using `pandas`. An initial cleaning was performed, removing rows where the researcher category was null to focus the analysis exclusively on career personnel.
2.  **General Descriptive Analysis:** The overall mean age was calculated, and a histogram was generated to visualize the distribution of all personnel.
3.  **Segmented Analysis by Category:** The data was grouped by `categoria_investigador` to:
    * Generate comparative visualizations (Box Plots and Violin Plots) showing the age distribution at each level.
    * Calculate detailed descriptive statistics (mean, median, quartiles, etc.) for each category.

## 🗂️ Repository Structure

* `personas_2022.csv`: The original dataset with CONICET personnel data.
* `CONICET_edades.ipynb`: Jupyter notebook with the complete analysis code and visualizations.
* `README.md`: This file.

## 🚀 Getting Started

To run this analysis in your own environment:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Ra77Data/My-Portfolio.git](https://github.com/Ra77Data/My-Portfolio.git)
    cd My-Portfolio/CONICET_edades
    ```

2.  **Install dependencies:**
    ```bash
    pip install pandas matplotlib seaborn
    ```

3.  **Run the notebook:**
    Open and run the `CONICET_edades.ipynb` file.

---
---

# 📊 Análisis de la Estructura Etaria de Investigadores del CONICET (2022)

## 📜 Resumen del Proyecto

Este proyecto realiza un análisis demográfico sobre la distribución de edades de los investigadores del **Consejo Nacional de Investigaciones Científicas y Técnicas (CONICET)** de Argentina, utilizando los datos públicos del año 2022.

El objetivo es entender la estructura etaria de la carrera de investigador científico en el principal organismo de ciencia del país. El análisis segmenta a los investigadores por su categoría (desde Asistente hasta Superior) para visualizar y cuantificar cómo la edad se correlaciona con el avance en la carrera científica.

## 🚀 Principales Hallazgos

El análisis revela una estructura de edad bien definida y una progresión clara a medida que aumenta la jerarquía en la carrera de investigador.

* **Edad Promedio General:** La edad promedio de un investigador del CONICET en 2022 es de **47.7 años**.

* **Correlación entre Edad y Categoría:** Se observa una fuerte correlación positiva entre la categoría del investigador y su edad. Las categorías iniciales, como "Investigador Asistente", agrupan a los profesionales más jóvenes, mientras que la categoría "Investigador Superior" está compuesta por los científicos de mayor trayectoria y edad.

* **Resumen Estadístico por Categoría:** A continuación se presenta el detalle estadístico de la edad para cada categoría de investigador:

| categoria_investigador | Cantidad | Media | Desv. Est. | Mín. | 25% | 50% (Mediana) | 75% | Máx. |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Investigador Asistente** | 12095 | 40.12 | 4.88 | 29.0 | 37.0 | 40.0 | 43.0 | 66.0 |
| **Investigador Adjunto** | 9845 | 47.79 | 5.86 | 34.0 | 44.0 | 47.0 | 51.0 | 78.0 |
| **Investigador Independiente** | 4872 | 56.41 | 6.84 | 41.0 | 51.0 | 56.0 | 61.0 | 88.0 |
| **Investigador Principal** | 2102 | 65.02 | 7.21 | 48.0 | 60.0 | 65.0 | 70.0 | 91.0 |
| **Investigador Superior** | 309 | 73.08 | 7.02 | 55.0 | 68.0 | 73.0 | 78.0 | 91.0 |

---

## 🛠️ Metodología

El análisis se llevó a cabo utilizando Python en un notebook de Jupyter (`CONICET_edades.ipynb`), siguiendo los siguientes pasos:

1.  **Carga y Limpieza de Datos:** Se cargó el dataset `personas_2022.csv` con `pandas`. Se realizó una limpieza inicial, eliminando las filas donde la categoría de investigador era nula para enfocar el análisis exclusivamente en el personal de carrera.
2.  **Análisis Descriptivo General:** Se calculó la media de edad general y se generó un histograma para visualizar la distribución de todo el personal.
3.  **Análisis Segmentado por Categoría:** Se agruparon los datos por `categoria_investigador` para:
    * Generar visualizaciones comparativas (Box Plots y Violin Plots) que muestran la distribución de edades en cada nivel.
    * Calcular estadísticas descriptivas detalladas (media, mediana, cuartiles, etc.) para cada categoría.

## 🗂️ Estructura del Repositorio

* `personas_2022.csv`: El dataset original con datos del personal de CONICET.
* `CONICET_edades.ipynb`: Notebook de Jupyter con el código completo del análisis y las visualizaciones.
* `README.md`: Este archivo.

## 🚀 Cómo Empezar

Para ejecutar este análisis en tu propio entorno:

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/Ra77Data/My-Portfolio.git](https://github.com/Ra77Data/My-Portfolio.git)
    cd My-Portfolio/CONICET_edades
    ```

2.  **Instala las dependencias:**
    ```bash
    pip install pandas matplotlib seaborn
    ```

3.  **Ejecuta el notebook:**
    Abre y ejecuta el archivo `CONICET_edades.ipynb`.
