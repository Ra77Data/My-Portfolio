# 🏆 Statistical Analysis of the FIFA World Cup 2022

## 📜 Project Goal

This project goes beyond individual match results to create a **consolidated statistical performance profile** for each national team that participated in the 2022 World Cup. The objective is to aggregate data from all matches played by a team to analyze its overall performance in the tournament and determine which teams led in key game metrics, such as offense, defense, and ball control.

## 🚀 Key Findings

The analysis revealed that a select group of teams consistently dominated most statistical categories.

* **Most Outstanding Teams:** By counting the times each team ranked #1 in the 42 analyzed metrics, the clear leaders were:
    1.  **Croatia:** Leader in 12 statistics.
    2.  **Morocco:** Leader in 11 statistics.
    3.  **Argentina:** Leader in 10 statistics.
    4.  **France:** Leader in 4 statistics.

### 🇦🇷 Analysis of the Champion: Argentina

A deeper analysis of the world champion, Argentina, demonstrates their dominance and consistency throughout the tournament:

* **Absolute Leader in 10 Key Categories:** Argentina positioned itself as the best team in the tournament in offensive and pressure metrics, including:
    * Total goals and goals from inside the box.
    * Shots on target.
    * Fouls received.
    * Corner kicks and free kicks.
    * Penalties converted.
    * Forced recoveries and defensive pressures applied.

* **Presence Among the Elite:** Of the 42 statistics analyzed, **Argentina was in the Top 4 in 34 of them**, proving to be one of the most complete and consistent teams of the World Cup.

---

## 🛠️ Methodology

The project was developed in two main phases across two Jupyter notebooks:

1.  **Data Cleaning and Preparation (`FIFAWC2022.ipynb`):**
    * The `Fifa_world_cup_matches.csv` dataset, containing detailed data for each match, was loaded.
    * Columns irrelevant to the statistical analysis were removed (e.g., `date`, `hour`, `category`).
    * Possession columns (expressed as text percentages) were converted to a numerical format (float) to enable calculations.
    * The cleaned dataset was saved as `df_fifawc2022.csv`.

2.  **Consolidation and Team-Based Analysis (`FIFAWC2022-2.ipynb`):**
    * The `df_fifawc2022.csv` file was loaded.
    * A script was created to transform individual match data into a consolidated summary by team, aggregating the statistics for each nation across all their games.
    * With the new consolidated DataFrame, the teams were ranked in each of the 42 metrics to identify the tournament leaders.

## 🗂️ Repository Structure

* `Fifa_world_cup_matches.csv`: Original dataset with statistics from the 64 matches.
* `df_fifawc2022.csv`: Intermediate dataset, resulting from the cleaning in the first notebook.
* `FIFAWC2022.ipynb`: Notebook with the data cleaning and preprocessing steps.
* `FIFAWC2022-2.ipynb`: Notebook with the main analysis, team data consolidation, and statistical rankings.
* `README.md`: This file.

## 🚀 Getting Started

To run this project in your local environment, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Ra77Data/My-Portfolio.git](https://github.com/Ra77Data/My-Portfolio.git)
    cd My-Portfolio/FIFAWC2022
    ```

2.  **Install dependencies:**
    This project primarily uses the `pandas` library.
    ```bash
    pip install pandas
    ```

3.  **Run the notebooks:**
    To replicate the results, run the notebooks in the following order:
    1.  `FIFAWC2022.ipynb`
    2.  `FIFAWC2022-2.ipynb`

---
---

# 🏆 Análisis Estadístico de la Copa Mundial de la FIFA 2022

## 📜 Objetivo del Proyecto

Este proyecto va más allá de los resultados individuales de los partidos para crear un **perfil de rendimiento estadístico consolidado** para cada selección nacional que participó en la Copa del Mundo 2022. El objetivo es agregar los datos de todos los partidos jugados por un equipo para analizar su desempeño general en el torneo y determinar qué equipos lideraron en las métricas clave del juego, como ofensiva, defensa y control del balón.

## 🚀 Principales Hallazgos

El análisis reveló que un grupo selecto de equipos dominó consistentemente en la mayoría de las categorías estadísticas.

* **Equipos más Destacados:** Al contar las veces que cada equipo se posicionó como el #1 en las 42 métricas analizadas, los líderes claros fueron:
    1.  **Croacia:** Líder en 12 estadísticas.
    2.  **Marruecos:** Líder en 11 estadísticas.
    3.  **Argentina:** Líder en 10 estadísticas.
    4.  **Francia:** Líder en 4 estadísticas.

### 🇦🇷 Análisis del Campeón: Argentina

Un análisis más profundo sobre el campeón del mundo, Argentina, demuestra su dominio y consistencia a lo largo del torneo:

* **Líder Absoluto en 10 Categorías Clave:** Argentina se posicionó como el mejor equipo del torneo en métricas ofensivas y de presión, incluyendo:
    * Goles totales y goles dentro del área.
    * Tiros al arco.
    * Faltas recibidas.
    * Tiros de esquina y tiros libres.
    * Penales convertidos.
    * Recuperaciones forzadas y presiones defensivas aplicadas.

* **Presencia en la Élite:** De las 42 estadísticas analizadas, **Argentina se encontró en el Top 4 en 34 de ellas**, demostrando ser uno de los equipos más completos y consistentes del mundial.

---

## 🛠️ Metodología

El proyecto se desarrolló en dos fases principales a través de dos notebooks de Jupyter:

1.  **Limpieza y Preparación de Datos (`FIFAWC2022.ipynb`):**
    * Se cargó el dataset `Fifa_world_cup_matches.csv`, que contiene datos detallados de cada partido.
    * Se eliminaron columnas irrelevantes para el análisis estadístico (ej. `date`, `hour`, `category`).
    * Se convirtieron las columnas de posesión (expresadas en porcentajes como texto) a un formato numérico (float) para poder realizar cálculos.
    * El dataset limpio se guardó como `df_fifawc2022.csv`.

2.  **Consolidación y Análisis por Equipo (`FIFAWC2022-2.ipynb`):**
    * Se cargó el archivo `df_fifawc2022.csv`.
    * Se creó un script para transformar los datos de partidos individuales en un resumen consolidado por equipo, agregando las estadísticas de cada selección a lo largo de todos sus encuentros.
    * Con el nuevo DataFrame consolidado, se procedió a ranquear a los equipos en cada una de las 42 métricas para identificar a los líderes del torneo.

## 🗂️ Estructura del Repositorio

* `Fifa_world_cup_matches.csv`: Dataset original con las estadísticas de los 64 partidos.
* `df_fifawc2022.csv`: Dataset intermedio, resultado de la limpieza del primer notebook.
* `FIFAWC2022.ipynb`: Notebook con el proceso de limpieza y preprocesamiento de datos.
* `FIFAWC2022-2.ipynb`: Notebook con el análisis principal, consolidación de datos por equipo y ranking de estadísticas.
* `README.md`: Este archivo.

## 🚀 Cómo Empezar

Para ejecutar este proyecto en tu entorno local, sigue estos pasos:

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/Ra77Data/My-Portfolio.git](https://github.com/Ra77Data/My-Portfolio.git)
    cd My-Portfolio/FIFAWC2022
    ```

2.  **Instala las dependencias:**
    Este proyecto utiliza principalmente la librería `pandas`.
    ```bash
    pip install pandas
    ```

3.  **Ejecuta los notebooks:**
    Para replicar los resultados, ejecuta los notebooks en el siguiente orden:
    1.  `FIFAWC2022.ipynb`
    2.  `FIFAWC2022-2.ipynb`
