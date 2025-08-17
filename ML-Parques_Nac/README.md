# 🏞️ Analysis and Prediction of Visits to National Parks in Argentina

## 📜 Project Summary

This project aims to analyze the time series of visits to the National Parks of Argentina to identify patterns and seasonalities. Subsequently, a Machine Learning model using **XGBoost** is developed to predict the number of future visitors.

The analysis provides an understanding of tourism trends, while the predictive model can serve as a valuable tool for resource planning, staff management, and marketing strategies in the parks.

## 📊 Visualization and Exploratory Data Analysis (EDA)

The first step was to load, clean, and visualize the data. The analysis revealed a **strong annual seasonality** in visits, with peaks during the summer months (January and February) and troughs in the winter months.

## ⚙️ Methodology

The workflow can be summarized in the following steps:

1.  **Data Loading and Cleaning**: The `visitas-residentes-y-no-residentes.csv` dataset was loaded. An initial cleaning was performed, consolidating visitor data into a single "total visits" metric per date.

2.  **Feature Engineering**: To prepare the data for the model, new features were created:
    * Temporal variables such as `year`, `month`, and `day of the week` were extracted.
    * **Lag features** were created for the previous 3 months, allowing the model to learn from recent trends.
    * **One-Hot Encoding** was applied to the `month` variable to treat it as a categorical feature.

3.  **Modeling with XGBoost**:
    * An **XGBoost Regressor** model was used, a powerful gradient boosting implementation ideal for tabular data and time series.
    * The data was split sequentially into training and test sets (80/20) to respect the chronological order and avoid data leakage.
    * Numerical features were scaled using `StandardScaler`.

## 📈 Results and Evaluation

The model was evaluated on the test set, obtaining the following results:

* **Mean Absolute Error (MAE): 0.73**
* **Root Mean Squared Error (RMSE): 0.88**

*Note: These metrics are calculated on the normalized data.*

The following graph compares the model's predictions (orange) with the actual values (blue) on the test set, demonstrating a good ability to follow the trend and seasonality of the data.

## 🚀 Getting Started

To run this project in your local environment, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USER/YOUR_REPOSITORY.git](https://github.com/YOUR_USER/YOUR_REPOSITORY.git)
    cd PATH_TO_PROJECT
    ```

2.  **Install dependencies:**
    Make sure you have the following Python libraries installed:
    ```bash
    pip install pandas matplotlib scikit-learn xgboost
    ```

3.  **Run the notebook:**
    Open and run the `Parques_Nac.ipynb` file in an environment like Jupyter Notebook or Google Colab.

---
---

# 🏞️ Análisis y Predicción de Visitas a Parques Nacionales de Argentina

## 📜 Resumen del Proyecto

Este proyecto tiene como objetivo analizar la serie temporal de visitas a los Parques Nacionales de Argentina para identificar patrones y estacionalidades. Posteriormente, se desarrolla un modelo de Machine Learning utilizando **XGBoost** para predecir el número de visitantes futuros.

El análisis permite entender las tendencias de turismo, mientras que el modelo predictivo puede servir como una herramienta valiosa para la planificación de recursos, gestión de personal y estrategias de marketing en los parques.

## 📊 Visualización y Análisis Exploratorio (EDA)

El primer paso fue cargar, limpiar y visualizar los datos. El análisis reveló una **fuerte estacionalidad anual** en las visitas, con picos durante los meses de verano (enero y febrero) y valles en los meses de invierno.

## ⚙️ Metodología

El flujo de trabajo se puede resumir en los siguientes pasos:

1.  **Carga y Limpieza de Datos**: Se cargó el dataset `visitas-residentes-y-no-residentes.csv`. Se realizó una limpieza inicial, consolidando los datos de visitantes en una única métrica de "visitas totales" por fecha.

2.  **Ing
