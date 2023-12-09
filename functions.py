import constantes_variables as c
import f_generic as g
import random
import string
import re



def iniciarSesion_crearCuenta():
    g.linea(y=2)
    g.linea(c='*')
    s = input("¿Desea Iniciar sesión o Registrarse? (i/r): ")

    if s=='i':
        iniciarSesion(c.informacion_clientes)
        
    elif s=='r':
        crearCuenta()

    g.linea(y=2)
    g.linea(c='*')
        
########################################################################################
########################################################################################

def iniciarSesion(informacion_clientes):
    compru=False

    usuario_iniciando = input('Introduce el usuario para iniciar sesión: ')
    contrasena_iniciando = input('Introduce la contraseña para iniciar sesión: ')
    

    for cliente in informacion_clientes:
        if cliente['usuario'] == usuario_iniciando and cliente['contraseña'] == contrasena_iniciando:
            print("Información del usuario:")
            compru=True
                
            for clave, valor in cliente.items():
                print(f"{clave}: {valor}")
                
        print('Usuario o contraseña incorrectos.')

    return cliente




def menu(informacion_clientes):
    print('Menú de opciones:')
    print('1. Ingresar dinero.')
    print('2. Sacar dinero.')
    print('3. Transferir dinero.')
    mal=False

    while mal==False:
        opcion=int(input('Elige una opción: '))
        if opcion==1:
            op1(informacion_clientes)
        elif opcion==2:
            op2(informacion_clientes)

        elif opcion==3:
            op3(informacion_clientes)
        else:
            print('Opción incorrecta.')

########################################################################################



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


########################################################################################
########################################################################################


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


########################################################################################

def saveUserPassw(user,passw):
    with open ('informacionUsuarios/contrasena.txt', 'ta') as passwtx:
        passwtx.write(passw + '\n')
     
    with open ('informacionUsuarios/user.txt', 'ta') as usertx:
        usertx.write(user + '\n')


########################################################################################




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

    



def guardarUserNuevo(user=c.usuarioNuevo):
    with open ('informacionUsuarios/nombreApellidos.txt', 'ta') as nApll:
        nApll.write(user['nombre'] + ' ' + user['apellidos'] + '\n')
    with open ('informacionUsuarios/DNI.txt', 'ta') as DNItx:
        DNItx.write(user['DNI'] + '\n')
    with open ('informacionUsuarios/telefono.txt', 'ta') as tel:
        tel.write(user['telefono'] + '\n')
    with open ('informacionUsuarios/email.txt', 'ta') as email:
        email.write(user['email'] + '\n')
        

    

    
    

    
        

    
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
    
    

def generaInfBancaria():
    with open ('informacionUsuarios/saldo.txt', 'ta') as saldotx:
        saldotx.write('0' + '\n')
    with open ('informacionUsuarios/numTargeta.txt', 'ta') as numTartx:
        numTartx.write(g.aleatorio(16) + '\n')
    with open ('informacionUsuarios/IBAN.txt', 'ta') as IBANtx:
        IBANtx.write('ES' + g.aleatorio(22) + '\n')


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




            
        
        
        





def ingreso(informacion_clientes,cliente):
    ingreso= int(input('Introduce la cantidad a ingresar: '))
    informacion_clientes[cliente]['saldo'] = int(informacion_clientes[cliente]['saldo']) + ingreso
    informacion_clientes[cliente]['balance del mes']= int(informacion_clientes[cliente]['balance del mes']) + ingreso
    print(f"Usuario: {informacion_clientes[cliente]['usuario']}")
    print(f"Saldo: {informacion_clientes[cliente]['saldo']}")
    print(f"Balance del mes: {informacion_clientes[cliente]['balance del mes']}")
    mal=True

def op1 (informacion_clientes):
    cliente = int(input('Introduce el número de cliente: '))
    if cliente < 0 or cliente >= len(informacion_clientes):
        print('Número de usuario inexistente.')
    else:
        ingreso(informacion_clientes,cliente)
        
