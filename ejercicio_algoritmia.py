def capitalizar_palabra(palabra):
    # * Comprobar que se este pasando un string
    if type(palabra) != str: 
        return "Se debe ingresar un string"
    
    # * Tomar la primera letra y volverla mayuscula
    letra_upper = palabra[0].upper()

    # * Concatenar el resto de las letras excepto la primera
    letra_upper += palabra[1:]

    # * Retornar la palabra capitalizada
    return letra_upper
    

print(capitalizar_palabra(55))