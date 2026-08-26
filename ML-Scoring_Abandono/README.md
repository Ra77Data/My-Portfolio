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

## 🎯 Recommendations by Profile

> Logical recommendations derived from the exploratory analysis and the
> predictive model (Logistic Regression, ROC AUC ≈ 0.80–0.83, PR-AUC ≈ 0.57).
> They complement the churn scoring and the decision threshold.

### Cross-cutting churn drivers (model odds ratios)

| Risk factor | Odds ratio |
|---|---|
| Overtime = Yes | **2.40×** |
| Environment satisfaction = Low | 2.26× |
| Frequent business travel | 2.02× |
| Laboratory Technician role | 1.93× |
| Sales Representative role | 1.80× |
| Job satisfaction = Low | 1.76× |
| Coworker satisfaction = Low | 1.70× |
| Marital status Single | 1.66× |
| Years since last promotion (+1 SD) | 1.64× |
| Number of previous companies (+1 SD) | 1.56× |

*Protective factors:* no travel (0.48×), Research Director (0.58×), years with
the current manager (0.59×).

**Cross-cutting pattern:** overtime + low salary + stagnation (no promotion) +
dissatisfaction, concentrated in underpaid technical roles.

### Sales — focus: Sales Representative

**Sales**: 446 employees · 20.6% churn · turnover cost $1.33M/year.
**Hot spot:** *Sales Representative* (83 people, **39.8% churn**, median salary
$2,579/month — the lowest-paid in the company).

| Signal | Leavers | Stayers / rest |
|---|---|---|
| Overtime = Yes | 37.5% churn | 13.8% churn |
| Job satisfaction = Low | 53.6% churn | 16.7% (High) |
| Involvement = Low | 51.7% churn | 16.2% (High) |
| Single | 34.6% churn | 11.5% (Divorced) |
| Average salary | $5,908 | $7,232 |
| Average tenure | 5.5 years | 7.7 years |

**Proposed actions:**
1. **Redesign Sales Representative compensation**: a commission plan or a
   retention-linked bonus, or raise the salary floor (currently $2,579).
2. **Cut overtime**: redistribute accounts/workload and review schedules.
3. **Career path Rep → Executive** with a defined promotion at 18–24 months
   (stagnation raises risk 1.64×).
4. **Mentoring for new hires and singles**, and limit frequent travel.

**Potential saving** (reducing churn by 30%): **$399,928/year** in Sales
($50,787 in Sales Representative alone).

### Research & Development — focus: Laboratory Technician and Research Scientist

**R&D**: 961 employees · 13.8% churn · turnover cost $1.28M/year.
**Hot spots:** *Laboratory Technician* (259, 23.9% churn, $2,886) and
*Research Scientist* (292, 16.1% churn, $2,888).

| Signal | Leavers | Stayers / rest |
|---|---|---|
| Overtime = Yes | 27.3% churn | 8.6% churn |
| Job satisfaction = Low | 22.2% churn | 5.1% (Very High) |
| Involvement = Low | 23.5% churn | 13.4% (High) |
| Average salary | $4,108 | $6,630 (−38%) |
| Technical Degree field | 1.66× risk | — |

**Proposed actions:**
1. **Review the technical salary bands** ($2.9k is very low and the
   leaver/stayer gap is −38%): selective adjustment.