def sacade(informacion_clientes,cliente,sacado):
    informacion_clientes[cliente]['saldo'] = int(informacion_clientes[cliente]['saldo']) - sacado
    informacion_clientes[cliente]['balance del mes']= int(informacion_clientes[cliente]['balance del mes']) - sacado
    print(f"Usuario: {informacion_clientes[cliente]['usuario']}")
    print(f"Saldo: {informacion_clientes[cliente]['saldo']}")
    print(f"Balance del mes: {informacion_clientes[cliente]['balance del mes']}")
    mal=True       
        
def op2 (informacion_clientes):
    cliente = int(input('Introduce el número de cliente: '))
    if cliente<0 or cliente>=len(informacion_clientes):
        print('Número de usuario inexistente.')
    else:
        sacado= int(input('Introduce la cantidad a sacar: '))
        if sacado<=int(informacion_clientes[cliente]['saldo']):
            if sacado >= int(informacion_clientes[cliente]['saldo'])/2:
                print('Disculpa pero al intentar sacar una cantidad que iguala o supera el 50% de dinero de tu cuenta necesitamos una confirmación.')
                comprobacion_contrasena=input('Introduce tu contraseña porfavor: ')
                if comprobacion_contrasena==informacion_clientes[cliente]['contraseña']:
                    sacade(informacion_clientes,cliente,sacado)
                else:
                    print('Contraseña incorrecta.')
            else:
                sacade(informacion_clientes,cliente,sacado)
        else:
            print('Fondos insuficientes.')

def cliente1_cliente2 (informacion_clientes,cliente1,sacado):
    cliente2=int(input('Introduce el número de quién recibe el dinero: '))
    informacion_clientes[cliente1]['saldo'] = int(informacion_clientes[cliente1]['saldo']) - sacado
    informacion_clientes[cliente1]['balance del mes']= int(informacion_clientes[cliente1]['balance del mes']) - sacado
    informacion_clientes[cliente2]['saldo']= int(informacion_clientes[cliente2]['saldo']) + sacado
    informacion_clientes[cliente2]['balance del mes']= int(informacion_clientes[cliente2]['balance del mes']) + sacado
    g.linea(str='*')    
    print('Estado de la cuenta del que ha ingresado: ')
    print(f"Usuario: {informacion_clientes[cliente1]['usuario']}")
    print(f"Saldo: {informacion_clientes[cliente1]['saldo']}")
    print(f"Balance del mes: {informacion_clientes[cliente1]['balance del mes']}")
    g.linea(str='*')    
    print('Estado de la cuenta del que recibe el dinero: ')
    print(f"Usuario: {informacion_clientes[cliente2]['usuario']}")
    print(f"Saldo: {informacion_clientes[cliente2]['saldo']}")
    print(f"Balance del mes: {informacion_clientes[cliente2]['balance del mes']}")
    mal=True

def op3 (informacion_clientes):
    cliente1=int(input('Introduce el número de quién ingresa el dinero: '))
    if cliente1 < 0 or cliente1 >= len(informacion_clientes):
        print('Número de usuario inexistente.')
    else:
        sacado=int(input('Introduce el dinero que se va a transferir: '))
        if sacado<=int(informacion_clientes[cliente1]['saldo']):
            if sacado >= int(informacion_clientes[cliente1]['saldo'])/2:
                print('Disculpa pero al intentar sacar una cantidad que iguala o supera el 50% de dinero de tu cuenta necesitamos una confirmación.')
                comprobacion_contrasena=input('Introduce tu contraseña porfavor: ')
                if comprobacion_contrasena==informacion_clientes[cliente1]['contraseña']:
                    cliente1_cliente2(informacion_clientes,cliente1,sacado)
                else:
                    print('Contraseña incorrecta.')
            else:
                cliente1_cliente2(informacion_clientes,cliente1,sacado)
        else:
            print('Fondos insuficientes')


