# 🏞️ Análisis y Predicción de Visitas a Parques Nacionales de Argentina

## 📜 Resumen del Proyecto

Este proyecto tiene como objetivo analizar la serie temporal de visitas a los Parques Nacionales de Argentina para identificar patrones y estacionalidades. Posteriormente, se desarrolla un modelo de Machine Learning utilizando **XGBoost** para predecir el número de visitantes futuros.

El análisis permite entender las tendencias de turismo, mientras que el modelo predictivo puede servir como una herramienta valiosa para la planificación de recursos, gestión de personal y estrategias de marketing en los parques.

## 📊 Visualización y Análisis Exploratorio (EDA)

El primer paso fue cargar, limpiar y visualizar los datos. El análisis reveló una **fuerte estacionalidad anual** en las visitas, con picos durante los meses de verano (enero y febrero) y valles en los meses de invierno.


## ⚙️ Metodología

El flujo de trabajo se puede resumir en los siguientes pasos:

1.  **Carga y Limpieza de Datos**: Se cargó el dataset `visitas-residentes-y-no-residentes.csv`. Se realizó una limpieza inicial, consolidando los datos de visitantes en una única métrica de "visitas totales" por fecha.

2.  **Ingeniería de Características (Feature Engineering)**: Para preparar los datos para el modelo, se crearon nuevas características:
    * Se extrajeron variables temporales como `año`, `mes` y `día de la semana`.
    * Se crearon **variables de retardo (lag features)** para los 3 meses anteriores, permitiendo que el modelo aprenda de las tendencias recientes.
    * Se aplicó **One-Hot Encoding** a la variable `mes` para tratarla de forma categórica.

3.  **Modelado con XGBoost**:
    * Se utilizó un modelo **XGBoost Regressor**, una potente implementación de gradient boosting ideal para datos tabulares y series de tiempo.
    * Los datos se dividieron en conjuntos de entrenamiento y prueba (80/20) de forma secuencial para respetar el orden cronológico y evitar la fuga de datos.
    * Las características numéricas fueron escaladas utilizando `StandardScaler`.

## 📈 Resultados y Evaluación

El modelo fue evaluado en el conjunto de prueba, obteniendo los siguientes resultados:

* **Mean Absolute Error (MAE): 0.73**
* **Root Mean Squared Error (RMSE): 0.88**

*Nota: Estas métricas se calculan sobre los datos normalizados.*

La siguiente gráfica compara las predicciones del modelo (naranja) con los valores reales (azul) en el conjunto de prueba, demostrando una buena capacidad para seguir la tendencia y la estacionalidad de los datos.


## 🚀 Cómo Empezar

Para ejecutar este proyecto en tu entorno local, sigue estos pasos:

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)
    cd RUTA_AL_PROYECTO
    ```

2.  **Instala las dependencias:**
    Asegúrate de tener las siguientes librerías de Python instaladas:
    ```bash
    pip install pandas matplotlib scikit-learn xgboost
    ```

3.  **Ejecuta el notebook:**
    Abre y ejecuta el archivo `Parques_Nac.ipynb` en un entorno como Jupyter Notebook o Google Colab.
