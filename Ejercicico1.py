import random
import math
def generar_problema_88_1():
    intentos = 0
    max_intent = 1000

    while intentos < max_intent:
        total = random.randint(50, 500)
        exceso = random.randint(5, 50)

        numerador = total + exceso
        if numerador % 6 == 0:
            x = numerador // 6
            if x > 0:
                tercera = 3 * x - exceso
                if tercera > 0:
                    print("\n" + "=" * 80)
                    print("Autor: Jeidy Alexandra Cordoba Gomez")
                    print("Diciembre de 2025")
                    print("Ejercicio 88-1, Álgebra de Baldor")
                    print("=" * 80)
                    print("Enunciado:")
                    print(f"Dividir {total} en tres partes tales que la segunda sea el doble de la primera "
                          f"y la suma de las primeras exceda a la tercera en {exceso}.")
                    print()
                    print("Solución paso a paso:")
                    print(f"Sea x la primera parte.")
                    print(f"La segunda parte es el doble de la primera, es decir: 2x.")
                    print(f"La suma de las primeras excede a la tercera en {exceso}, "
                          f"es decir, la tercera parte es: (x + 2x) - {exceso} = 3x - {exceso}.")
                    print(f"Como el número a dividir es {total}, entonces la suma de las tres partes debe ser igual a {total}:")
                    print(f"x + 2x + (3x - {exceso}) = {total}")
                    print(f"Simplificando: 6x - {exceso} = {total}")
                    print(f"Despejando: 6x = {total} + {exceso} => 6x = {numerador}")
                    print(f"Entonces: x = {numerador} / 6 = {x}")
                    print()
                    print("Resultado final:")
                    print(f"Primera parte: x = {x}")
                    print(f"Segunda parte: 2x = {2 * x}")
                    print(f"Tercera parte: 3x - {exceso} = {tercera}")
                    print(f"Comprobación: {x} + {2*x} + {tercera} = {x + 2*x + tercera} = {total}")
                    return
        intentos += 1
    print("No se pudo generar un problema válido con solución entera y positiva en los intentos permitidos.")
    
    
generar_problema_88_1()