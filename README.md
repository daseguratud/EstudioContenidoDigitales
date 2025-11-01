Archivos del proceso de analisis de contenidos de libros sobre fundamentos de sistemas digitales
main.py:
    Script para el procesmiento de los contenidos recolectados.
Pytools:
    Clases creadas poara el procesamiento de los archivos de los contenidos de los libros consultados.
    - Parameters.py: 
        Parametros necesarios para el experimento.
    - Consolidar.py:
        Une los archivos de la carpeta de contenidos en unso solo y lo deja en la  carpeta de salida.
    - UnificarLenguaje.py:
        Traduce las líneas del archivo consolidado. Depende del traductor de goolge en linea (pip install googletrans==4.0.0-rc1).
01_Contenidos:
    Carpeta con los archivos de los contenidos de los libros consultados.
02_ContenidosConsolidados:
    Carpeta con el archivo resultado de consolidar todos los archivos de contenidos de los libros consultados. Se crea despues de ejecutar main.py