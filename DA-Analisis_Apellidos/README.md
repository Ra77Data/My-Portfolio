### Análisis de la Distribución de Apellidos en Argentina

El proyecto en este repositorio analiza y visualiza la distribución geográfica de los apellidos más comunes en Argentina.

### Funcionalidad

1. **Carga de datos:** Importa un conjunto de datos con información sobre la frecuencia de los apellidos en cada provincia argentina.
2. **Procesamiento de datos:**
    - Agrupa los datos por provincia y apellido, calculando el porcentaje promedio de la población que lleva cada apellido en cada provincia.
    - Filtra los datos para mostrar la distribución de un apellido específico (por ejemplo, "González").
3. **Visualización:**
    - Genera mapas de calor que muestran la distribución geográfica de los apellidos. 
    - Se crean dos tipos de mapas:
        - Uno que muestra la frecuencia del apellido en relación con la población local de cada provincia.
        - Otro que muestra la cantidad total de personas con el apellido en cada provincia.
4. **Interpretación:**  Permite analizar las diferencias en la distribución de apellidos a nivel nacional y regional.

### Archivos

* `dist_apellidos_arg_ii.py`:  Script principal de Python.
* `apellidos_mas_frecuentes_provincia.csv`:  Dataset con la frecuencia de apellidos por provincia. 
* `apellidos_cantidad_personas_provincia.csv`: Dataset con la cantidad de personas por apellido en cada provincia.
* `argentina-with-regions_1413.geojson`: Archivo GeoJSON con la información geográfica de las provincias argentinas.





