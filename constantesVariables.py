import random
import string


claves = [
    'usuario',
    'contraseña',
    'nombreApellidos',
    'numero de tarjeta',
    'IBAN',
    'saldo',
    'balance del mes',
    'DNI',
    'telefono',
    'email'
]


archivos = [
    'informacionUsuarios/user.txt',
    'informacionUsuarios/contrasena.txt',
    'informacionUsuarios/nombreApellidos.txt',
    'informacionUsuarios/numTarjeta.txt',
    'informacionUsuarios/IBAN.txt',
    'informacionUsuarios/saldo.txt',
    'informacionUsuarios/balance.txt',
    'informacionUsuarios/DNI.txt',
    'informacionUsuarios/telefono.txt',
    'informacionUsuarios/email.txt'
]


informacion_clientes = {clave: [] for clave in claves}


usuarioNuevo = {'nombre':'',
                'apellidos':'',
                'CP':'',
                'telefono':'',
                'provincia':'',
                'localidad':'',
                'direccion':'',
                'email':'',
                'DNI':''}

salgo = False

def leerArchivos():

    for archivo, clave in zip(archivos, claves):
        with open(archivo, 'r') as archivo_actual:
            lineas = archivo_actual.readlines()
            informacion_clientes[clave] = [linea.strip() for linea in lineas]


def escribir_en_archivos():
    for clave, archivo in zip(informacion_clientes.keys(), archivos):
        with open(archivo, 'w') as archivo_actual:
            for elemento in informacion_clientes[clave]:
                archivo_actual.write(f"{elemento}\n")





                
