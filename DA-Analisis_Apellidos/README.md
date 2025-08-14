# 🇦🇷 Análisis de la Distribución de Apellidos en Argentina (2021)

## 📜 Resumen del Proyecto

Este proyecto realiza un análisis exploratorio sobre la distribución y frecuencia de los apellidos en Argentina, utilizando datos públicos del Registro Nacional de las Personas (RENAPER) correspondientes al año 2021.

El objetivo es identificar los apellidos más comunes en el país, entender su peso demográfico y descubrir datos curiosos sobre la diversidad de apellidos presentes en la población argentina.

## 🚀 Principales Hallazgos

Del análisis se desprenden varios insights clave sobre la demografía argentina:

* **Diversidad de Apellidos:** Se identificaron un total de **348,288 apellidos únicos** en el conjunto de datos.
* **Top 10 Apellidos:** Los apellidos más comunes en Argentina son:
    1.  GONZALEZ
    2.  RODRIGUEZ
    3.  GOMEZ
    4.  FERNANDEZ
    5.  LOPEZ
    6.  MARTINEZ
    7.  DIAZ
    8.  PEREZ
    9.  SANCHEZ
    10. ROMERO
* **Concentración Demográfica:** Estos 10 apellidos representan al **9.36%** del total de la población registrada en el dataset.
* **Apellidos Curiosos:** Se encontró una variedad de apellidos poco comunes y llamativos, como **"ROCK", "PANA", "RAMBO", "BERA"** y **"CUMBIA"**, cada uno con una frecuencia sorprendentemente alta.

---

## 🛠️ Metodología

El análisis se llevó a cabo en un notebook de Jupyter (`Dist_Apellidos_Arg.ipynb`) siguiendo estos pasos:

1.  **Carga y Exploración:** Se cargó el dataset `distribucion-apellidos-2021.csv` con `pandas` para una inspección inicial de la estructura y los tipos de datos.
2.  **Análisis de Frecuencia:** Se filtró el DataFrame para aislar los 10 apellidos más comunes y se calcularon métricas agregadas, como el porcentaje de la población que representan.
3.  **Visualización de Datos:** Se utilizó `matplotlib` y `seaborn` para crear un gráfico de barras horizontal que facilita la comparación de la frecuencia de los apellidos más populares.
4.  **Análisis Adicional:** Se exploraron los datos para encontrar y cuantificar apellidos únicos y curiosos.

## 🗂️ Estructura del Repositorio

* `distribucion-apellidos-2021.csv`: El dataset original del RENAPER.
* `Dist_Apellidos_Arg.ipynb`: Notebook de Jupyter con todo el código del análisis y las visualizaciones.
* `README.md`: Este archivo.

## 🚀 Cómo Empezar

Para ejecutar este análisis en tu propio entorno:

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/Ra77Data/My-Portfolio.git](https://github.com/Ra77Data/My-Portfolio.git)
    cd My-Portfolio/Dist_Apellidos_Arg
    ```

2.  **Instala las dependencias:**
    ```bash
    pip install pandas matplotlib seaborn
    ```

3.  **Ejecuta el notebook:**
    Abre y ejecuta el archivo `Dist_Apellidos_Arg.ipynb`.
