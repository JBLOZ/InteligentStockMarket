import constantes_variables as c
import f_generic as g
import crearCuenta as cc
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
        cc.crearCuenta()

    g.linea(y=2)
    g.linea(c='*')
        



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


