import random
import math

def generar_problema_88_10():
    intentos = 0
    max_intentos = 1000

    while intentos < max_intentos:
   
        resta1 = random.randint(10, 50)
        resta2 = random.randint(10, 50)
        while resta2 == resta1:
            resta2 = random.randint(10, 50)
     
        mult1 = random.randint(2, 20)
        mult2 = random.randint(2, 20)
        while mult2 == mult1:
            mult2 = random.randint(2, 20)
        

        
        numerador = mult1 * resta1 - mult2 * resta2
        denominador = mult1 - mult2
        
        if denominador != 0 and numerador % denominador == 0:
            x = numerador // denominador
            
           
            if x > max(resta1, resta2):
                print("\n" + "=" * 80)
                print("Autor: Jeidy Alexandra Cordoba Gomez ")
                print("Diciembre de 2025")
                print("Ejercicio 88-10")
                print("=" * 80)
                print(f"Si a un número se resta {resta1} y la diferencia se multiplica por {mult1}, - Problema10.py:41")
                print(f"el resultado es el mismo que si al número se resta {resta2} y la diferencia - Problema10.py:42")
                print(f"se multiplica por {mult2}. Hallar el número. - Problema10.py:43")
                print()
                print("Solución paso a paso: - Problema10.py:45")
                print(f"Sea x el número buscado - Problema10.py:46")
                print(f"Primera operación: (x  {resta1}) × {mult1} - Problema10.py:47")
                print(f"Segunda operación: (x  {resta2}) × {mult2} - Problema10.py:48")
                print()
                print(f"Según el problema: - Problema10.py:50")
                print(f"{mult1}(x  {resta1}) = {mult2}(x  {resta2}) - Problema10.py:51")
                print(f"{mult1}x  {mult1*resta1} = {mult2}x  {mult2*resta2} - Problema10.py:52")
                print(f"{mult1}x  {mult2}x = {mult1*resta1}  {mult2*resta2} - Problema10.py:53")
                print(f"({mult1}  {mult2})x = {mult1*resta1}  {mult2 * resta2} - Problema10.py:54")
                print(f"x = {mult1*resta1} {mult2 * resta2 }  ÷ {mult1 + mult2} - Problema10.py:55")
                print(f"x = {x} - Problema10.py:56")
                print()
                print("Resultado final: - Problema10.py:58")
                print(f"El número buscado es: {x} - Problema10.py:59")
                print()
                print("Comprobación: - Problema10.py:61")
                print(f"Primera operación: ({x}  {resta1}) × {mult1} = {xresta1} × {mult1} = {(xresta1)*mult1} - Problema10.py:62")
                print(f"Segunda operación: ({x}  {resta2}) × {mult2} = {xresta2} × {mult2} = {(xresta2)*mult2} - Problema10.py:63")
                print(f"Ambas son iguales: {(xresta1)*mult1} = {(xresta2)*mult2} ✓ - Problema10.py:64")
                return
                
        intentos += 1
    print("No se pudo generar un problema válido en los intentos permitidos. - Problema10.py:68")

generar_problema_88_10()