from .Parameters import Parameters
import os

class UnificarLenguaje:
    @staticmethod
    def Traducir():
        archivosOriginales = os.listdir(Parameters.contenidosOriginalesPath)
        for archivo in archivosOriginales:
            print(archivo)
            
    @staticmethod
    def __ProcessFileLine(linea):
        try:          
            return linea
        except Exception as ex:            
            print(ex)