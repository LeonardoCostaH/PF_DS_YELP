
# ETL Pipeline en AWS

---

## Descripción General
Este documento describe el ETL pipeline implementado en Amazon AWS para la transformación de datos. El proceso involucra el uso de servicios como S3, AWS Glue, y AWS Step Functions para orquestar y automatizar las tareas.

## Arquitectura del Pipeline
<p align=center><img src=files/img/pipeline.drawio.png><p>

La arquitectura consta de los siguientes componentes principales:

1. **S3 Bucket:** Se utiliza como almacenamiento de datos para las fuentes y destinos del pipeline.

2. **AWS Glue:**
   - **Data Catalog:** Almacena los metadatos de las tablas y bases de datos utilizadas en el pipeline.
   - **Crawlers:** Escanean y catalogan los datos en el Data Catalog.
   - **Jobs:** Realizan las transformaciones de datos utilizando un enfoque visual.

3. **AWS Step Functions:**
   - **Workflow:** Orquesta y programa la ejecución de los jobs de AWS Glue para una ejecución sin problemas del pipeline.

## Pasos del Pipeline

### 1. Almacenamiento en S3
Los datos de origen se almacenan en un bucket de S3. La estructura de los datos se organiza de la siguiente manera:

<p align=center><img src=files/img/etl1.jpeg><p>

### 2. Catalogación con AWS Glue Crawler
Los crawlers de AWS Glue se utilizan para descubrir y catalogar los datos almacenados en S3. Se ejecutan automáticamente para mantener actualizado el Data Catalog.

### 3. Creación de Base de Datos y Tablas en AWS Glue
Con los metadatos catalogados, se crean bases de datos y tablas en el Data Catalog de AWS Glue para representar la estructura de los datos.

### 4. Transformación con AWS Glue Jobs
Se implementan jobs de AWS Glue para realizar transformaciones en los datos. Estos jobs utilizan un enfoque visual para definir las operaciones de transformación.

<p align=center><img src=files/img/etl2.jpeg><p>

### 5. Orquestación con AWS Step Functions
Se crea un workflow en AWS Step Functions para orquestar la secuencia de ejecución de los jobs de AWS Glue. Esto garantiza una ejecución ordenada y sin errores del pipeline.

<p align=center><img src=files/img/pipeline1.jpeg><p>

## Monitoreo y Mantenimiento
Se establecen prácticas de monitoreo para supervisar el rendimiento del pipeline. Esto incluye el registro de eventos y el uso de las métricas proporcionadas por los servicios de AWS.

## Conclusiones
El ETL pipeline implementado en AWS proporciona una solución robusta y escalable para la transformación de datos. La combinación de S3, AWS Glue, y Step Functions permite una administración eficiente y automatizada del flujo de datos.
- A continuacion un video de la implementacion del pipeline:

- Click aqui ---> [![YouTube](https://img.shields.io/badge/YouTube-badge?style=for-the-badge&logo=youtube&logoColor=%23FF0000&color=black)](https://www.youtube.com/watch?v=2szowDhM7RQ&ab_channel=MelisaArce)

- Captura del final del proceso (se tarda un tiempo en aparecer las tablas transformadas)


<p align=center><img src=files/img/etl3.jpeg><p>



