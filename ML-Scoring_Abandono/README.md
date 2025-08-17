# 🤖 Employee Churn Prediction Model

## 📜 Project Summary

This project addresses one of the most significant challenges for the Human Resources area: employee turnover. The main objective is to develop a Machine Learning model capable of predicting the probability of an employee leaving the company.

Beyond prediction, a deep analysis is carried out to identify the profiles of employees at higher risk and, fundamentally, to **quantify the economic impact** that this talent drain represents for the organization. The final result is a scoring tool that allows the company to take proactive and strategic actions for talent retention.

## 📊 Interactive Dashboard in Tableau

To visualize the most important insights from this analysis, including the profile of at-risk employees and the economic impact, I have created an interactive dashboard.

**[➡️ View Dashboard on Tableau Public](https://public.tableau.com/app/profile/cesar.martin.gonzalez/viz/DashboardEmpleadosenRiesgo/Dashboard1)**

---

## 🚀 Methodology and Workflow

The project is structured in two main phases, each contained in its own Jupyter notebook.

### 1. Exploratory and Business Analysis (`Analisis_de_Abandono.ipynb`)

In this initial phase, the focus was on understanding the data and extracting key business insights.

* **Data Analysis (EDA):** Variables were explored to identify patterns, distributions, and correlations. A thorough cleaning was performed, handling null values and removing irrelevant variables (e.g., `mayor_edad`, `horas_quincena`).
* **Problem Quantification:** The **churn rate was determined to be 16.1%**.
* **Employee Profile:** A common profile was identified among employees who leave: low education level, single, with a high load of overtime, and notably, a high incidence in the **Sales Representative** position.
* **Economic Impact Analysis:** The annual cost of employee turnover was calculated, estimating a loss of **$2.7 million** in the last year. Additionally, the potential savings from reducing the churn rate by different percentages were projected (e.g., a saving of ~$271k by reducing churn by 10%).

### 2. Model Building and Evaluation (`Modelo_ML_Upgrade_II.ipynb`)

With the data cleaned and enriched, the modeling phase proceeded.

* **Preprocessing:** Categorical variables were transformed into a numerical format using `OneHotEncoder` and features were scaled with `StandardScaler`.
* **Model Training:** The data was split into training (70%) and testing (30%) sets. A **Logistic Regression** model was chosen for its interpretability and good performance.
* **Optimization and Results:** `GridSearchCV` was used to find the best hyperparameters. The final model achieved robust performance, with a **ROC AUC of 0.82**. This represents a **22.9% improvement** over an initial baseline model.
* **Scoring Generation:** Finally, the trained model was used to generate a score (`scoring_abandono`) for each employee, indicating their probability of leaving.

---

## 🛠️ Project Structure

* `AbandonoEmpleados.csv`: The original dataset and starting point of the analysis.
* `Analisis_de_Abandono.ipynb`: Notebook with exploratory analysis, data cleaning, and business impact analysis.
* `df_abandono.csv`: The resulting dataset from the first notebook, clean and ready for modeling.
* `Modelo_ML_Upgrade_II.ipynb`: Notebook with the construction, training, and evaluation of the Machine Learning model.
* `abandono_con_scoring2.xlsx`: Final file with the churn probability score for each employee.
* `README.md`: This file.

## 🚀 Getting Started

To run this project in your local environment, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Ra77Data/My-Portfolio.git](https://github.com/Ra77Data/My-Portfolio.git)
    cd My-Portfolio/ML-Scoring_Abandono
    ```

2.  **Install dependencies:**
    Make sure you have the following Python libraries installed:
    ```bash
    pip install pandas numpy matplotlib scikit-learn
    ```

3.  **Run the notebooks:**
    To replicate the results, run the notebooks in the following order:
    1.  `Analisis_de_Abandono.ipynb`
    2.  `Modelo_ML_Upgrade_II.ipynb`

## 💡 Strategic Applications

The results of this model allow the company to:

* **Retain Talent:** Proactively identify employees at high risk of leaving to implement personalized retention plans.
* **Optimize Investment:** Focus HR resources on profiles with the greatest economic impact and highest probability of churn.
* **Improve Workplace Climate:** Use insights about the reasons for leaving (e.g., overtime, low salary, position) to make strategic decisions that improve working conditions.

---
---

# 🤖 Modelo Predictivo de Abandono de Empleados

## 📜 Resumen del Proyecto

Este proyecto aborda uno de los desafíos más significativos para el área de Recursos Humanos: la rotación de personal. El objetivo principal es desarrollar un modelo de Machine Learning capaz de predecir la probabilidad de que un empleado abandone la empresa.

Más allá de la predicción, se realiza un profundo análisis para identificar los perfiles de empleados con mayor riesgo y, fundamentalmente, **cuantificar el impacto económico** que esta fuga de talento representa para la organización. El resultado final es una herramienta de scoring que permite a la empresa tomar acciones proactivas y estratégicas para la retención de talento.

## 📊 Dashboard Interactivo en Tableau

Para visualizar los insights más importantes de este análisis, incluyendo el perfil de los empleados en riesgo y el impacto económico, he creado un dashboard interactivo.

**[➡️ Ver Dashboard en Tableau Public](https://public.tableau.com/app/profile/cesar.martin.gonzalez/viz/DashboardEmpleadosenRiesgo/Dashboard1)**

---

## 🚀 Metodología y Flujo de Trabajo

El proyecto se estructura en dos fases principales, cada una contenida en su propio notebook de Jupyter.

### 1. Análisis Exploratorio y de Negocio (`Analisis_de_Abandono.ipynb`)

En esta fase inicial, el foco estuvo en entender los datos y extraer insights de negocio clave.

* **Análisis de Datos (EDA):** Se exploraron las variables para identificar patrones, distribuciones y correlaciones. Se realizó una limpieza exhaustiva, tratando valores nulos y eliminando variables irrelevantes (ej. `mayor_edad`, `horas_quincena`).
* **Cuantificación del Problema:** Se determinó que la **tasa de abandono es del 16.1%**.
* **Perfil del Empleado:** Se identificó un perfil común entre los empleados que abandonan: bajo nivel educativo, solteros, con alta carga de horas extra y, notablemente, una alta incidencia en el puesto de **Representante de Ventas**.
* **Análisis de Impacto Económico:** Se calculó el coste anual de la rotación de personal, estimando una pérdida de **$2.7 millones** en el último año. Además, se proyectó el ahorro potencial al reducir la tasa de abandono en diferentes porcentajes (ej. un ahorro de ~$271k al reducir la fuga en un 10%).

### 2. Construcción y Evaluación del Modelo (`Modelo_ML_Upgrade_II.ipynb`)

Con los datos limpios y enriquecidos, se procedió a la fase de modelado.

* **Preprocesamiento:** Se transformaron las variables categóricas a un formato numérico mediante `OneHotEncoder` y se escalaron las características con `StandardScaler`.
* **Entrenamiento del Modelo:** Se dividieron los datos en conjuntos de entrenamiento (70%) y prueba (30%). Se eligió un modelo de **Regresión Logística** por su interpretabilidad y buen rendimiento.
* **Optimización y Resultados:** Se utilizó `GridSearchCV` para encontrar los mejores hiperparámetros. El modelo final alcanzó un rendimiento robusto, con un **ROC AUC de 0.82**. Esto representa una **mejora del 22.9%** respecto a un modelo base inicial.
* **Generación de Scoring:** Finalmente, el modelo entrenado se utilizó para generar una puntuación (`scoring_abandono`) para cada empleado, indicando su probabilidad de abandono.

---

## 🛠️ Estructura del Proyecto

* `AbandonoEmpleados.csv`: El dataset original y punto de partida del análisis.
* `Analisis_de_Abandono.ipynb`: Notebook con el análisis exploratorio, limpieza de datos y análisis de impacto de negocio.
* `df_abandono.csv`: Dataset resultante del primer notebook, limpio y listo para el modelado.
* `Modelo_ML_Upgrade_II.ipynb`: Notebook con la construcción, entrenamiento y evaluación del modelo de Machine Learning.
* `abandono_con_scoring2.xlsx`: Archivo final con el scoring de probabilidad de abandono para cada empleado.
* `README.md`: Este archivo.

## 🚀 Cómo Empezar

Para ejecutar este proyecto en tu entorno local, sigue estos pasos:

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/Ra77Data/My-Portfolio.git](https://github.com/Ra77Data/My-Portfolio.git)
    cd My-Portfolio/ML-Scoring_Abandono
    ```

2.  **Instala las dependencias:**
    Asegúrate de tener las siguientes librerías de Python instaladas:
    ```bash
    pip install pandas numpy matplotlib scikit-learn
    ```

3.  **Ejecuta los notebooks:**
    Para replicar los resultados, ejecuta los notebooks en el siguiente orden:
    1.  `Analisis_de_Abandono.ipynb`
    2.  `Modelo_ML_Upgrade_II.ipynb`

## 💡 Aplicaciones Estratégicas

Los resultados de este modelo permiten a la empresa:

* **Fidelizar Talento:** Identificar de forma proactiva a los empleados con alto riesgo de abandono para implementar planes de retención personalizados.
* **Optimizar la Inversión:** Enfocar los recursos de RRHH en los perfiles de mayor impacto económico y mayor probabilidad de fuga.
* **Mejorar el Clima Laboral:** Utilizar los insights sobre los motivos del abandono (ej. horas extra, bajo salario, puesto) para tomar decisiones estratégicas que mejoren las condiciones laborales.
