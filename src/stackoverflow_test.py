# -*- coding: utf-8 -*-

from stackoverflow import *

################################################################
#  Funciones auxiliares
################################################################

def mostrar_numerados(registros):
    for n, e in enumerate(registros):
        print(n, "-", e)


################################################################
#  Funciones de test
################################################################

def test_leer_preguntas(preguntas):
    pass

def test_filtrar_por_anyo(preguntas):
    pass


def test_calcular_etiquetas(preguntas):
    pass


def test_calcular_preguntas_mejor_valoradas(preguntas):
    pass
    

def test_contar_etiquetas(preguntas):
    pass
    

def test_mostrar_distribucion_etiquetas(preguntas):
    pass
    
    
def test_calcular_palabras_clave(stopwords):
    pass


def test_contar_palabras_clave(preguntas, stopwords):
    pass

    
def test_agrupar_preguntas_por_anyo(preguntas):
    pass


def test_mostrar_evolucion_etiquetas(preguntas):
    pass


################################################################
#  Programa principal
################################################################
if __name__ == '__main__':
    pass
    #preguntas = leer_preguntas('../data/stackoverflow_python_questions.csv')
    # test_leer_preguntas(preguntas)
    # test_filtrar_por_anyo(preguntas)
    # test_calcular_etiquetas(preguntas)
    # test_calcular_preguntas_mejor_valoradas(preguntas)
    # test_contar_etiquetas(preguntas)
    # test_mostrar_distribucion_etiquetas(preguntas)
    # stopwords = lee_stopwords('./data/stopwords.txt')
    # test_calcular_palabras_clave(stopwords)
    # test_contar_palabras_clave(preguntas, stopwords)
    # test_agrupar_preguntas_por_anyo(preguntas)
    # test_mostrar_evolucion_etiquetas(preguntas)
