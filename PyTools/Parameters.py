import os
import shutil
class Parameters:
    contenidosOriginalesPath = "./01_Contenidos/"
    contenidosTraducidosPath = "./02_ContenidosTraducidos/"
    contenidosUnificadosPath = "./03_ContenidosConsolidados/"
    contenidosLimpiosPath = "./04_ContenidosLimpios/"
    contenidosUnificadosFile = "Contenidos.txt"
    @staticmethod
    def getOutFileConsolidados(): 
        return f"{Parameters.contenidosUnificadosPath}{Parameters.contenidosUnificadosFile}"    
    @staticmethod
    def getOutFileTraducidos(): 
        return f"{Parameters.contenidosTraducidosPath}{Parameters.contenidosUnificadosFile}"    
    @staticmethod
    def getOutFileLimpios(): 
        return f"{Parameters.contenidosLimpiosPath}{Parameters.contenidosUnificadosFile}"
    @staticmethod
    def CreatePath(path):
        if not os.path.exists(path):
            os.makedirs(path)
    @staticmethod
    def CreateFile(name):
        if os.path.exists(name):
            os.remove(name)
    @staticmethod
    def CopyFile(Origen,Destino):
        shutil.copy(Origen,Destino)