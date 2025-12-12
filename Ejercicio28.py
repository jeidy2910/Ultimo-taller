import random

def generar_problema_88_28():
    intentos = 0
    max_intentos = 1000
    
    while intentos < max_intentos:
        gano_mas_por_dia = random.randint(30, 90)
        gane_jueves_veces = random.randint(2, 5)
        total_jueves = gano_mas_por_dia * 3
        
        if gane_jueves_veces < total_jueves:
            denominador = gane_jueves_veces - 1
            numerador = total_jueves
            
            if numerador % denominador == 0:
                x = numerador // denominador
                
                if x > 0:
                    print("\n" + "=" * 80)
                    print("Autor: Jeidy Alexandra Cordoba Gomez ")
                    print("Diciembre de 2025")
                    print("Ejercicio 88-28")
                    print("=" * 80)
                    print(f"Cada día lunes a jueves, gano ${gano_mas_por_dia} más que lo que gané el día anterior. Si el jueves gano el {gane_jueves_veces} veces de lo del lunes, ¿Cuánto gano cada día?")
                    print()
                    
                    print("Solución:")
                    print(f"Sea x lo que gané el lunes")
                    print(f"El martes gano x + {gano_mas_por_dia}")
                    print(f"Si el jueves gana {gane_jueves_veces} veces de lo del lunes:")
                    print(f"El miércoles gano (x + {gano_mas_por_dia}) + {gano_mas_por_dia} = x + {gano_mas_por_dia + gano_mas_por_dia}")
                    print(f"El jueves gano ((x + {gano_mas_por_dia}) + {gano_mas_por_dia}) + {gano_mas_por_dia} = x + {gano_mas_por_dia + gano_mas_por_dia + gano_mas_por_dia}")
                    print()
                    print(f"Si el jueves gano el cuádruple de lo del lunes, entonces: {gane_jueves_veces}x es lo que gano el jueves, esto significa que:")
                    print(f"{gane_jueves_veces}x = x + {total_jueves}")
                    print(f"{gane_jueves_veces}x - x = {total_jueves}")     
                    print(f"{gane_jueves_veces - 1}x = {total_jueves}") 
                    print(f"x = {total_jueves} / {gane_jueves_veces - 1}") 
                    print(f"x = {x}")  
                    print()
                    print(f"x = {x} es lo que gano el lunes")
                    print(f"x + {gano_mas_por_dia} = {x} + {gano_mas_por_dia} = {x + gano_mas_por_dia} es lo que gano el martes")      
                    print(f"x + {gano_mas_por_dia + gano_mas_por_dia} = {x} + {gano_mas_por_dia} + {gano_mas_por_dia} = {x + gano_mas_por_dia + gano_mas_por_dia} es lo que gano el miércoles")
                    print(f"x + {gano_mas_por_dia + gano_mas_por_dia + gano_mas_por_dia} = {x} + {gano_mas_por_dia} + {gano_mas_por_dia} + {gano_mas_por_dia} = {x + gano_mas_por_dia + gano_mas_por_dia + gano_mas_por_dia} es lo que gano el jueves")
                    return           
        intentos += 1
    print("No se pudo generar un problema válido en los intentos permitidos.")
    
generar_problema_88_28()