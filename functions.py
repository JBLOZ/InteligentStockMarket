import constantes_variables as c
import random
import string
import re





def crearCuenta():
    
    nombre_usuario = pedirNombre()
    nombre_usuario = comprobarUsuario(nombre_usuario)
    passw = pedirPassw()
    passw = comprobarPassw(passw,nombre_usuario)
    bienvenida(nombre_usuario,passw)
    saveUserPassw(nombre_usuario,passw)
    pedirDatos()



    



    return nombre_usuario, passw



def pedirNombre():
    nombre_usuario = input('Introduce un nombre de usuario: ')
    return nombre_usuario



def comprobarUsuario(nombre_usuario):

    while len(nombre_usuario) < 3 or nombre_usuario.capitalize() in c.usuarios:

        if len(nombre_usuario) < 3:
            print('El nombre de usuario tiene que tener mas de 3 caracteres')
        else:
            print('Este nombre de usuario ya ha sido usado')    

        nombre_usuario = pedirNombre()

    return nombre_usuario


def pedirPassw():
    passw = input('Introduce una contrasena para la cuenta: ')
    return passw

def comprobarPassw(passw,user):
    while len(passw) < 8 or not any(i.isupper() for i in passw) or not any(i.isdigit() for i in passw) or user.upper() in passw.upper():

        if len(passw) < 8:
            print ('La contrasena debe de tener 8 o mas caracteres')
        if not any(i.isupper() for i in passw):
            print('La contrasena debe de tener almenos una mayuscula')
        if not any(i.isdigit() for i in passw):
            print ('La contrasena debe de tener al menos un numero')
        if user.upper() in passw.upper():
            print ('La contrasena no puede contener tu nombre de usuario')
        passw = pedirPassw()

    return passw

def bienvenida(user,passw):
    print('Bienvenido a Inteligent Stock Market ' + user + ', no comparta nunca su contrasena: ' + ocultarStrings(passw))



#Oculta la string que quieras con el carácter que quieras
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


def saveUserPassw(user,passw):
    c.contrasenas.append(passw) 
    c.usuarios.append(user)
    comprobarUserPassw(user,passw)

def comprobarUserPassw(user,passw):
    guardado = False
    if passw in c.contrasenas and user in c.usuarios:
        print('Hemos guardado tu usuario y contraseña')
        guardado = True
    else:
        print('No hemos podido guardar tu usuario y contraseña')
        guardado = False
    return guardado


def pedirDatos():
    c.usuarioNuevo['nombre'] = input('Nombre: ')
    print(c.usuarioNuevo['nombre'])
    comprobarStringCarcEsp(c.usuarioNuevo['nombre'])




    
def comprobarStringCarcEsp(strn,tipo = 'nombre'):
    for i in range (len(strn)):
        if ord(strn.lower[i]) > 97 and ord(strn[i]) < 122:
            pass
        else:
            print(tipo +' no es valido')

    return strn
        


comprobarStringCarcEsp(input(''))





def iniciarSesion(usuarios,contrasenas):
    usuario_iniciando=input('Introduce tu usuario: ')
    contrasena_iniciando=input('Introduce tu contrasena: ')
    posUs=1
    posCo=0
    
    if usuario_iniciando in usuarios:
        posUs = usuarios.index(usuario_iniciando)
        
        
    if contrasena_iniciando in contrasenas:
        posCo= contrasenas.index(contrasena_iniciando)
    
    if posUs == posCo:

        print('Correcto.')




def generar_contrasena():
    global contrasena_generada
    lista1 = ['pescado', 'mono', 'ajolote', 'gato']
    lista2 = ['88', '77', '34', '56']
    contrasena_generada = random.choice(lista1) + random.choice(lista2)
    print(contrasena_generada)
    return contrasena_generada

def cambiar_contrasena():
    while True:
        contrasena_usuario = input('Introduce la contrasena actual: ')
        if contrasena_usuario == contrasena_generada:
            nueva_contrasena = input('Introduce una nueva contrasena: ')
            if len(nueva_contrasena) >= 8 and any(i.isupper() for i in nueva_contrasena) and any(i.isdigit() for i in nueva_contrasena):
                print('Contrasena cambiada exitosamente.')
                return nueva_contrasena
            else:
                print('Nueva contrasena no valida. Asegurate de que cumple con los requisitos.')
        else:
            print('Contrasena incorrecta. Intenta nuevamente.')




