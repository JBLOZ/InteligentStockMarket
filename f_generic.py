import constantes_variables as c
import random








def bienvenida(user,passw):
    print('Bienvenido a Inteligent Stock Market ' + user + ', no comparta nunca su contrasena: ' + ocultarStrings(passw))

def bienvenida2(user):
    print('Bienvenido de nuevo ' + str(user) + 'a Inteligent Stock Market, te echabamos de menos')

def linea(c='',y=1,x=80):
    linea = c
    for i in range (y):
        for i in range (x):
            linea = linea + c
        print(linea)
        linea = c






def ocultarStrings(strn, numCaract=None, caracter="*", posicion="aleatoria"):
    if numCaract is None:
        numCaract = len(strn) // 2

    nuevaStr = strn

    if posicion == "aleatoria":
        for i in range(numCaract):
            index = random.randint(0, len(nuevaStr) - 1)
            nuevaStr = nuevaStr[:index] + caracter + nuevaStr[index + 1:]
    else:

        if posicion == "final":
            nuevaStr = strn[:len(strn)-numCaract]  


        if posicion == "inicio":        
            nuevaStr = strn[numCaract:]
        for i in range(numCaract):
            nuevaStr = caracter + nuevaStr 

    return nuevaStr


def comprobarStringCarcEsp(strn, nombre='nombre',tipo = 'l',long = None):

    if long == None:
        long = [0,50]

    
    valido = False
    for i in range(len(strn)):
        if tipo == 'l' and (97 <= ord(strn[i].lower()) <= 122 or ord(strn[i].lower()) == 32):
            valido = True
            
        elif tipo == 'n' and 47 <= ord(strn[i]) <= 57:
            valido = True
        
        elif tipo == 'ln' and (47 <= ord(strn[i]) <= 57 or 97 <= ord(strn[i].lower()) <= 122 or ord(strn[i].lower()) == 32):
            valido = True

        else:           
            valido = False
            break
    if tipo == 'e' and '@' in strn and '.' in strn:
        valido = True

    if (long[0] <= len(strn) <= long[1]) and valido:
        valido = True
    else:
        valido = False

    return valido



def aleatorio(x):
    num=0
    for i in range(x):
        num=num + str(random.randint(0,9))
