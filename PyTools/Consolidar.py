import os
from .Parameters import Parameters
class Consolidar:
    @staticmethod
    def UnirArchivos():
        nombreArchivos = Consolidar.__ListarArchivos()
        Consolidar.__ClearOutputPutFile()
        for nombreArchivo in nombreArchivos:
            with open(Parameters.contenidosOriginalesPath+nombreArchivo,'r') as archivo:
                contenido = f"\n->**********************************{nombreArchivo}\n{archivo.read()}"
                Consolidar.__AppendOutputFile(contenido)
    
    @staticmethod
    def __ListarArchivos():
        listado = os.listdir(Parameters.contenidosOriginalesPath)
        listado.sort()
        return listado
    @staticmethod
    def __AppendOutputFile(contenido):
        if not os.path.exists(Parameters.contenidosUnificadosPath):
            os.makedirs(Parameters.contenidosUnificadosPath)
        with open(Parameters.getOutFileConsolidados(),"a") as file:
            file.write(contenido)
    @staticmethod
    def __ClearOutputPutFile():
        Parameters.CreatePath(Parameters.contenidosUnificadosPath)
        Parameters.CreateFile(Parameters.getOutFileConsolidados())