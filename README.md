# CTR-y-HMAC-algorithm
Aplicación de algoritmos de cifrados CTR y HMAC. Hecho en Python.

## Instrucciones
_Clonar el repositorio_

```
git clone https://github.com/Chrisnb1/CTR-y-HMAC-algorithm
```

## Objetivos
* Adaptación del cifrado en bloque CTR
* Generación de MAC´s utilizando el algoritmo HMAC. 

## Codigo
* CTR.py & HMAC.py- algoritmos de cifrado simple
* Repositorio.py - Obtención de claves e implementación de los algoritmos.
* Main.py - Ejecución del programa.

## Teoría
### Cifrado simétrico - Modo de operación: CTR
Se emplea un vector de inicialización IV (puede ser aleatorio o no) y se concatena y/o combina con un contador (inicialmente en 0) con la clave k para codificar el primer bloque. Cada bloque es cifrado y luego combinado, mediante la operación XOR, con el siguiente bloque del mensaje original.  

![image](https://user-images.githubusercontent.com/63667971/222265108-ed7af45c-429c-493d-9a05-00ad548d9b5f.png)

A medida que avanzan los bloques del texto plano a cifrar el contador se incrementa en 1 y, por tanto, se origina una secuencia cifrante diferente en cada bloque. 

![image](https://user-images.githubusercontent.com/63667971/222265187-96f8ecb8-5718-4db5-b6ee-c1fc64188502.png)

Las ecuaciones del cifrado y descifrado son:
* 𝐶𝑖=𝐸𝑘(𝐼𝑉||CTR𝑖) ⊕ 𝑃𝑖
* 𝑃𝑖=𝐸𝑘(𝐼𝑉||CTR𝑖) ⊕ 𝐶𝑖

Siendo:
* IV: valor aleatorio (vector inicial).
* CTR𝑖: contador en su índice i.
* 𝐸𝑘 : bloque de código con la clave k.
* 𝐶𝑖: Texto cifrado en su índice i.
* 𝑃𝑖: Texto plano en su índice i.

### MAC con hashes - Modo de operación: HMAC
El funcionamiento de HMAC comienza tomando un mensaje M que contiene bloques de longitud b bits. Una firma de entrada se rellena a la izquierda del mensaje y el conjunto se proporciona como entrada a una función hash que nos da un resumen de mensaje temporal MD '. MD ' nuevamente se agrega a una firma de salida y al conjunto se le aplica nuevamente una función hash, el resultado es nuestro MD de resumen de mensaje final.

![image](https://user-images.githubusercontent.com/63667971/222265938-1303a925-364f-4d08-a3b8-b604101428be.png)

La definición del algoritmo es:

![image](https://user-images.githubusercontent.com/63667971/222266006-b677a328-d26b-49d4-ae0f-59d37437e0aa.png)

Siendo:
* H: función hash.
* M: mensaje original.
* 𝑆0 : (𝐾´⊕𝑜𝑝𝑎𝑑)
* 𝑆𝑖: (𝐾´⊕𝑖𝑝𝑎𝑑)
* Yi: es el bloque i en el mensaje original M, donde i varía entre [1, L).
* L: el recuento de bloques en M.
* K: es la clave secreta utilizada para el hash.
* IV: valor aleatorio (vector inicial).

