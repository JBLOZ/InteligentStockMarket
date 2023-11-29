import constantes_variables as c
import random
import string
import re





def crearCuenta():
    enter(2)
    lineaAlta()
    nombre_usuario = pedirNombre()
    nombre_usuario = comprobarUsuario(nombre_usuario)
    lineaAlta()
    passw = pedirPassw()
    passw = comprobarPassw(passw,nombre_usuario)
    enter(2)
    bienvenida(nombre_usuario,passw)
    enter()
    lineaBaja()
    saveUserPassw(nombre_usuario,passw)
    lineaAlta()
    enter()
    lineaBaja()
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

        lineaBaja()    
        nombre_usuario = pedirNombre()

    return nombre_usuario


def pedirPassw():
    passw = input('Introduce una contrasena para la cuenta: ')
    return passw

def comprobarPassw(passw,user):
    while len(passw) < 8 or not any(i.isupper() for i in passw) or not any(i.isdigit() for i in passw) or user.upper() in passw.upper():
        lineaBaja()

        if len(passw) < 8:
            print ('La contrasena debe de tener 8 o mas caracteres')
        if not any(i.isupper() for i in passw):
            print('La contrasena debe de tener almenos una mayuscula')
        if not any(i.isdigit() for i in passw):
            print ('La contrasena debe de tener al menos un numero')
        if user.upper() in passw.upper():
            print ('La contrasena no puede contener tu nombre de usuario')
        lineaAlta()
        passw = pedirPassw()


    return passw

def bienvenida(user,passw):
    print('Bienvenido a Inteligent Stock Market ' + user + ', no comparta nunca su contrasena: ' + ocultarStrings(passw))

def bienvenida2(user):
    print('Bienvenido de nuevo ' + str(user) + 'a Inteligent Stock Market, te echabamos de menos')





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
    print('DATOS PERSONALES')
    lineaAlta()
    pide ('nombre','Nombre: ')
    pide ('apellidos','Apellidos: ')
    c.usuarioNuevo['DNI'] = input('DNI: ')
    while not comprobarStringCarcEsp(c.usuarioNuevo['DNI'],nombre='DNI',tipo='n',num=8): 
        pass
        


    
def pide(x='nombre', y='Nombre: '):
    c.usuarioNuevo[x] = input(y).capitalize()
    while not comprobarStringCarcEsp(c.usuarioNuevo[x]):
        lineaBaja()
        c.usuarioNuevo[x] = input(y).capitalize()

    return usuarioNuevo[x]
    
    



    
def comprobarStringCarcEsp(strn, nombre='nombre',tipo = 'l',num = None):
    if num == None:
        num = len(strn)
    
    valido = False
    for i in range(num):
        if tipo == 'l' and 97 <= ord(strn[i].lower()) <= 122:
            valido = True
            
        elif tipo == 'n' and 47 <= ord(strn[i]) <= 57:
            valido = True

        else:
            print(nombre + ' no válido')
            valido = False
            break

    return valido





def iniciarSesion(usuarios = c.usuarios,
                contrasenas = c.contrasenas,
                num_tarjeta = c.num_tarjeta,
                cantidad_dinero = c.cantidad_dinero,
                balance_mes = c.balance_mes,
                pin = c.pin,
                firma_digital = c.firma_digital):
    enter(2)
    lineaFlechas()
    enter(2)
    
    

    posiciones = False
    contrasenast = False
    usuariost = False
    

    while posiciones==False or contrasenast==False or usuariost==False:
        usuario_iniciando = input('Introduce el usuario para iniciar sesión: ')
        contrasena_iniciando = input('Introduce la contraseña para iniciar sesión: ')

        if usuario_iniciando in usuarios and contrasena_iniciando in contrasenas:
            posUs = usuarios.index(usuario_iniciando)
            posCo = contrasenas.index(contrasena_iniciando)
            
            if posUs == posCo:
                posiciones = True
                bienvenida2(c.usuarios[posUs])
                enter()
            else:
                print('Usuario o contraseña inválidos.')

            usuariost = True
            contrasenast = True
        else:
            print('Usuario o contraseña incorrectos.')


    return (num_tarjeta[posUs],cantidad_dinero[posUs],num_tarjeta[posUs],cantidad_dinero[posUs],balance_mes[posUs],pin[posUs],firma_digital[posUs])


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




def lineaBaja(x=1):
    for i in range (x):
        print('____________________________________________________________________________')

def lineaAlta(x=1):
    for i in range (x):
        print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')

def lineaFlechas(x=1):
    for i in range (x):
        print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')

def lineaAsterisco(x=1):
    for i in range (x):
        print('****************************************************************************')

def enter(x=1):
    for i in range (x):
        print('')
        
        
        

def iniciarSesion_crearCuenta():
    enter(2)
    lineaAsterisco()
    s = input("¿Desea Iniciar sesión o Registrarse? (i/r): ")

    if s=='i':
        iniciarSesion(c.usuarios,c.contrasenas)
        
    elif s=='r':
        crearCuenta()

    enter(2)
    lineaAsterisco()
        
def aleatorio(x):
    num=0
    for i in range(x):
        num=num + str(random.randint(0,9))

