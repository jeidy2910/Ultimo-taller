import random
import math

def generar_problema_88_13():
    intentos = 0
    max_intentos = 1000
    
    while intentos < max_intentos:
       
        total = random.randint(100, 800)
        doble = 2
        triple = 3
        cuadruple = 4
        
   
        numerador = total - 11
        
        if numerador % 9 == 0:
            x = numerador // 9
            if x > 0:
                print("\n" + "=" * 80)
                print("Autor: Jeidy Alexandra Cordoba Gomez ")
                print("Diciembre de 2025")
                print("Ejercicio 88-13")
                print("=" * 80)
                print(f"Hallar tres números enteros consecutivos, tales que el doble del menor más el triple del mediano más el cuádruple del mayor equivalga a {total}.")
                print()
                print("Solución:")
                print(f"Sea x el menor")
                print(f"El doble del menor es 2x")
                print(f"El triple del mediano es 3(x+1)")
                print(f"El cuadruple del mayor es 4(x+2)")
                print(f"Total: {total}")
                print(f"Ecuación: 2x + 3(x + 1) + 4((x + 1)+1)")
                print(f"Desarrollando: 2x + 3x + 3 + 4x + 8 = {total}")
                print(f"9x + 11 = {total}")
                print(f"9x = {total} - 11")
                print(f"x = ({total} - 11) / 9")
                print()
                print(f"Resultado: Los números son {x}, {x+1} y {x+2}")
                return
                
        intentos += 1
    print("No se pudo generar un problema válido.")
    
generar_problema_88_13()