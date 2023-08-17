from leer_escribir_archivos import leer_archivo_texto, exportar_archivo_texto, agregar_a_archivo
import re
import collections
import os.path

nombre_archivo = "python.txt" #nombre del archivo a analizar
palabras = ("ciencia", "python","Python") #para funcion "encontrar_palabra"
letra = ("h") #para funcion "frecuencia_letra"
palabras1 = (("desarrollo","solo")) #para funcion "frecuencia_palabras"

class AnalizadorDeTexto:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.contenido = leer_archivo_texto(nombre_archivo)
        
    def tipo_archivo(self):
        return os.path.splitext(self.nombre_archivo)[1]
    
    def contador_palabras(self):
        contador = collections.Counter(self.contenido.split())
        return contador
    
    def total_palabras(self):
        total = len(re.findall(r"\w+", contenido))
        return total
    
    def encontrar_palabra(self, palabras):
        try:
            resultados = ""
            for palabra in palabras:
                if re.search(palabra, self.contenido):
                    resultados += (f"La palabra '{palabra}' se encontro en el texto\n")
                else:
                    resultados += (f"La palabra '{palabra}' NO se encontro en el texto\n")
            return resultados
        except Exception as e:
            print(str(e))

    def frecuencia_palabra(self, palabras):
        try:
            frecuencia_palabras = ""
            for palabra in palabras:
                ocurrencias = len(re.findall(palabra, self.contenido))
                if ocurrencias == 0:
                    frecuencia_palabras += (f"\nLa palabra '{palabra}' aparece {ocurrencias} veces en el texto, \nesta mal escrita o no existe revisar mayusculas-minusculas, redaccion, etc.")
                else:
                    frecuencia_palabras += (f"\nLa palabra '{palabra}' aparece {ocurrencias} veces en el texto.")
            return frecuencia_palabras
        except (TypeError, NameError) as e:
            print(str(e))

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
            return frecuencia_letra
        except (NameError, TypeError):
            print("Error de TypeError o NameError")

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
                        
