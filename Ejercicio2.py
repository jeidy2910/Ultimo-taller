import random
import math
def generar_problema_88_2():
    intentos = 0
    max_intentos = 1000

    while intentos < max_intentos:
        m = random.randint(2, 5)  
        p = random.randint(m + 1, m + 3)  
        años_atras = random.randint(2, 10)
        
        
        numerador = años_atras * (1 - p)
        denominador = m - p
        
        if denominador != 0 and numerador % denominador == 0:
            x = numerador // denominador
            if x > años_atras:  
                A = m * x 
                if A > años_atras:
                    print("\n" + "=" * 80)
                    print("Autor: Jeidy Alexandra Cordoba Gomez")
                    print("Diciembre de 2025")
                    print("Ejercicio 88-2")
                    print("=" * 80)
                    print("Enunciado:")
                    print(f"La edad de A es {m} veces la de B y hace {años_atras} años era {p} veces la de B. Hallar las edades actuales.")
                    print()
                    print("Solución paso a paso:")
                    print(f"Sea x la edad de B")
                    print(f"La edad de A es {m} veces B, entonces {m}x es la edad de A")
                    print(f"La edad de B hace {años_atras} años era x - {años_atras}")
                    print(f"La edad de A hace {años_atras} años era {m}x - {años_atras}")
                    print(f"Hace {años_atras} años la edad de A era {p} veces la de B, entonces:")
                    print(f"{m}x - {años_atras} = {p}(x - {años_atras})")
                    print(f"Resolviendo: {m}x - {años_atras} = {p}x - {p*años_atras}")
                    print(f"{m}x - {p}x = {años_atras} - {p*años_atras}")
                    print(f"({m - p})x = {años_atras - p*años_atras}")
                    print(f"x = {x} (edad de B)")
                    print(f"{m}x = {A} (edad de A)")
                    print()
                    print("Resultado final:")
                    print(f"Edad de A: {A} años")
                    print(f"Edad de B: {x} años")
                    print(f"Comprobación: {A} = {m} × {x} ✓")
                    print(f"Hace {años_atras} años: A tenía {A - años_atras}, B tenía {x - años_atras}")
                    print(f"  {A - años_atras} = {p} × {x - años_atras} ")
                    return
        intentos += 1
    print("No se pudo generar un problema válido en los intentos permitidos.")
    
generar_problema_88_2()