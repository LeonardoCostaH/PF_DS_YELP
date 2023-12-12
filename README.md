# Proyecto GeoGenesis Metadata

---

<p align=center><img src=files/img/Geogenesis_logo.png><p>

---

### INDICE

- [Presentacion GeoGenesis Metadata](#presentacion-geogenesis-metadata)
- [Conjunto y Fuente de Datos](#conjunto-y-fuente-de-datos)
- [Cliente](#cliente)
- [Objetivos](#objetivos)
- [Alcance](#alcance)
- [Workflow](#workflow)
- [Tecnologías](#tecnologías)
- [KPIS propuestos](#kpis-propuestos)
- [Desarrolladores](#desarrolladores)

---

## Presentacion GeoGenesis Metadata

Bienvenido a Geogenesis Metadata, tu socio estratégico en la creación y lanzamiento de proyectos hoteleros innovadores. Nos especializamos en ofrecer asesoramiento experto basado en un exhaustivo análisis de información geográfica y predicciones avanzadas de análisis de sentimiento.
En Geogenesis Metadata, nos destacamos por nuestra dedicación a la excelencia, nuestro enfoque innovador y nuestra capacidad para transformar datos en decisiones estratégicas. Al elegirnos como tu consultora de confianza, estás eligiendo la sinergia entre la precisión de la información geográfica y la inteligencia del análisis de sentimiento.

## Conjunto y Fuente de Datos

Lo que nos distingue es nuestra capacidad para extraer información valiosa de fuentes confiables como Yelp y Google Maps, así como de otras fuentes externas, para complementar y enriquecer nuestro trabajo. Esta integración de datos exhaustivos nos permite ofrecer análisis más completos y perspicaces, asegurando que cada proyecto hotelero se beneficie de una visión global y precisa. En Geogenesis, entendemos que cada cliente es único, y adaptamos nuestra experiencia y conocimientos para asegurar el éxito de cada proyecto hotelero que emprendemos.

## Cliente

Cadena hotelera en Estados Unidos que quiere mejorar servicios ya existentes
Nuestra consultora está diseñada específicamente para satisfacer las necesidades únicas y exigencias de aquellos que buscan lanzar, expandir o mejorar sus proyectos hoteleros. Trabajamos estrechamente con propietarios de hoteles, inversores y equipos de gestión, brindando asesoramiento estratégico respaldado por análisis geográficos detallados y pronósticos de análisis de sentimiento. En Geogenesis, entendemos que cada cliente es único, y adaptamos nuestra experiencia y conocimientos para asegurar el éxito de cada proyecto hotelero que emprendemos.

## Objetivos

- Objetivo principal: Desarrollar una herramienta de análisis para facilitar la mejora de hoteles existentes. Esta herramienta se basará en el análisis de opiniones de usuarios, las características específicas de los hoteles actuales y las atracciones turísticas populares en sus respectivas zonas.

## Alcance

- Recomendación de Locales Basada en Experiencias Anteriores
  Desarrollar un sistema de recomendación de restaurantes que utilice las experiencias anteriores de los usuarios en Yelp y Google Maps. Esto proporcionará a los usuarios sugerencias personalizadas para explorar nuevos lugares basados en sus preferencias y reseñas anteriores.
- Identificación de Ubicaciones Estratégicas para Nuevos Locales
  Utilizar datos geográficos y reseñas para identificar las ubicaciones más estratégicas para abrir nuevos locales de restaurantes y negocios afines en Estados Unidos. Esto optimizará la expansión de la cadena y maximizará su impacto.

### KPIS propuestos

- #### KPI 1: Aumentar el porcentaje de reseñas positivas (PRP) en un 2% cada 3 meses hasta alcanzar 90%.

  Fórmula:
  PRP = (Numero de reseñas positivas/Total de reseñas) * 100

  Descripción:
  El PRP calcula el porcentaje de reseñas que contienen sentimientos positivos en comparación con el total de reseñas. Proporciona una medida cuantitativa de la positividad de las experiencias compartidas por los clientes.

- #### KPI 2: Aumentar el índice de satisfacción de huéspedes (ISH) de EEUU en los próximos 6 meses en un 7%.

  Fórmula:
  ISH = (Cantidad de reseñas positivas de huéspedes de Estados Unidos / Total de reseñas positivas de huéspedes de Estados Unidos) * 100.

  Descripción:
  Este KPI se centra en mejorar la satisfacción de los huéspedes provenientes de Estados Unidos durante los próximos seis meses. El Índice de Satisfacción es una medida clave que refleja la calidad de la experiencia del cliente. La meta específica es lograr un aumento del 7% en el Índice de Satisfacción en comparación con el periodo actual.

- #### KPI 3: Mantener el índice de Respuestas a Reseñas Negativas (IRRN) por encima del 95%. 

  Fórmula:
  IRRN = (Reseñas negativas contestadas/Total de reseñas negativas) * 100

  Descripción:
  Este KPI se enfoca en la eficacia y prontitud de la gestión de respuestas a reseñas negativas. El Índice de Respuestas a Reseñas Negativas (IRRN) busca evaluar el compromiso y la capacidad de la organización para abordar de manera efectiva las preocupaciones expresadas por los clientes a través de reseñas negativas. La meta establecida es mantener este índice por encima del 95%, lo que indica un alto nivel de atención y respuesta a las experiencias negativas reportadas por los clientes

- #### KPI 4: Mantener el promedio mensual de sentimiento para huéspedes que vienen en familia por encima de 0.25.

  Fórmula:
  Suma de todos los valores de sentimiento / Cantidad de valores de sentimiento

  Descripción:
  El sentimiento es una métrica que mide el grado de satisfacción de las reseñas de los clientes. Es un número entre 1 y -1, siendo 1 muy satisfecho y -1 muy insatisfecho. Este KPI se centra en medir la percepción general de los huéspedes que vienen en familia, utilizando el análisis de sentimientos como indicador. El objetivo es mantener un promedio mensual de sentimiento positivo, representado por un valor superior a 0.25. Este KPI busca evaluar la satisfacción y experiencia general de las familias que eligen hospedarse, asegurando que el ambiente y los servicios proporcionados generen opiniones favorables para todo el grupo familiar.

---

## Workflow

<p align=center><img src=files/img/workflow.jpeg><p>

- Diccionario de Datos y DER: [Link diccionario](https://drive.google.com/drive/folders/1kuQy_BOdoovmRketR3T8dd2RiRuLq-Rt?usp=sharing)
 - ETL pipeline se encuentra [aqui](pipeline.md)
---

## Tecnologías

![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-badge?style=for-the-badge&logo=postgresql&logoColor=%234169E1&color=white)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)
![Canva](https://img.shields.io/badge/Canva-%2300C4CC.svg?style=for-the-badge&logo=Canva&logoColor=white)
![AWS](https://img.shields.io/badge/Amazon_AWS-badge?style=for-the-badge&logo=amazonaws&logoColor=black&labelColor=yellow&color=%23232F3E)
![Trello](https://img.shields.io/badge/Trello-badge?style=for-the-badge&logo=trello&logoColor=white&color=blue)
![Streamlit](https://img.shields.io/badge/Streamlit-badge?style=for-the-badge&logo=streamlit&logoColor=red&color=white)





---

## Desarrolladores

| Rol           | ![Linkedin](files/img/linkedin.png)                                              | ![Gmail](files/img/gmail.png)                                  | ![GitHub](files/img/github.png)                                     |
| ------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------------------------------------- |
| Data Enginner | [Melisa Arce](https://www.linkedin.com/in/melisaameliaarce/)                      | [melisaamelia.arce](mailto:melisaamelia.arce@gmail.com)         | [Melisa Arce](https://github.com/melisaameliaarce)                   |
| Data Enginner | [Luis Octavio Varas Jaime](https://www.linkedin.com/in/luis-o-varas/)             | [vluis2386](mailto:vluis2386@gmail.com)                         | [LuisOVaras](https://github.com/LuisOVaras)                          |
| Data Analyst  | [Leonardo Augusto Costa Hermes](https://linkedin.com/in/leonardo-costa-672a3a1b9) | [leonardocostahermes](mailto:leonardocostahermes@gmail.com)     | [LeonardoCostaH](https://gitHub.com/LeonardoCostaH/)                 |
| Data Analyst  | [Diego Saint Denis](https://www.linkedin.com/in/diego-saint-denis/)               | [diego.saintdenis](mailto:diego.saintdenis@gmail.com)           | [data-d-s-d](https://github.com/data-d-s-d)                          |
| Data Analyst  | [Joaquín Jullier](https://www.linkedin.com/in/joaqu%C3%ADn-jullier-6179a4266/)   | [julliercapellojoaquin](mailto:julliercapellojoaquin@gmail.com) | [JullierJoaquin](https://github.com/JullierJoaquin?tab=repositories) |

---
