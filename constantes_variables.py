import random
import string

informacion_clientess= [{'usuario':'Hugo','contraseña':'micaela','numero de tarjeta':'0123456789012345','saldo':'500','balance del mes':'-500'},
                       {'usuario':'Jordi','contraseña':'hola','numero de tarjeta':'9876543210987654','saldo':'700','balance del mes':'-250'},
                       {'usuario':'Adrian','contraseña':'rana','numero de tarjeta':'0246802468024680','saldo':'900','balance del mes':'-400'},
                       {'usuario':'David','contraseña':'silla','numero de tarjeta':'9753197531953197','saldo':'250','balance del mes':'-800'},
                       {'usuario':'Pepe','contraseña':'hola93','numero de tarjeta':'0918273645546372','saldo':'340','balance del mes':'-1000'}
                      ]


# Inicializa la lista de diccionarios
informacion_clientes = []

# Nombres de las claves
claves = ['usuario',
        'contraseña',
        'nombreApellidos',
        'numero de tarjeta',
        'IBAN',
        'saldo',
        'DNI',
        'telefono',
        'email']

# Nombres de los archivos
archivos = [
    'informacionUsuarios/user.txt',
    'informacionUsuarios/contrasena.txt',
    'informacionUsuarios/nombreApellidos.txt',
    'informacionUsuarios/numTargeta.txt',
    'informacionUsuarios/IBAN.txt',
    'informacionUsuarios/saldo.txt',
    'informacionUsuarios/DNI.txt',
    'informacionUsuarios/telefono.txt',
    'informacionUsuarios/email.txt'
]

# Itera sobre cada archivo y clave
for archivo, clave in zip(archivos, claves):
    # Inicializa el diccionario para el archivo actual
    diccionario_actual = {}

    # Abre el archivo y lee todas las líneas
    with open(archivo, 'r') as archivo_actual:
        lineas = archivo_actual.readlines()

        # Asigna al diccionario con la clave correspondiente
        diccionario_actual[clave] = [linea.strip() for linea in lineas]

    # Agrega el diccionario a la lista
    informacion_clientes.append(diccionario_actual)

# Imprime la lista de diccionarios
print(informacion_clientes)









usuarioNuevo = {'nombre':'',
                'apellidos':'',
                'CP':'',
                'telefono':'',
                'provincia':'',
                'localidad':'',
                'direccion':'',
                'email':'',
                'DNI':''}

lineatx = 0

                
