

def capitalizar_palabra(palabra):
    # * Tomar la primera letra y vovler mayuscula
    letra_upper = palabra[0].upper()

    # * Concatenar el resto de las letras expecto la primera
    letra_upper += palabra[1:]

    # * Retornar la palabra capitalizada
    return letra_upper
    

print(capitalizar_palabra("python"))