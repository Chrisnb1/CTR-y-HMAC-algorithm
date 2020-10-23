import Repositorio

lookupTable = {"0000":"0011", "0001":"0100", "0010":"0101", "0011":"0110",
             "0100":"0111", "0101":"1001", "0110":"1101", "0111":"1111",
             "1000":"1100", "1001":"1110", "1010":"1011", "1011":"1010",
             "1100":"1000", "1101":"0001", "1110":"0010", "1111": "0000"}


# Funciones

# funcion que realiza el algoritmo CTR
def obtenerCifrado(M, K):
    # varialbles
    nonce = "01"
    contador = "00"
    _M = M[:4] #bits mas significativos
    M_ = M[4:] #bits menos significativos
    resultado = ""

    # algoritmo en bucle, mientras el contador no se '10' (maximo numero del contador para mensaje de 8 bits)
    while contador!="10":
        # concatenacion nonce||contador
        nonce_contador = nonce + contador
        #sumar xor K⊕nonce||contador
        suma = Repositorio.sumaXOR(K, nonce_contador)
        # busqueda en la tabla de verdad para e cifrado simple
        E = lookupTable.get(suma)
        if E == None: # si no encuentra el resultado en la tabla
            print("No se puede cifrar este numero")
            break
        else: # si lo encuentra
            if contador == "00": # opera con _M
                resultado += Repositorio.sumaXOR(_M, E)
            else: # opera con M_
                resultado += Repositorio.sumaXOR(M_, E)
        print("-Nonce: ", nonce, "-Contador: ", contador, "-Bloque E: ", E, "-Resultado: ", resultado)
        # incrementa el contador
        contador = sumarContador(contador)
    # devuelve el mensaje cifrado
    print()
    print("El texto cifrado con CTR es: ", resultado)


# suma el contador binario
def sumarContador(c):
    # parsea a entero y suma en 1
    contador = int(c) + 1
    # parsea a binario y saca los digitos '0b'
    contador = bin(contador)[2:]
    # verifica que la longitud del contador sea maximo 2 digitos (dos bits)
    if len(contador) == 1:
        # si el contador es 1, se agrega un 0 delante
        contador = str(contador).zfill(2)
    elif len(contador) > 2:
        # si el contador es mayo a dos digitos, se obtienen los dos primeros
        contador = str(contador)[2:]
    # retorna el contador
    return contador


