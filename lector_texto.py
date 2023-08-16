from leer_escribir_archivos import leer_archivo_texto, exportar_archivo_texto
import re
import collections
import os.path

nombre_archivo = "rorgfo.txt"

def tipo_de_archivo(nombre_archivo):
    return os.path.splitext(nombre_archivo)[1]

with open (nombre_archivo, "r") as archivo:
    contenido = archivo.read()
    palabras = contenido.split()

def contador_palabras(texto): 
    contador = collections.Counter(contenido.split())
    return contador

def total_palabras(texto):
    total = len(re.findall(r"\w+", texto))
    return total


def encontrar_palabra(palabras, texto):
    try:
        for palabra in palabras:
            if re.search(palabra,texto):
                print(f"La palabra '{palabra}' se encontro en el texto")
            else:
                print(f"La palabra '{palabra}' NO se encontro en el texto")
    except Exception as e:
        print(str(e))
    
texto = contenido
palabras = ("Python", "ciencia", "reduccion", "personal")

palabras1 = ("Python", "desarrollo", "cienciaa")
def frecuencia_palabra(palabra, texto):
    try:
        for palabra in palabras1:
            ocurrencias = len(re.findall(palabra, texto))
            if ocurrencias == 0:
                print(f"\nLa palabra '{palabra}' aparece {ocurrencias} veces en el texto, esta mal escrita o no existe\nrevisar mayusculas-minusculas, redaccion, etc.")
            else:
                print(f"\nLa palabra '{palabra}' aparece {ocurrencias} veces en el texto.")
    except (TypeError, NameError) as e:
        print(str(e))

palabra = "Python"
letra = "j"

def frecuencia_letra(letra, texto):
    try:
        ocurrencias = len(re.findall(letra, texto))
        if ocurrencias == 0:
            print(f"\nLa letra '{letra}' aparece {ocurrencias} veces en el texto, esta mal escrita, no existe,\npuede revisar mayusculas-minusculas")
        else:
            print(f"\nLa letra '{letra}' aparece {ocurrencias} veces en el texto.\n")
    except (NameError, TypeError):
        print("Error de TypeError o NameError")
    

print(f"\nTipo de Archivo: {tipo_de_archivo(str(nombre_archivo))}")
print(f"\nCont. Texto: {leer_archivo_texto((nombre_archivo))}")
print(f"\nContador de Palabras: {(contador_palabras(texto))}")
print(f"\nTotal palabras en este texto: {total_palabras((texto))}\n")
encontrar_palabra(palabras, texto)
frecuencia_palabra(palabras1, texto)
frecuencia_letra(letra, texto)




