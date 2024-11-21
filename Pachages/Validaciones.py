
#VALIDAR INT
def validar_numeros(string):
    bandera_sonNumeros = False
    for i in range(len(string)):
        numero = ord(string[i])
        if numero >= 48 and numero <= 57: 
            bandera_sonNumeros = True
        else:
            return False
    return bandera_sonNumeros

#VALIDAR STR
def validar_letra(string):
    if len(string) != 1:
        return False
    bandera_sonLetras = False
    for i in range(len(string)):
        letra = ord(string[i])
        if (letra >= 65 and letra <= 90) or (letra >= 97 and letra <= 122):
            bandera_sonLetras = True
        else:
            return False
    return bandera_sonLetras

