# 🤖 Modelo Predictivo de Abandono de Empleados

## 📜 Resumen del Proyecto

Este proyecto aborda uno de los desafíos más significativos para el área de Recursos Humanos: la rotación de personal. El objetivo principal es desarrollar un modelo de Machine Learning capaz de predecir la probabilidad de que un empleado abandone la empresa.

Más allá de la predicción, se realiza un profundo análisis para identificar los perfiles de empleados con mayor riesgo y, fundamentalmente, **cuantificar el impacto económico** que esta fuga de talento representa para la organización. El resultado final es una herramienta de scoring que permite a la empresa tomar acciones proactivas y estratégicas para la retención de talento.

## 📊 Dashboard Interactivo en Tableau

Para visualizar los insights más importantes de este análisis, incluyendo el perfil de los empleados en riesgo y el impacto económico, he creado un dashboard interactivo.

**[➡️ Ver Dashboard en Tableau Public](https://public.tableau.com/app/profile/cesar.martin.gonzalez/viz/DashboardEmpleadosenRiesgo/Dashboard1)**

![Tableau Dashboard Preview](https://i.imgur.com/8a6B2c3.png)

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

