class Parameters:
    inputPath = "./01_Contenidos/"
    outPath = "./02_ContenidosConsolidados/"
    outFile = "Contenidos.txt"
    @staticmethod
    def getOutFile(): 
        return f"{Parameters.outPath}{Parameters.outFile}"