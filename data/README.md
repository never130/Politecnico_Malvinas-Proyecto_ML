# **Carpeta data**
Esta carpeta contiene todos los archivos de datos utilizados y generados en el proyecto Politecnico Malvinas - Proyecto ML. El objetivo de esta carpeta es organizar los datos necesarios para los análisis y modelos de predicción meteorológica realizados a partir del dataset de la Estación Astronómica Río Grande (EARG).

## **Estructura de la Carpeta**
La carpeta data está organizada en subdirectorios para facilitar el acceso y organización de los datos:

- raw/: Contiene los datos en su formato original, tal como fueron obtenidos mediante scraping del boletín meteorológico de la EARG.

    - boletin_2016_01-2024_08.xlsx: Archivo de Excel con registros meteorológicos diarios desde enero de 2016 hasta agosto de 2024.
      
    - scraping.ipynb: Script de Python utilizado para el scraping de los boletines meteorológicos de la EARG.

- processed/: Contiene los datos preprocesados y limpios para su posterior analisis y modelado.

    - datos_limpios.csv: Archivo csv limpio para el posterior modelo de machine learning.

    - datos procesados.csv: Archivo csv con los datos pre-procesados.

    - produccion_simulada_eolica.csv: Archivo csv con los datos limpios sumando los datos creados con la informacion y simulacion obtenida del parque eolico.

## **Acceso al Dataset**
El dataset meteorológico fue recopilado directamente de los boletines públicos disponibles en la página de la Estación Astronómica Río Grande (EARG), parte de la Universidad Nacional de La Plata.

**URL de referencia:** http://earg.fcaglp.unlp.edu.ar/meteorologia/boletin/

### **Informacion en cuanto a los datos recopilados del proyecto Parque Eolico de Tierra del Fuego**

**Fuente:** https://www.mejorenergia.com.ar/noticias/2023/10/03/1991-tierra-del-fuego-obtiene-un-prestamo-de-us-65-millones-para-la-construccion-de-un-parque-eolico

**Fuente:** https://www.tierradelfuego.gob.ar/wp-content/uploads/2023/08/Resumen-No-Tecnico-Parque-Eolico-0823-Espanol.pdf

-----

## Descripcion a los archivos del dataset

**Archivo boletin_2016_01-2024_08.xlsx**
Este archivo contiene las variables meteorológicas recogidas desde enero de 2016 hasta agosto de 2024, incluyendo datos sobre:

- Temperatura (media, máxima y mínima, con sus respectivas horas y minutos)
  
- Viento (dirección y ráfagas)

- Presión atmosférica

- Lluvia diaria

- Radiación solar y UV

  
Estos datos se almacenaron en formato Excel para facilitar su manejo y análisis en este proyecto.

