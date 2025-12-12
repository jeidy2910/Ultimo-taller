import random

def generar_problema_88_25():
    intentos = 0
    max_intentos = 1000
    
    while intentos < max_intentos:
       
        dinero_inicial = random.randint(50, 500)
        multiplicador = random.randint(2, 5)
        
        d = dinero_inicial
        m = multiplicador
        
        numerador = d * (m - 1)
        denominador = 1 + m
        
        if numerador % denominador == 0 and numerador > 0:
            x = numerador // denominador
            
            if 0 < x < d:
                dinero_A = d - x
                dinero_B = m * dinero_A
                
                print("\n" + "=" * 80)
                print("Autor: Jeidy Alexandra Cordoba Gomez ")
                print("Diciembre de 2025")
                print("Ejercicio 88-25")
                print("=" * 80)
                print(f"A y B empiezan a jugar con ${d:,} cada uno.  Problema25 - Problema25.py:29")
                print(f"¿Cuánto ha perdido A si B tiene ahora {m} veces lo que tiene A? - Problema25.py:30")
                print()
                
                print("Solución: - Problema25.py:33")
                print(f"Sea x lo que perdió A  Problema25.34 - Problema25.py:34")
                print(f"A tiene ahora: ${d:,}  x - Problema25.py:35")
                print(f"B tiene ahora: {m} × (${d:,}  x) - Problema25.py:36")
                print()
                print(f"La suma de lo que tienen ahora es igual al total inicial: - Problema25.py:38")
                print(f"(${d:,}  x) + {m}(${d:,}  x) = ${2*d:,} - Problema25.py:39")
                print(f"({d}  x) + {m*d}  {m}x = {2*d} - Problema25.py:40")
                print(f"{d + m*d}  x  {m}x = {2*d} - Problema25.py:41")
                print(f"{d + m*d}  {2*d} = x + {m}x - Problema25.py:42")
                print(f"{d*(m / 1)} = {m} + 1 x - Problema25.py:43")
                print(f"x = {d*(m / 1)} ÷ {m + 1} - Problema25.py:44")
                print(f"x = ${x:,} - Problema25.py:45")
                print()
                print(f"Resultado: A perdió ${x:,} - Problema25.py:47")
                print()
                print(f"Comprobación: - Problema25.py:49")
                print(f"A tiene: ${d:,}  ${x:,} = ${dinero_A:,} - Problema25.py:50")
                print(f"B tiene: {m} × ${dinero_A:,} = ${dinero_B:,} - Problema25.py:51")
                print(f"Suma: ${dinero_A:,} + ${dinero_B:,} = ${dinero_A + dinero_B:,} - Problema25.py:52")
                print(f"Total inicial: ${2*d:,} ✓ - Problema25.py:53")
                return
                
        intentos += 1
    print("No se pudo generar un problema válido en los intentos permitidos. - Problema25.py:57")

generar_problema_88_25()