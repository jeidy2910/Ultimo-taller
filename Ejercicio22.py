import random

def generar_problema_88_22():
    intentos = 0
    max_intentos = 1000
    
    while intentos < max_intentos:
        factor_A = random.randint(2, 5)  
        factor_B = random.randint(2, 5) 
        
        pierde_A = random.randint(1, 10)
        pierde_B = random.randint(1, 10)
        
        gana_C = random.randint(5, 50)
        
        multiplicador = random.randint(2, 4)
        
        numerador = multiplicador * gana_C + pierde_B - pierde_A
        denominador = factor_A * factor_B - factor_B - multiplicador
        
        if denominador != 0 and numerador % denominador == 0:
            x = numerador // denominador
            
            if x > 0:
                C = x
                B = factor_B * C
                A = factor_A * B
                
                if A > pierde_A and B > pierde_B:
                    print("\n" + "=" * 80)
                    print("Autor: Jeidy Alexandra Cordoba Gomez ")
                    print("Diciembre de 2025")
                    print("Ejercicio 88-22")
                    print("=" * 80)
                    print(f"A tiene {factor_A} veces lo que tiene B,")
                    print(f"y B tiene {factor_B} veces lo de C.")
                    print(f"Si A pierde ${pierde_A} y B pierde ${pierde_B},")
                    print(f"la diferencia de lo que les queda a A y a B es")
                    print(f"{multiplicador} veces lo que tendría C si ganara ${gana_C}.")
                    print(f"¿Cuánto tiene cada uno?")
                    print()
                    
                    print("Solución:")
                    print(f"Sea x lo que tiene C")
                    print(f"B = {factor_B}x")
                    print(f"A = {factor_A}({factor_B}x) = {factor_A*factor_B}x")
                    print()
                    
                    print(f"Si A pierde ${pierde_A}: A queda = {factor_A*factor_B}x - {pierde_A}")
                    print(f"Si B pierde ${pierde_B}: B queda = {factor_B}x - {pierde_B}")
                    print(f"Si C ganara ${gana_C}: C tendría = x + {gana_C}")
                    print()
                    
                    print(f"Ecuación:")
                    print(f"({factor_A*factor_B}x - {pierde_A}) - ({factor_B}x - {pierde_B}) = {multiplicador}(x + {gana_C})")
                    print()
                    
                    print(f"Resolviendo:")
                    print(f"{factor_A*factor_B}x - {pierde_A} - {factor_B}x + {pierde_B} = {multiplicador}x + {multiplicador*gana_C}")
                    print(f"{factor_A*factor_B}x - {factor_B}x - {multiplicador}x = {multiplicador*gana_C} + {pierde_A} - {pierde_B}")
                    print(f"({factor_A*factor_B - factor_B - multiplicador})x = {multiplicador*gana_C + pierde_A - pierde_B}")
                    print(f"{denominador}x = {numerador}")
                    print(f"x = {numerador} ÷ {denominador}")
                    print(f"x = ${C}")
                    print()
                    
                    print(f"Resultado:")
                    print(f"C tiene: ${C}")
                    print(f"B tiene: {factor_B} x ${C} = ${B}")
                    print(f"A tiene: {factor_A} x ${B} = ${A}")
                    return
                
        intentos += 1
    print("No se pudo generar un problema válido en los intentos permitidos.")
    
generar_problema_88_22()