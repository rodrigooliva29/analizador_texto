from leer_escribir_archivos import leer_archivo_texto, exportar_archivo_texto
import re
import collections
import os.path

nombre_archivo = "python.txt" #nombre del archivo a analizar
palabras = ("ciencia", "python","Python") #para funcion "encontrar_palabra"
letra = ("h") #para funcion "frecuencia_letra"
palabras1 = ("desarrollo","solo") #para funcion "frecuencia_palabras"

class AnalizadorDeTexto:

    """El constructor de la clase toma un argumento nombre_archivo el cual se va a analizar"""
    def __init__(self, nombre_archivo):
        """Crea dos atributos, nombre archivo y contenido, primero para reconocer el archivo y el otro para analizar el contenido"""
        self.nombre_archivo = nombre_archivo
        self.contenido = leer_archivo_texto(nombre_archivo)

    """Este metodo devuelve la extension del archivo a analizar, utilizando la funcion os.path.splitext()""" 
    def tipo_archivo(self):
        return os.path.splitext(self.nombre_archivo)[1]
    
    """Cuenta las veces que se repiten las palabras utilizando la clase collections.Counter"""
    def contador_palabras(self):
        contador = collections.Counter(self.contenido.split())
        return contador
    
    """Este metodo cuenta el total de palabras del texto utilizando re.findall para encontrar y luego contar"""
    def total_palabras(self):
        total = len(re.findall(r"\w+", self.contenido))
        return total
    
    """Este metodo busca una lista de palabras en el archivo y muestra si se encontraron o no"""
    def encontrar_palabra(self, palabras):
        try:
            resultados = ""
            for palabra in palabras:
                if re.search(palabra, self.contenido):
                    resultados += (f"La palabra '{palabra}' se encontro en el texto\n")
                else:
                    resultados += (f"La palabra '{palabra}' NO se encontro en el texto\n")
        except Exception as e:
            print(str(e))
        return resultados
    
    """Este metodo muestra las veces que se repiten las palabras especificadas e imprime un mensaje que indica la cantida de veces"""
    def frecuencia_palabra(self, palabras):
        try:
            frecuencia_palabras = ""
            for palabra in palabras:
                frecuencia = len(re.findall(palabra, self.contenido))
                if frecuencia == 0:
                    frecuencia_palabras += (f"\nLa palabra '{palabra}' aparece {frecuencia} veces en el texto, \nesta mal escrita o no existe revisar mayusculas-minusculas, redaccion, etc.")
                else:
                    frecuencia_palabras += (f"\nLa palabra '{palabra}' aparece {frecuencia} veces en el texto.")
        except (TypeError, NameError) as e:
            print(str(e))
        return frecuencia_palabras
    """Este metodo muestra las veces que se repiten la letra especificada e imprime un mensaje que indica la cantida de veces"""
    def frecuencia_letra(self, letra):
        try:
            frecuencia_letra = ""
            if len(letra) !=1:
                print("Inserte solo una letra")
            else:
                ocurrencias = len(re.findall(letra, self.contenido))
                if ocurrencias == 0:
                    frecuencia_letra += (f"\nLa letra '{letra}' aparece {ocurrencias} veces en el texto, esta mal escrita, no existe,\npuede revisar mayusculas-minusculas")
                else:
                    frecuencia_letra += (f"\nLa letra '{letra}' aparece {ocurrencias} veces en el texto.\n")
        except (NameError, TypeError):
            print("Error de TypeError o NameError")
        return frecuencia_letra
    
"""Este código verifica si el archivo se está ejecutando directamente o si se ha importado como un módulo en otro archivo"""
if __name__ == "__main__":
    
    analizador = AnalizadorDeTexto(nombre_archivo)
    tipo = analizador.tipo_archivo()
    contenido = leer_archivo_texto(nombre_archivo)
    contador = analizador.contador_palabras()
    total = analizador.total_palabras()
    palabra = analizador.encontrar_palabra(palabras)
    frecuencia_letra = analizador.frecuencia_letra(letra)
    frec_palabra = analizador.frecuencia_palabra(palabras1)

    exportar_archivo_texto("resultados.txt", 
                       (
                        f"La extension del archivo es: {tipo}\n"
                        f"\nContenido del Archivo: {contenido}\n"
                        f"\nEl total de palabras en este texto es: {total}\n"
                        f"\nCantidad de palabras una por una: {contador}\n"
                        f"\nSe encontraron las palabras especficadas:\n{palabra}"
                        f"\nLa frecuencia por palabras indicadas es: {frec_palabra}\n"
                        f"\nLa frecuencia por letra indicada es: {frecuencia_letra}"                                  
                       )
                       )
                        
