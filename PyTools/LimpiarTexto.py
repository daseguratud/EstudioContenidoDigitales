from .Parameters import Parameters
class LimpiarTexto:
    stopwords=""
    @staticmethod
    def Limpiar():
        lineas=Parameters.ReadAllLines("stopwords.csv")
        LimpiarTexto.stopwords = []
        for linea in lineas: 
            LimpiarTexto.stopwords.append(linea.replace("\n",""))
        print("->*********** Stopwords")
        print(LimpiarTexto.stopwords)
        Parameters.CreatePath(Parameters.contenidosLimpiosPath)
        Parameters.CreateFile(Parameters.getOutFileLimpios())
        Parameters.CopyFile(Parameters.getOutFileConsolidados(),Parameters.getOutFileLimpios())
        LimpiarTexto.__ProcessFileLines(LimpiarTexto.__LimpiaNumeros)
        LimpiarTexto.__ProcessFileLines(LimpiarTexto.__ToLower)
        LimpiarTexto.__ProcessFileLines(LimpiarTexto.__QuitaStopWords)
    @staticmethod
    def __ProcessFileLines(function):
        lineas=Parameters.ReadAllLines(Parameters.getOutFileLimpios())
        with open(Parameters.getOutFileLimpios(),'w+',encoding="utf-8") as destino:
            for linea in lineas:
                if(not linea.startswith('->')):
                    linea = function(linea)
                destino.write(linea)
    @staticmethod
    def __LimpiaNumeros(cadena):
        Numeros=['0','1','2','3','4','5','6','7','8','9','.']
        cadenaFinal=""
        for letra in cadena:
            try:
                Numeros.index(letra)
            except:
                cadenaFinal+=letra
        return cadenaFinal
    def __ToLower(cadena):       
        return str.lower(cadena)
    def __QuitaStopWords(cadena):        
        cadenaFinal = cadena
        for stopword in LimpiarTexto.stopwords:
            cadenaFinal=str.replace(cadenaFinal,stopword," ")
        return cadenaFinal