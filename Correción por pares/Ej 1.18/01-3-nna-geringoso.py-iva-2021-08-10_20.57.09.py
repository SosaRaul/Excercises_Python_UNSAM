# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 20:45:05 2021

@author: Ivanna Stefanía Obregón Arce
"""

cadena = input('Ingrese cadena: ')
capadepenapa = ''

for i in cadena:
    if i in 'aeiou':
        capadepenapa = capadepenapa + i + 'p' + i
    else:
        capadepenapa += i
        
print(capadepenapa)