import constantes_variables as c
import f_generic as g
import crearCuenta as cc
import random




def iniciarSesion_crearCuenta():

    salir = False

    while not salir:
        c.salgo = False
        c.leerArchivos()
        g.linea(y=2)
        g.linea(c='*')
        s = input("¿Desea Iniciar sesión, Registrarse o Salir? (i/r/s): ")

        if s=='i':
            
            cliente = iniciarSesion(c.informacion_clientes)
            if cliente != None:
                menu (cliente)


        elif s=='r':
            cc.crearCuenta()
        
        elif s=='s':

            g.linea(y=2)
            g.linea(c='*')
            salir = True
        



def iniciarSesion(informacion_clientes):
    

    n = 0
    
    while n < 3:

        usuario_iniciando = input('Introduce el usuario para iniciar sesión: ')
        contrasena_iniciando = input('Introduce la contraseña para iniciar sesión: ')

        for i in range (len(informacion_clientes['usuario'])):
            if informacion_clientes['usuario'][i] == usuario_iniciando and informacion_clientes['contraseña'][i] == contrasena_iniciando:
                cliente = i

                print("INFORMACION DEL USUARIO:")
                infoCuenta(cliente)
                g.linea('*',y=2)

                return cliente
     
        print('Usuario o contraseña incorrectos.')
        g.linea('<>',x=39)
        n = n + 1

    return None


                
                


def infoCuenta(cliente,oculto=True):
    print(c.informacion_clientes['nombreApellidos'][cliente].upper())
    g.linea()
    print('USUARIO: ' + c.informacion_clientes['usuario'][cliente])
    print('CONTRASEÑA: ' + g.ocultarStrings(c.informacion_clientes['contraseña'][cliente]))
    print('SALDO: ' + c.informacion_clientes['saldo'][cliente] + '€')
    if oculto:
        print('NUMERO DE TARJETA: ' + g.ocultarStrings(c.informacion_clientes['numero de tarjeta'][cliente],posicion='inicio',numCaract=12))
        print('IBAN: ' + g.ocultarStrings(c.informacion_clientes['IBAN'][cliente],posicion='inicio',numCaract=18))
    else:
        print('NUMERO DE TARJETA: ' +c.informacion_clientes['numero de tarjeta'][cliente])
        print('IBAN: ' + c.informacion_clientes['IBAN'][cliente])
        
    print('BALANCE DEL MES: ' + str(c.informacion_clientes['balance del mes'][cliente]) + '€')
    




def menu(cliente,informacion_clientes=c.informacion_clientes):
   
    print(c.salgo)

    while c.salgo==False:
        c.escribir_en_archivos()
        print('Menú de opciones:')
        print('1. Ingresar dinero.')
        print('2. Sacar dinero.')
        print('3. Transferir dinero.')
        print('4. Informacion de la cuenta')
        print('5. Cambiar contraseña')
        print('S. Salir')
        g.linea('_')
        opcion=input('Elige una opción: ')
        g.linea()
        if opcion=='1':
            op1_ingreso(informacion_clientes,cliente)
        elif opcion=='2':
            op2(informacion_clientes,cliente)

        elif opcion=='3':
            op3(informacion_clientes,cliente)
        elif opcion=='4':

            sensible = input('Desea ver informacion sensible de la cuenta como el numero de cuenta? (s/n)')
            if sensible == 's':
                n = 0
                while n < 3:

                    passw = input('Introduce tu contraseña porfavor: ')
                    while passw != informacion_clientes['contraseña'][cliente]:
                        print('Contraseña incorrecta.')
                        passw=input('Introduce tu contraseña porfavor: ')
                        n = n + 1
                    infoCuenta(cliente,oculto=False)
                iniciarSesion_crearCuenta()
            else:
                infoCuenta(cliente,oculto=True)


        elif opcion == '5':
            cambiar_contrasena(cliente)

        elif opcion.upper() == 'S':

            salir = True

        else:
            print('Opción incorrecta.')
    return



def cambiar_contrasena(cliente):
   passw = cc.pedirPassw()
   print(cliente)
   passw = cc.comprobarPassw(passw,c.informacion_clientes['usuario'][cliente])
   c.informacion_clientes['contraseña'][cliente] = passw




            
        
        
        






def op1_ingreso(informacion_clientes,cliente):
    ingreso= int(input('Introduce la cantidad a ingresar: '))

    informacion_clientes['saldo'][cliente] = int(informacion_clientes['saldo'][cliente]) + ingreso
    informacion_clientes['balance del mes'][cliente]= int(informacion_clientes['balance del mes'][cliente]) + ingreso

    print(f"Usuario: {informacion_clientes['usuario'][cliente]}")
    print(f"Saldo: {informacion_clientes['saldo'][cliente]}")
    print(f"Balance del mes: {informacion_clientes['balance del mes'][cliente]}")
    g.linea()
    
    



        
