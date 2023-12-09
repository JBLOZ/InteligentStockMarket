import constantes_variables as c
import random
import functions as f
import f_generic as g


def crearCuenta():
    g.linea(y=2)
    g.linea(c='¯')
    nombre_usuario = pedirNombre()
    nombre_usuario = comprobarUsuario(nombre_usuario)
    g.linea(c='¯')
    passw = pedirPassw()
    passw = comprobarPassw(passw,nombre_usuario)
    g.linea()
    g.linea(c='_')
    g.bienvenida(nombre_usuario,passw)
    g.linea(c='¯')
    g.linea(c='_')
    saveUserPassw(nombre_usuario,passw)
    g.linea(c='¯')

    pedirDatos()
    generaInfBancaria()
    

    return nombre_usuario, passw





def pedirNombre():
    nombre_usuario = input('Introduce un nombre de usuario: ')
    return nombre_usuario

def comprobarUsuario(nombre_usuario):

    while len(nombre_usuario) < 3 or nombre_usuario.capitalize() in c.informacion_clientes:

        if len(nombre_usuario) < 3:
            print('El nombre de usuario tiene que tener mas de 3 caracteres')
        else:
            print('Este nombre de usuario ya ha sido usado')

        g.linea(c='_')    
        nombre_usuario = pedirNombre()

    return nombre_usuario

def pedirPassw():
    passw = input('Introduce una contrasena para la cuenta: ')
    return passw


def comprobarPassw(passw,user):
    while len(passw) < 8 or not any(i.isupper() for i in passw) or not any(i.isdigit() for i in passw) or user.upper() in passw.upper():
        g.linea(c='_')

        if len(passw) < 8:
            print ('La contrasena debe de tener 8 o mas caracteres')
        if not any(i.isupper() for i in passw):
            print('La contrasena debe de tener almenos una mayuscula')
        if not any(i.isdigit() for i in passw):
            print ('La contrasena debe de tener al menos un numero')
        if user.upper() in passw.upper():
            print ('La contrasena no puede contener tu nombre de usuario')
        g.linea(c='¯')
        passw = pedirPassw()


    return passw


def saveUserPassw(user,passw):
    with open ('informacionUsuarios/contrasena.txt', 'ta') as passwtx:
        passwtx.write(passw + '\n')
     
    with open ('informacionUsuarios/user.txt', 'ta') as usertx:
        usertx.write(user + '\n')


def pedirDatos():
    print('DATOS PERSONALES')
    g.linea(c='¯')
    pide (x='nombre',y='Nombre: ',z=[3,10])
    pide (x='apellidos',y='Apellidos: ',z=[6,25])
    pide(x='DNI',y='DNI: ',z=[9,9],carc='ln')

    while not (g.comprobarStringCarcEsp(c.usuarioNuevo['DNI'][:8],nombre='DNI',tipo='n') and g.comprobarStringCarcEsp(c.usuarioNuevo['DNI'][8],nombre='DNI',tipo='l')):
        
        print('DNI no válido')
        c.usuarioNuevo['DNI'] = input('DNI: ')

        pide(x='DNI',y='DNI: ',z=[9,9],carc='ln',first=False)
    
    pide (x='telefono',y='Telefono: ',z=[9,9],carc='n')
    pide (x='email', y='Correo electronico: ', z=[5,35],carc='e')
    pide (x='CP', y='Codigo postal: ', z=[5,5],carc='n')
    pide (x='direccion', y='direccion: ', z=[6,30], carc='ln')
    guardarUserNuevo()
    print(c.usuarioNuevo['DNI'])

def pide(x,y,carc='l',z=None,first=True):

    if first:
        c.usuarioNuevo[x] = input(y).lower()

    while not g.comprobarStringCarcEsp(c.usuarioNuevo[x],long=z,tipo=carc):
        
        if x[-1] == 's':
            print(x.capitalize() + ' invalidos')
        else:
            print(x.capitalize() + ' no valido')
        g.linea(c='¯')

        c.usuarioNuevo[x] = input(y).lower()

    return c.usuarioNuevo[x]

##
##
##

def generaInfBancaria():
    with open ('informacionUsuarios/saldo.txt', 'ta') as saldotx:
        saldotx.write('0' + '\n')
    with open ('informacionUsuarios/numTargeta.txt', 'ta') as numTartx:
        numTartx.write(g.aleatorio(16) + '\n')
    with open ('informacionUsuarios/IBAN.txt', 'ta') as IBANtx:
        IBANtx.write('ES' + g.aleatorio(22) + '\n')

def guardarUserNuevo(user=c.usuarioNuevo):
    with open ('informacionUsuarios/nombreApellidos.txt', 'ta') as nApll:
        nApll.write(user['nombre'] + ' ' + user['apellidos'] + '\n')
    with open ('informacionUsuarios/DNI.txt', 'ta') as DNItx:
        DNItx.write(user['DNI'] + '\n')
    with open ('informacionUsuarios/telefono.txt', 'ta') as tel:
        tel.write(user['telefono'] + '\n')
    with open ('informacionUsuarios/email.txt', 'ta') as email:
        email.write(user['email'] + '\n')