# Predicción Eólica Fueguina

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

Este proyecto se centra en el análisis y modelado de datos meteorológicos obtenidos de la Estación Astronómica Río Grande (EARG), con el objetivo de desarrollar modelos de aprendizaje automático para predecir condiciones climáticas en la región de Tierra del Fuego.

## **Estructura del Proyecto**
El proyecto sigue una estructura organizada en carpetas, diseñada para almacenar y procesar los datos de manera eficiente. A continuación se describe la organización principal del repositorio:

- data/: Carpeta principal de datos del proyecto.
    - raw/: Contiene los datos originales y el script de scraping.

- notebooks/: Contiene notebooks de Jupyter con los análisis y modelos desarrollados.

- src/: Código fuente del proyecto, incluyendo funciones personalizadas y scripts de preprocesamiento y modelado.

## **Acceso a los Datos**
Los archivos de datos están organizados en la carpeta **data/raw**

## **Instalación y Ejecución**
**Clonar este repositorio:**
```
git clone https://github.com/never130/Politecnico_Malvinas-Proyecto_ML.git
cd Politecnico_Malvinas-Proyecto_ML
```
**Crear y activar un entorno virtual (opcional pero recomendado):**
```
python3 -m venv .venv
source .venv/bin/activate  # Para Linux/Mac
.venv\Scripts\activate     # Para Windows
```
**Instalar las dependencias:**
```
pip install -r requirements.txt
Ejecutar el análisis en los notebooks ubicados en notebooks/.
```

## Organizacion del Proyecto

```
├── LICENSE            <- Licencia de código abierto si se elige una
├── Makefile           <- Makefile con comandos de conveniencia como `make data` o `make train`
├── README.md          <- README de nivel superior para desarrolladores que utilizan este proyecto.
├── data
│   ├── external       <- Datos de fuentes de terceros.
│   ├── interim        <- Datos intermedios que han sido transformados.
│   ├── processed      <- Los conjuntos de datos finales y canónicos para modelado.
│   └── raw            <- La volcado original e inmutable de datos.
│       ├── scraping.py              <- Código para realizar el scraping de datos meteorológicos.
│       └── boletin_2016_01-2024_08.xlsx <- Archivo excel con los datos meteorológicos extraídos.
│       
├── docs               <- Documentacion del proyecto; ver www.mkdocs.org para más detalles
│
├── models             <- Modelos entrenados y serializados, predicciones de modelos o resúmenes de modelos
│
├── notebooks          <- Notebooks de Jupyter. La convención de nombres es un número (para ordenar),
│                         las iniciales del creador y una breve descripción delimitada por guiones, por ejemplo,
│                         `1.0-jqp-exploración-inicial-de-datos`.
│
├── pyproject.toml     <- Archivo de configuración del proyecto con metadatos del paquete para 
│                         prediccion_eolica y configuración para herramientas como black
│
├── references         <- Diccionarios de datos, manuales y otros materiales explicativos.
│
├── reports            <- Análisis generado como HTML, PDF, LaTeX, etc.
│   └── figures        <- Gráficos y figuras generados para ser utilizados en informes
│
├── requirements.txt   <- Archivo de requisitos para reproducir el entorno de análisis, por ejemplo,
│                         generado con `pip freeze > requirements.txt`
│
├── setup.cfg          <- Archivo de configuración para flake8
│
└── src   <- Código fuente para usar en este proyecto.
    │
    ├── __init__.py             <- Hace que prediccion_eolica sea un módulo de Python
    │
    ├── config.py               <- Almacena variables y configuraciones útiles
    │
    ├── dataset.py              <- Scripts para descargar o generar datos
    │
    ├── features.py             <- Código para crear características para modelado
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Código para ejecutar inferencias de modelos con modelos entrenados          
    │   └── train.py            <- Código para entrenar modelos
    │
    └── plots.py                <- Código para crear visualizaciones

```

--------

