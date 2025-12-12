import random

def generar_problema_88_20():
    intentos = 0
    max_intentos = 1000
    
    while intentos < max_intentos:
        
        diferencia = random.randint(10, 50) 
        multiplicador = random.randint(2, 5)  
        
        
        numerador = diferencia * (multiplicador + 1)
        
        if numerador % 2 == 0:
            mayor = numerador // 2
            menor = mayor - diferencia
            
            
            if mayor > 0 and menor > 0 and mayor > menor:
                print("\n" + "=" * 80)
                print("Autor: Jeidy Alexandra Cordoba Gomez ")
                print("Diciembre de 2025")
                print("Ejercicio 88-20")
                print("=" * 80)
                print(f"Hallar dos números cuya diferencia es {diferencia} y cuya suma")
                print(f"es {multiplicador} veces su diferencia.")
                print()
                
                print("Solución:")
                print(f"Sea x el número mayor")
                print(f"Sea y el número menor")
                print()
                print(f"Condiciones:")
                print(f"1) x - y = {diferencia}")
                print(f"2) x + y = {multiplicador} × {diferencia} = {multiplicador*diferencia}")
                print()
                print(f"x + (x - {diferencia}) = {multiplicador*diferencia}")
                print(f"2x - {diferencia} = {multiplicador*diferencia}")
                print(f"2x = {multiplicador*diferencia} + {diferencia}")
                print(f"2x = {multiplicador*diferencia + diferencia}")
                print(f"2x = {diferencia}({multiplicador} + 1)")
                print(f"2x = {diferencia*(multiplicador + 1)}")
                print(f"x = {diferencia*(multiplicador + 1)} ÷ 2")
                print(f"x = {mayor} (número mayor)")
                print()
                print(f"y = x - {diferencia}")
                print(f"y = {mayor} - {diferencia}")
                print(f"y = {menor} (número menor)")
                print()
                print(f"Resultado:")
                print(f"Número mayor: {mayor}")
                print(f"Número menor: {menor}")
                print()
                print(f"Comprobación:")
                print(f"Diferencia: {mayor} - {menor} = {diferencia}")
                print(f"Suma: {mayor} + {menor} = {mayor + menor}")
                print(f"{multiplicador} × {diferencia} = {multiplicador*diferencia}")
                return
                
        intentos += 1
    print("No se pudo generar un problema válido en los intentos permitidos.")
    
generar_problema_88_20()