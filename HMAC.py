import Repositorio

# Funciones

# funcion hash simple, recibe un string y retorna un string
def hashSimple(num):
    binario_decimal = int(num, 2) # convierte la cadena en entero, de binario a decimal (en base 2)
    mod = (binario_decimal * 7) % 13 # se realiza el modulo (a * 7) mod 13
    resul = bin(mod)[2:] # se parsea a binario y se quita los dos digitos delante (0b)
    resultado = str(resul) # se parsea a string nuevamente

    salida = Repositorio.bloqueBits(resultado) # Se acomoda la entrada a los digitos del bloque (4 bits)

    print("De binario a decimal = ", binario_decimal,"-Mod = (",binario_decimal,"* 7 ) mod 13 = " ,mod,"-De decimal a binario = ", salida)
    return salida

# funcion que define el algoritmo HMAC. Recibe la clave y el mensaje en binario
# H((k xor opad)||H((k xor ipad)||m))
def obtenerMAC(M, K):
    # variables constantes
    ipad = "1100"
    opad = "1001"
    # suma (k XOR ipad)
    K_ipad = Repositorio.sumaXOR(K, ipad)
    print("-Clave = ", K, "-Ipad = ", ipad, "-(k ⊕ ipad) = ", K_ipad)
    # concatenacion del resultado (k XOR ipad) y el mensaje (M)
    # ((k xor ipad) || m)
    M_K_ipad = K_ipad + M
    # primer bloque _MD=H((k xor ipad) || m)
    _MD = hashSimple(M_K_ipad)
    print()
    print("-MD´ = H((k ⊕ ipad) || m) = ", _MD)
    # suma (k XOR opad)
    K_opad = Repositorio.sumaXOR(K, opad)
    print("-Clave = ", K, "-Opad = ", opad, "-(k ⊕ opad) = ", K_opad)
    # concatenacion del resultado (k XOR opad) y el primer bloque _MD
    # ((k xor opad) ||_MD)
    _MD_K_opad = K_opad + _MD
    # MD=H((k xor opad) ||_MD)
    print()
    MD = hashSimple(_MD_K_opad)
    print("-Ipad = ", ipad, "-Opad = ", opad, "-MD = H((k ⊕ opad) || MD´) = ", MD)
    print()
    print("El número MAC es (MD) = ", MD)
