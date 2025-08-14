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
