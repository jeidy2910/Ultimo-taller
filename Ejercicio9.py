import random
import math

def generar_problema_88_9():
    intentos = 0
    max_intentos = 1000

    while intentos < max_intentos:
       
        valor_moneda1 = random.choice([5, 10, 25, 50])  
        valor_moneda2 = random.choice([1, 5, 10, 25])   
        
        if valor_moneda1 == valor_moneda2:
            valor_moneda2 = random.choice([1, 5, 10, 25])
        
       
        if valor_moneda1 < valor_moneda2:
            valor_moneda1, valor_moneda2 = valor_moneda2, valor_moneda1
        
        total_monedas = random.randint(10, 50)
        
        total_centavos = random.randint(100, 1000)  
        
    
        
        numerador = total_centavos - valor_moneda2 * total_monedas
        denominador = valor_moneda1 - valor_moneda2
        
        if denominador != 0 and numerador % denominador == 0:
            x = numerador // denominador
            if x > 0 and x < total_monedas:
                y = total_monedas - x
                
                print("\n" + "=" * 80)
                print("Autor: Jeidy Alexandra Cordoba Gomez ")
                print("Diciembre de 2025")
                print("Ejercicio 88-9")
                print("=" * 80)
                print("Enunciado:")
                print(f"Tengo ${total_centavos/100:.2f} en monedas de {valor_moneda1} y {valor_moneda2} centavos. ")
                print(f"Si en total tengo {total_monedas} monedas, ¿cuántas son de {valor_moneda1} centavos ")
                print(f"y cuántas de {valor_moneda2} centavos?")
                print()
                print("Solución paso a paso:")
                print(f"Sea x la cantidad de monedas de {valor_moneda1} centavos")
                print(f"Como en total hay {total_monedas} monedas, entonces {total_monedas} - x es la ")
                print(f"cantidad de monedas de {valor_moneda2} centavos")
                print()
                print(f"La suma del valor de las monedas es ${total_centavos/100:.2f} ({total_centavos} centavos):")
                print(f"{valor_moneda1}x + {valor_moneda2}({total_monedas} - x) = {total_centavos}")
                print(f"{valor_moneda1}x + {valor_moneda2*total_monedas} - {valor_moneda2}x = {total_centavos}")
                print(f"({valor_moneda1} - {valor_moneda2})x + {valor_moneda2*total_monedas} = {total_centavos}")
                print(f"({valor_moneda1 - valor_moneda2})x = {total_centavos} - {valor_moneda2*total_monedas}")
                print(f"({valor_moneda1 - valor_moneda2})x = {total_centavos - valor_moneda2*total_monedas}")
                print(f"x = {total_centavos - valor_moneda2*total_monedas} ÷ {valor_moneda1 - valor_moneda2}")
                print(f"x = {x} (monedas de {valor_moneda1}¢)")
                print()
                print(f"Reemplazando: {total_monedas} - {x} = {y} (monedas de {valor_moneda2}¢)")
                print()
                print("Resultado final:")
                print(f"Monedas de {valor_moneda1} centavos: {x}")
                print(f"Monedas de {valor_moneda2} centavos: {y}")
                print()
                print("Comprobación:")
                print(f"Total monedas: {x} + {y} = {total_monedas} ✓")
                valor_total = x*valor_moneda1 + y*valor_moneda2
                print(f"Valor total: {x}×{valor_moneda1}¢ + {y}×{valor_moneda2}¢ = {valor_total}¢ = ${valor_total/100:.2f} ✓")
                return
                
        intentos += 1
    print("No se pudo generar un problema válido en los intentos permitidos.")
    
generar_problema_88_9()