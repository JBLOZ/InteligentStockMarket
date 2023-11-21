import constantes_variables as c
import random
import string



def crearCuenta():
    nombre_usuario = ""
    nombre_usuario = input('Introduce un nombre de usuario: ')
    while len(nombre_usuario) < 3:
        nombre_usuario = input('El nombre de usuario tiene que tener mas de 3 caracteres: ')
        while nombre_usuario in c.usuarios:
            nombre_usuario = input('Este nombre de usuario ya ha sido usado, escoja otro : ')
    while nombre_usuario in c.usuarios:
            nombre_usuario = input('Este nombre de usuario ya ha sido usado, escoja otro : ')    
        
    return nombre_usuario

def iniciar_sesion(usuarios,contrasenas):
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

