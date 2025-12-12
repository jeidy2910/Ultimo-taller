import random

def generar_problema_88_26():
    intentos = 0
    max_intentos = 1000
    
    while intentos < max_intentos:
        pierde_A = random.randint(100, 1000)
        n_veces_a = random.randint(2, 5)
        n_veces_b = random.randint(2, 5)

        numerador = pierde_A * n_veces_b + pierde_A
        denominador = n_veces_a * n_veces_b - 1

        if denominador != 0 and numerador % denominador == 0:
            x = numerador // denominador

            if x > 0:
                print("\n" + "=" * 80)
                print("Autor: Jeidy Alexandra Cordoba Gomez ")
                print("Diciembre de 2025")
                print("Ejercicio 88-26")
                print("=" * 80)
                print(f"A y B empiezan a jugar teniendo A {n_veces_a} veces el dinero que B. A pierde ${pierde_A} y entonces B tiene {n_veces_b} veces de lo que tiene A. ¿con cuánto empezó a jugar cada uno? - Problema26.py:25")
                print("Sea x la cantidad con la que empezó a jugar B, entonces: - Problema26.py:26")
                print("2x es la cantidad con la que empezó a jugar A - Problema26.py:27")
                print(f"Si A pierde ${pierde_A}, entonces: 2x {pierde_A}, es lo que tiene A - Problema26.py:28")
                print(f"Lo que pierde A lo gana B, es decir x + {pierde_A} es lo que tiene B - Problema26.py:29")
                print(f"B tiene el doble de lo que tiene A, es decir: {n_veces_b}({n_veces_a}x - {pierde_A}) - Problema26.py:30")
                print(f"El problema menciona “A pierde ${pierde_A} y entonces B tiene el doble de lo que tiene A”, esto lo podemos expresar de la siguiente manera: - Problema26.py:31")
                print()
                print("Solución: - Problema26.py:33")
                print(f"x + {pierde_A} = {n_veces_b}({n_veces_a}x - {pierde_A}) - Problema26.py:34")
                print(f"x + {pierde_A} = {n_veces_b * n_veces_a}x - {n_veces_b * pierde_A} - Problema26.py:35")
                print(f"x - {n_veces_b * n_veces_a}x = {pierde_A} - {n_veces_b * pierde_A} - Problema26.py:36")
                print(f"{n_veces_b * n_veces_a - 1 }x = {pierde_A} - {n_veces_b * pierde_A} - Problema26.py:37")
                print(f"{n_veces_b * n_veces_a - 1 }x = {pierde_A - n_veces_b * pierde_A} - Problema26.py:38")
                print(f"-x = {pierde_A - n_veces_b * pierde_A} / -{n_veces_b * n_veces_a - 1 }= - Problema26.py:39")
                print(f"x = {(pierde_A - n_veces_b * pierde_A) * (-1) / (n_veces_b * n_veces_a - 1)}= - Problema26.py:40")
                return
                
        intentos += 1
    print("No se pudo generar un problema válido.")

generar_problema_88_26()