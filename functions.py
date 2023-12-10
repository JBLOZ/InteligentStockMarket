import constantesVariables as c
import funcionesGenericas as g
import crearCuenta as CC
import iniciarSesion as IS


#FUNCION PRINCIPAL DEL PROGRAMA, ES LA PANTALLA PRINCIPAL 


def iniciarSesion_crearCuenta():

    salir = False

    while not salir:
        c.salgo = False
        c.leerArchivos()

        g.linea(y=2)
        g.linea(c='*')

        s = input("¿Desea Iniciar sesión, Registrarse o Salir? (i/r/s): ")

        if s=='i':
            
            IS.iniciarSesion()

        elif s=='r':

            CC.crearCuenta()
            c.leerArchivos()
        
        elif s=='s':

            g.linea(y=2)
            g.linea(c='*')
            salir = True
        