def sacar(informacion_clientes,cliente,sacado):
    informacion_clientes['saldo'][cliente] = int(informacion_clientes['saldo'][cliente]) - sacado
    informacion_clientes['balance del mes'][cliente]= int(informacion_clientes['balance del mes'][cliente]) - sacado

    print(f"Usuario: {informacion_clientes['usuario'][cliente]}")
    print(f"Saldo: {informacion_clientes['saldo'][cliente]}")
    print(f"Balance del mes: {informacion_clientes['balance del mes'][cliente]}")
    g.linea()
    
           
        
def op2 (informacion_clientes,cliente):
    
   
    sacado= int(input('Introduce la cantidad a sacar: '))
    while not (sacado<=int(informacion_clientes['saldo'][cliente])):
        sacado= int(input('Introduce una cantidad menor a tu saldo de ' + str(informacion_clientes['saldo'][cliente]) + '€: '))

    if sacado >= int(informacion_clientes['saldo'][cliente])/2:
        print('Disculpa pero al intentar sacar una cantidad que iguala o supera el 50% de dinero de tu cuenta necesitamos una confirmación.')
        passw=input('Introduce tu contraseña porfavor: ')
        n = 0

        while passw!=informacion_clientes['contraseña'][cliente]:
            print('Contraseña incorrecta.')
            if n == 3:
                print('Volveras a la pagina de inicio de sesion para la mayor seguridad de tu cuenta')
                g.linea('_')
                c.salgo = True
                return 
            
            passw = input('Introduce tu contraseña porfavor: ')

            n = n + 1
            

        
        sacar(informacion_clientes,cliente,sacado)
        
            
    else:
        sacar(informacion_clientes,cliente,sacado)
        
    


def traspaso (informacion_clientes,cliente,cobrador,sacado):
    
    informacion_clientes['saldo'][cliente] = int(informacion_clientes['saldo'][cliente]) - sacado
    informacion_clientes['balance del mes'][cliente]= int(informacion_clientes['balance del mes'][cliente]) - sacado


    informacion_clientes['saldo'][cobrador]= int(informacion_clientes['saldo'][cobrador]) + sacado
    informacion_clientes['balance del mes'][cobrador]= int(informacion_clientes['balance del mes'][cobrador]) + sacado

    g.linea('*')    
    print('ESTADISTICAS DE TU CUENTA: ')
    print(f"Usuario: {informacion_clientes['usuario'][cliente]}")
    print(f"Saldo: {informacion_clientes['saldo'][cliente]}")
    print(f"Balance del mes: {informacion_clientes['balance del mes'][cliente]}")
    g.linea('*') 

    return   

    

def op3 (informacion_clientes,cliente):

    cobrador = bizumTransferencia()
    sacado=int(input('Introduce el dinero que se va a transferir: '))
    while not (sacado<=int(informacion_clientes['saldo'][cliente])):
        print('Fondos insuficientes')
        sacado=int(input('Vuelva a introducir el importe, siempre menor a su saldo de '+ str(informacion_clientes['saldo'][cliente])+ '€: '))


    if sacado >= int(informacion_clientes['saldo'][cliente])/2:
        print('Disculpa pero al intentar sacar una cantidad que iguala o supera el 50% de dinero de tu cuenta necesitamos una confirmación.')
        passw=input('Introduce tu contraseña porfavor: ')
        n = 0

        while passw!=informacion_clientes['contraseña'][cliente]:
            print('Contraseña incorrecta.')
            if n == 3:
                print('Volveras a la pagina de inicio de sesion para la mayor seguridad de tu cuenta')
                g.linea('_')
                c.salgo = True
                return
            
            passw=input('Introduce tu contraseña porfavor: ')

            n = n + 1
            

        traspaso(informacion_clientes,cliente,cobrador,sacado)
            
    else:
        traspaso(informacion_clientes,cliente,cobrador,sacado)
        





def bizumTransferencia(informacion_clientes=c.informacion_clientes):

    encontrado = False
    tipo=input('Que desea realizar, bizum o transferencia? (b/t): ')
    while tipo != 'b' and tipo != 't':
        tipo=input('Que desea realizar, bizum o transferencia? (b/t): ')

    if tipo == 'b':
        while encontrado == False:
            tel=input('Introduce el numero de telefono del cobrador del bizum: ')
            for i in range (len(informacion_clientes['telefono'])):

                if tel == informacion_clientes['telefono'][i]:
                    cobrador = i
                    encontrado = True
                




    elif tipo == 't':

        while encontrado == False:
            tel=input('Introduce el numero IBAN (de ISM) de la cuenta del cobrador de la transferencia: ')
            for i in range (len(informacion_clientes['IBAN'])):

                if tel == informacion_clientes['IBAN'][i]:
                    cobrador = i
                    encontrado = True
                
        

    return cobrador