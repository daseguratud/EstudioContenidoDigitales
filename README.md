Archivos del proceso de analisis de contenidos de libros sobre fundamentos de sistemas digitales

main.py
    Script para el procesmiento de los contenidos recolectados.

Pytools

    Clases creadas poara el procesamiento de los archivos de los contenidos de los libros consultados.

    - Parameters.py
        Parametros necesarios para el experimento.

    - Consolidar.py
        Une los archivos de la carpeta de contenidos en unso solo y lo deja en la  carpeta de salida.

    - UnificarLenguaje.py
        Traduce las líneas del archivo consolidado. Depende del traductor de goolge en linea (pip install googletrans==4.0.0-rc1).

01_Contenidos

    Carpeta con los archivos de los contenidos de los libros consultados. El nombre del archivo es puesto con el siguiente patron: <indice>_<apellido primer autor>_<idioma en|es>.txt.

02_ContenidosTraducidos

    La carpeta contiene los archivos de contenidos en ingles, los archivos que originalmente estaban en español son traducidos por medio de googletrans.

03_ContenidosConsolidados

    En esta carpeta se encuentra un solo archivo consolidado con el contenido en ingles de todos los libros.

04_ContenidosLimpios

    En esta carpeta está el archivo resultado de procesar el archivo consolidado de todos los contenidos en ingles. Parte del proceso está convertir este contenido a minúsculas y retirar las palabras y caracteres registrados en el archivo "stopwords.csv" 