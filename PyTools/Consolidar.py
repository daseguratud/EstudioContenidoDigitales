import os
from .Parameters import Parameters
class Consolidar:
    
    def UnirArchivos(self):
        nombreArchivos = self.__ListarArchivos()
        self.__ClearOutputPutFile()
        for nombreArchivo in nombreArchivos:
            with open(Parameters.inputPath+nombreArchivo,'r') as archivo:
                contenido = f"->**********************************{nombreArchivo}\n{archivo.read()}"
                self.__AppendOutputFile(contenido)

    def __ListarArchivos(self):
        listado = os.listdir(Parameters.inputPath)
        listado.sort()
        return listado
    def __AppendOutputFile(self, contenido):
        if not os.path.exists(Parameters.outPath):
            os.makedirs(Parameters.outPath)
        with open(Parameters.getOutFile(),"a") as file:
            file.write(contenido)
    def __ClearOutputPutFile(self):
        if not os.path.exists(Parameters.outPath):
            os.makedirs(Parameters.outPath)
        if os.path.exists(Parameters.getOutFile()):
            os.remove(Parameters.getOutFile())
