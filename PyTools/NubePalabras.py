from wordcloud import WordCloud
import matplotlib.pyplot as plt
from .Parameters import Parameters

class NubePalabras:
    @staticmethod
    def CrearNube():
        texto = Parameters.ReadAllText(Parameters.getOutFileLimpios())
        nube_palabras = WordCloud(
            width=800, height=400, 
            background_color='white', 
            colormap='viridis').generate(texto)
        frequencies = nube_palabras.words_        
        plt.figure(figsize=(10, 5))
        plt.imshow(nube_palabras, interpolation='bilinear')
        plt.axis('off')
        plt.show()
        Parameters.CreatePath(Parameters.nubePalabrasPath)
        Parameters.CreateFile(Parameters.getOutFileNubePalabrasFrec())
        Parameters.WriteAllText(Parameters.getOutFileNubePalabrasFrec(),str.join("\n",frequencies))
