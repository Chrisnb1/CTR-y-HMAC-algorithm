import Repositorio
from CTR import obtenerCifrado #Importamos la funcion del algoritmo CTR
from HMAC import obtenerMAC  # Importamos la funcion del algoritmo HMAC

# Solicita el Mensaje
def mensaje():
    # Solicita un string con 0 y 1, y lo devuelve.
    while True:
        M = input("Introduce un mensaje a cifrar en binario (maximo de 8 bits): ")
        for i in M:
            if i!='1' and i!='0': # Si no contiene 0 o 1 la cadena ingresada, se vuelve a repetir el bucle
                print("La entrada no es valida. Intentelo nuevamente.")
                break
        else:
            if Repositorio.validarBits(M, 8):
                break


# Solicita la clave
def clave():
    # Solicita un numero binario de tipo string y lo devuelve.
    while True:
        K = input("Introduce una clave en binario (maximo de 4 bits): ")
        for i in K: # Si no contiene 0 o 1 la cadena ingresada, se vuelve a repetir el bucle
            if i != '1' and i != '0':
                print("La entrada no es valida. Intentelo nuevamente.")
                break
        else:
            Repositorio.validarBits(K, 4)
            break



# Consola
mensaje()
clave()
print()
print("***APLICANDO ALGORITMO CTR PARA OBTENER EL MENSAJE CIFRADO***")
print()
obtenerCifrado(Repositorio.obtenerMensaje(), Repositorio.obtenerClave())
print()
print("***APLICANDO ALGORITMO HMAC PARA OBTENER LA MAC***")
print()
obtenerMAC(Repositorio.obtenerMensaje(), Repositorio.obtenerClave())