2. **Reduce laboratory overtime** (driver #1: 2.4×).
3. **Engagement/mentoring program** for low involvement and environment.
4. **Promotion path** Lab Technician → Research Scientist → Director
   (Research Director almost never leaves: 0.58×).

**Potential saving** (reducing churn by 30%): **$384,529/year** in R&D
($121,887 in Laboratory Technician alone).

### Human Resources — focus: generalist HR role

**HR**: 63 employees · 19.0% churn · turnover cost $104k/year.
**Hot spot:** *generalist HR role* (52, 23.1% churn, $3,093); HR Managers have
**0% churn**.

| Signal | Leavers | Stayers / rest |
|---|---|---|
| Environment satisfaction = Low | 36.4% churn | 7.7% (High) |
| Frequent travel | 36.4% churn | 17.4% (Rarely) |
| Job satisfaction = Low | 33.3% churn | 13.9% (High) |
| Average salary | $3,716 | $7,346 (**−49%**) |
| Average tenure | 4.2 years | 8.0 years |

**Proposed actions:**
1. **Equalize compensation** (the −49% gap is the largest in the company and
   is unsustainable).
2. **Improve climate/environment** and reduce frequent travel (36.4% churn).
3. **Onboarding + check-ins in the first 2 years** (they leave early).

**Potential saving** (reducing churn by 30%): **$31,245/year**.

### Prioritization by ROI

| Action | Profile | Saving (churn −30%) | Difficulty |
|---|---|---|---|
| Overtime control | Cross-cutting (driver #1, 2.4×) | high, indirect | Medium |
| Technical salary bands | R&D | $121,887 (Lab Tech) | Medium |
| Sales Rep compensation | Sales | $50,787 | Medium |
| HR compensation | HR | $31,245 | Low |
| Career path Rep→Exec | Sales | part of $399,928 | Low |

**Two key business takeaways:**
1. **Overtime is the biggest and cheapest lever**: it is the model's #1 driver
   (2.4×) and appears in all three departments. An overtime policy has the best
   cost/benefit.
2. **Low salary is concentrated in 3–4 specific roles** (Sales Rep, Lab
   Technician, Research Scientist, HR generalist). A global salary review is not
   needed: fixing those focal points captures most of the avoidable churn.

### How to use these recommendations with the model

- Cross them with the **scoring**: act first on the employees in these profiles
  whose `scoring_abandono ≥ threshold` (see `plan_retencion.xlsx`).
- **High-impact** profiles (high salary ⇒ high turnover cost) admit lower
  thresholds: `threshold_i = C_action / (r × impact_i)`.

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

## 🎯 Recomendaciones (por perfil)

> Recomendaciones lógicas surgidas del análisis exploratorio y del modelo
> predictivo (Regresión Logística, ROC AUC ≈ 0.80–0.83, PR-AUC ≈ 0.57).
> Complementan el scoring de abandono y el umbral de decisión.

### Drivers transversales del abandono (odds ratio del modelo)

| Factor de riesgo | Odds ratio |
|---|---|
| Horas extra = Sí | **2.40×** |
| Satisfacción entorno = Baja | 2.26× |
| Viajes frecuentes | 2.02× |
| Puesto Laboratory Technician | 1.93× |
| Puesto Sales Representative | 1.80× |
| Satisfacción trabajo = Baja | 1.76× |
| Satisfacción compañeros = Baja | 1.70× |
| Estado civil Soltero | 1.66× |
| Años desde última promoción (+1 DE) | 1.64× |
| Nº empresas anteriores (+1 DE) | 1.56× |

*Factores protectores:* sin viajes (0.48×), Research Director (0.58×), años con
el manager actual (0.59×).

**Patrón transversal:** horas extra + salario bajo + estancamiento (sin
promoción) + descontento, concentrado en puestos técnicos mal pagados.

### Sales — foco: Sales Representative

**Sales**: 446 empleados · fuga 20.6% · coste de rotación $1.33M/año.
**Foco caliente:** *Sales Representative* (83 personas, **39.8% de fuga**,
salario medio $2.579/mes, los peor pagados de la empresa).

| Señal | Leavers | Stayers / resto |
|---|---|---|
| Horas extra = Sí | 37.5% fuga | 13.8% fuga |
| Satisfacción trabajo = Baja | 53.6% fuga | 16.7% (Alta) |
| Implicación = Baja | 51.7% fuga | 16.2% (Alta) |
| Solteros | 34.6% fuga | 11.5% (Divorciados) |
| Salario medio | $5.908 | $7.232 |
| Antigüedad media | 5.5 años | 7.7 años |

**Acciones propuestas:**
1. **Rediseñar la compensación de Sales Representative**: plan de comisiones o
   bonus ligado a permanencia, o subir el piso salarial (hoy $2.579).
2. **Cortar horas extra**: repartir cartera/cuentas y revisar cuadrantes.
3. **Plan de carrera Rep → Executive** con ascenso definido a 18–24 meses
   (el estancamiento eleva el riesgo 1.64×).
4. **Mentoría para nuevos ingresos y solteros** y limitar viajes frecuentes.

**Ahorro potencial** (reduciendo la fuga un 30%): **$399.928/año** en Sales
($50.787 solo en Sales Representative).

### Research & Development — foco: Laboratory Technician y Research Scientist

**R&D**: 961 empleados · fuga 13.8% · coste de rotación $1.28M/año.
**Focos calientes:** *Laboratory Technician* (259, 23.9% fuga, $2.886) y
*Research Scientist* (292, 16.1% fuga, $2.888).

| Señal | Leavers | Stayers / resto |
|---|---|---|
| Horas extra = Sí | 27.3% fuga | 8.6% fuga |
| Satisfacción trabajo = Baja | 22.2% fuga | 5.1% (Muy_Alta) |
| Implicación = Baja | 23.5% fuga | 13.4% (Alta) |
| Salario medio | $4.108 | $6.630 (−38%) |
| Carrera Technical Degree | 1.66× riesgo | — |

**Acciones propuestas:**
1. **Revisar las bandas salariales de los técnicos** ($2.9k es muy bajo y la
   brecha leaver/stayer es del −38%): ajuste selectivo.
2. **Reducir horas extra de laboratorio** (motor nº1: 2.4×).
3. **Programa de engagement/mentoría** para implicación y entorno Bajos.
4. **Camino de promoción** Lab Technician → Research Scientist → Director
   (Research Director casi no se va: 0.58×).

**Ahorro potencial** (reduciendo la fuga un 30%): **$384.529/año** en R&D
($121.887 solo en Laboratory Technician).

### Human Resources — foco: rol HR generalista

**HR**: 63 empleados · fuga 19.0% · coste de rotación $104k/año.
**Foco caliente:** *rol HR generalista* (52, 23.1% fuga, $3.093); los Managers
de HR tienen **0% de fuga**.

| Señal | Leavers | Stayers / resto |
|---|---|---|
| Satisfacción entorno = Baja | 36.4% fuga | 7.7% (Alta) |
| Viajes frecuentes | 36.4% fuga | 17.4% (Rarely) |
| Satisfacción trabajo = Baja | 33.3% fuga | 13.9% (Alta) |
| Salario medio | $3.716 | $7.346 (**−49%**) |
| Antigüedad media | 4.2 años | 8.0 años |

**Acciones propuestas:**
1. **Equiparar la compensación** (la brecha del −49% es la mayor de toda la
   empresa y es insostenible).
2. **Mejorar clima/entorno** y reducir viajes frecuentes (36.4% de fuga).
3. **Onboarding + check-ins en los primeros 2 años** (se van temprano).

**Ahorro potencial** (reduciendo la fuga un 30%): **$31.245/año**.

### Priorización por ROI

| Acción | Perfil | Ahorro (fuga −30%) | Dificultad |
|---|---|---|---|
| Control de horas extra | Transversal (motor nº1, 2.4×) | alto, indirecto | Media |
| Ajuste bandas técnicos | R&D | $121.887 (Lab Tech) | Media |
| Compensación Sales Rep | Sales | $50.787 | Media |
| Compensación HR | HR | $31.245 | Baja |
| Plan de carrera Rep→Exec | Sales | parte de $399.928 | Baja |

**Dos conclusiones de negocio clave:**
1. **Las horas extra son el palo más grande y más barato de tocar**: es el
   driver nº1 del modelo (2.4×) y aparece en los tres departamentos. Una
   política de horas extra tiene el mejor coste/beneficio.
2. **El salario bajo se concentra en 3–4 roles concretos** (Sales Rep, Lab
   Technician, Research Scientist, HR generalista). No hace falta una revisión
   salarial global: basta corregir esos focos, que concentran la mayor parte
   del abandono evitable.

### Cómo usar estas recomendaciones junto al modelo

- Cruzar con el **scoring**: intervenir primero en los empleados de estos
  perfiles con `scoring_abandono ≥ umbral` (ver `plan_retencion.xlsx`).
- Los perfiles de **alto impacto** (salario alto ⇒ coste de rotación alto)
  admiten umbrales más bajos: `umbral_i = C_acción / (r × impacto_i)`.
