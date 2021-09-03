frase = input('Ingrese frase:').split()
print(frase)
frase_traducida = ''
for palabra in frase:
    if (palabra[-2] == 'o' or palabra[-2] == 'O'):
        frase_traducida += palabra[0:-2] + 'e' + palabra[-1] + ' '
    else:
        frase_traducida += palabra + ' '

print(frase_traducida)

# TODO : fix punctuation marks