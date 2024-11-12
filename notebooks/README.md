# Notebooks
## La carpeta está organizado en los siguientes archivos:
- 01_datos_cargados.ipynb
- 02_datos_analisis.ipynb
- 03_datos_eolicos_simulados.ipynb
- 04_modelos.ipynb
   ## Archivos del Proyecto

### 1. `01_datos_cargados.ipynb` - **Exploración de los datos y carga inicial**
   - **Descripción**: Este notebook se encarga de cargar los datos desde el archivo CSV, realizar una revisión preliminar y preparar los datos para su análisis. Se revisan las primeras filas del conjunto de datos para verificar la estructura y detectar posibles anomalías.
   - **Pasos importantes**:
     - Carga de los datos.
     - Inspección inicial de las primeras filas.
     - Identificación de posibles valores nulos o inconsistentes.

### 2. `02_datos_analisis.ipynb` - **Análisis Exploratorio de Datos (EDA)**
   - **Descripción**: Este notebook realiza un análisis exploratorio más detallado del conjunto de datos. Se generan estadísticas descriptivas y gráficos para visualizar las relaciones entre las diferentes variables, como la temperatura, el viento y la producción de energía.
   - **Pasos importantes**:
     - Generación de estadísticas descriptivas.
     - Creación de gráficos de dispersión y diagramas de caja para identificar patrones y outliers.
     - Análisis de correlaciones entre las variables.

### 3. `03_datos_eolicos_simulados.ipynb` - **Simulación de la Producción Eólica**
   - **Descripción**: En este notebook, se simula la producción eólica utilizando una fórmula simplificada basada en el viento medio. Se crea una nueva columna en el conjunto de datos que representa la producción de energía eólica diaria según el viento medio.
   - **Pasos importantes**:
     - Cálculo de la producción diaria de energía eólica utilizando el viento medio.
     - Inspección de los primeros valores de la nueva columna.
     - Preparación de los datos para su uso en los modelos de predicción.

### 4. `04_modelos.ipynb` - **Entrenamiento y Evaluación de Modelos**
   - **Descripción**: Este notebook entrena varios modelos de aprendizaje automático para predecir la producción de energía eólica diaria. Se entrenan modelos de regresión lineal, SVM (Support Vector Machine) y árbol de decisión, y se evalúan con métricas como el error cuadrático medio (MSE) y el coeficiente de determinación (R²).
   - **Pasos importantes**:
     - Entrenamiento de modelos de regresión lineal, SVM y árbol de decisión.
     - Evaluación de la precisión de los modelos utilizando métricas estándar.
     - Comparación de los resultados mediante gráficos de dispersión y predicciones.