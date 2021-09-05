#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 00:44:59 2021

@author: martin
"""
def invertir_lista(lista):
    largo_lista = len(lista)
    invertida = [None]*largo_lista
    for posicion, valor in enumerate(lista): # Recorro la lista
        #agrego el elemento e al principio de la lista invertida
        indice = largo_lista - posicion - 1
        invertida[indice] = valor 
    return invertida

def propagar(lista):
    lista_propagada = lista.copy()
    longitud_lista = len(lista_propagada)-1
    for indice, estado_fosforo in zip(range(longitud_lista), lista_propagada):
        if estado_fosforo == 1 and lista_propagada[indice+1] != -1:
            lista_propagada[indice+1] = 1
    lista_propagada = invertir_lista(lista_propagada)
    
    # for indice, estado_fosforo in zip(range(longitud_lista), lista_propagada):
    #     if estado_fosforo == 1 and lista_propagada[indice+1] != -1:
    #         lista_propagada[indice+1] = 1
    # lista_propagada = invertir_lista(lista_propagada)
    return lista_propagada

lista = [ 0,0,0,1]
print("Lista original  : ",lista)
print("Lista propagada : ",propagar(lista))
