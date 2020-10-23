# Variables globales
mensaje_M = ""
clave_K = ""

# funcion que realiza la suma XOR entre dos numeros (ambos string)
def sumaXOR(a, b):
    c = int(a, 2) ^ int(b, 2) # convierte la cadena en entero, de binario a decimal (en base 2)
    c = bin(c)[2:] # se parsea a binario y se quita los dos digitos delante (0b)
    resul = str(c) # se parsea a string nuevamente
    salida = bloqueBits(resul)
    return salida

# funcion que acomoda los bits
def bloqueBits(num):
    resultado = 0

    if len(num) > 4: # si los bits son mas 4, se opera con los 4 menos significativos
        resultado = num[0:4]
    elif len(num) < 4: # si son menos que 4, se le agregan ceros a la izquierda
        resultado = num.zfill(4)
    else:
        resultado = num

    return resultado # retorna el resultado (string)



# Funciones
def validarBits(num, bits):
    result = ""
    # Si es mayor la longitud de carteres ingresados se vuelve a solicitar dicha entrada
    if len(num) > bits:
        print("el numero es debe ser MENOR a ",bits,"  bits")
        return False
    # Si es menor, se agregan ceros delante del numero
    elif len(num) < bits:
        print("el numero es MENOR a",bits,"bits")
        result = num.zfill(bits)
        resto = bits - len(num)
        print("se han agregado ", resto, "cero(s) al numero: ", result)


    else:
        result = num

    # Se guarda el mensaje
    if bits == 8:
        guardarMensaje(result)

    # Se guarda la clave
    else:
        guardarClave(result)

    return True

# Se guarda el mensaje
def guardarMensaje(_mensaje):
    global mensaje_M
    mensaje_M = _mensaje

# Se obtiene el mensaje
def obtenerMensaje():
    global mensaje_M
    if mensaje_M != "":
        return mensaje_M
    else:
        print("El mensaje no se encuentra definido.")

# Se guarda la clave
def guardarClave(_clave):
    global clave_K
    clave_K = _clave

# Se obtiene la clave
def obtenerClave():
    global clave_K
    if clave_K != "":
        return clave_K
    else:
        print("La clave no se encuentra definida.")