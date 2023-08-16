from leer_escribir_archivos import leer_archivo_texto
import re
import collections
import os.path

class AnalizadorDeTexto:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.contenido = leer_archivo_texto(nombre_archivo)
        with open (self.nombre_archivo, "r") as archivo:
            self.contenido = archivo.read()
            self.palabras = self.contenido.split()
              
    def tipo_archivo(self):
        return os.path.splitext(self.nombre_archivo)[1]
           
    def contador_palabras(self):
        #palabras = self.leer_archivo()
        contador = collections.Counter(self.contenido.split())
        return contador
    
    def total_palabras(self):
        total = len(re.findall(r"\w+", contenido))
        return total
    
    def encontrar_palabra(self, palabras):
        try:
            for palabra in palabras:
                if re.search(palabra, self.contenido):
                    print(f"La palabra '{palabra}' se encontro en el texto")
                else:
                    print(f"La palabra '{palabra}' NO se encontro en el texto")
        except Exception as e:
            print(str(e))

    def frecuencia_palabra(self, palabras):
        try:
            for palabra in palabras:
                ocurrencias = len(re.findall(palabra, self.contenido))
                if ocurrencias == 0:
                    print(f"\nLa palabra '{palabra}' aparece {ocurrencias} veces en el texto, esta mal escrita o no existe\nrevisar mayusculas-minusculas, redaccion, etc.")
                else:
                    print(f"\nLa palabra '{palabra}' aparece {ocurrencias} veces en el texto.")
        except (TypeError, NameError) as e:
            print(str(e))

    def frecuencia_letra(self, letra):
        try:
            if len(letra) !=1:
                print("Inserte solo una letra")
            else:
            #texto = ' '.join(self.leer_archivo())
                ocurrencias = len(re.findall(letra, self.contenido))
                if ocurrencias == 0:
                    print(f"\nLa letra '{letra}' aparece {ocurrencias} veces en el texto, esta mal escrita, no existe,\npuede revisar mayusculas-minusculas")
                else:
                    print(f"\nLa letra '{letra}' aparece {ocurrencias} veces en el texto.\n")
        except (NameError, TypeError):
            print("Error de TypeError o NameError")

analizador = AnalizadorDeTexto("roro.txt")

tipo= analizador.tipo_archivo()
print(f"Tipo de Archivo: {tipo}""\n")

contenido = leer_archivo_texto("roro.txt")
print(contenido)

contador = analizador.contador_palabras()
print(contador)

total = analizador.total_palabras()
print(f"El total de palabras en este texto es {total}""\n")

encontrar_palabras = analizador.encontrar_palabra(("ciencia", "python","Python"))
print(encontrar_palabras)

frecuencia_palabras = analizador.frecuencia_palabra(("Cienciea","solo"))
print(frecuencia_palabras)

frecuencia_letra = analizador.frecuencia_letra(("h"))
print(frecuencia_letra)
"""

palabras = analizador.leer_archivo()
print(f"Palabras: {palabras}")
contador = analizador.contador_palabras()
print(f"Contador de palabras: {contador}")
total = analizador.total_palabras()
print(f"Total de palabras: {total}")
analizador.encontrar_palabra(["Python", "ciencia", "reduccion", "personal"])
analizador.frecuencia_palabra("Python")
analizador.frecuencia_letra("j")
"""