## Predicción de Abandono de Empleados: Un Modelo de Machine Learning

Este proyecto se centra en la creación de un modelo de machine learning para predecir la probabilidad de que un empleado abandone la empresa. El objetivo es identificar los factores que contribuyen al abandono y proporcionar a la empresa información valiosa para la toma de decisiones estratégicas.

### Datos

El conjunto de datos utilizado para entrenar el modelo se encuentra en los archivos `abandono_con_scoring.xlsx`, `abandono_con_scoring2.xlsx`, `AbandonoEmpleados.csv` y `df_abandono.csv`. Estos archivos contienen información sobre diversos aspectos de la vida laboral de los empleados, incluyendo:

* **Información personal:** Edad, estado civil, nivel educativo, carrera.
* **Información laboral:** Departamento, distancia al trabajo, nivel laboral, puesto, salario, horas extra, satisfacción con el trabajo, satisfacción con el entorno, años en la compañía, años desde la última promoción, años con el manager actual.
* **Impacto de abandono:** Impacto económico en caso de abandono del empleado.
* **Abandono:** Variable objetivo que indica si el empleado abandonó la empresa o no.

### Metodología

El proyecto se desarrolló siguiendo las siguientes etapas:

1. **Análisis Exploratorio de Datos:** Se realizó un análisis exhaustivo del conjunto de datos para comprender las variables, identificar patrones, relaciones y posibles outliers.
2. **Preprocesamiento de Datos:** Se limpiaron los datos, se trataron los valores faltantes, se codificaron las variables categóricas y se escalaron las variables numéricas.
3. **Selección de Características:** Se seleccionaron las variables más relevantes para el modelo utilizando técnicas de selección de características.
4. **Entrenamiento del Modelo:** Se entrenaron diferentes modelos de machine learning, incluyendo regresión logística, árboles de decisión y máquinas de vectores de soporte.
5. **Evaluación del Modelo:** Se evaluó el rendimiento de los modelos utilizando métricas como precisión, recall, F1-score y AUC.
6. **Scoring de Abandono:** Se desarrolló un sistema de scoring que asigna una puntuación a cada empleado, reflejando su probabilidad de abandono.

### Resultados

El modelo final seleccionado fue [Nombre del Modelo]. Este modelo logró un [Métrica de Rendimiento] de [Valor] en el conjunto de datos de prueba. Se proporciona un archivo con el scoring de abandono para cada empleado, permitiendo identificar aquellos con mayor riesgo de abandonar la empresa.

### Aplicaciones

Este proyecto tiene diversas aplicaciones prácticas para las empresas:

* **Retención de Empleados:**  Identificar a los empleados con alto riesgo de abandono para implementar medidas de retención personalizadas.
* **Optimización de Recursos:**  Priorizar las acciones de retención en los empleados con mayor impacto económico en caso de abandono.
* **Planificación Estratégica:**  Comprender los factores clave que impulsan el abandono para tomar decisiones estratégicas a nivel de gestión de recursos humanos.


Se puede observar el analisis terminado mediante el dashboard publicado en Tableau desde el siguiente link: https://public.tableau.com/app/profile/cesar.martin.gonzalez/viz/DashboardEmpleadosenRiesgo/Dashboard1

