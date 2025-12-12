import random

def generar_problema_88_3():
    intentos = 0
    max_intentos = 1000

    while intentos < max_intentos:
        
        num_trajes = random.randint(10, 100)
        num_zapatos = random.randint(10, 100)

       
        x = random.randint(10, 200)
        extra = random.randint(10, 100)
        
       
        total = num_trajes * (2*x + extra) + num_zapatos * x
        
        
        print("\n" + "=" * 80)
        print("Autor: Jeidy Alexandra Cordoba Gomez ")
        print("Diciembre de 2025")
        print("Ejercicio 88-3")
        print("=" * 80)
        print("Enunciado:")
        print(f"Un comerciante adquiere {num_trajes} trajes y {num_zapatos} pares de zapatos por {total:,} nuevos soles. "
              f"Cada traje costó el doble de lo que costó cada par de zapatos más {extra} nuevos soles. "
              f"Hallar el precio de un traje y de un par de zapatos.")
        print()
        print("Solución paso a paso:")
        print(f"Sea x el precio de un par de zapatos")
        print(f"Cada traje costó el doble de lo que costó cada par de zapatos más {extra} nuevos soles, "
              f"entonces: 2x + {extra} es el costo de cada traje")
        print(f"Se compraron {num_trajes} trajes, es decir: {num_trajes}(2x + {extra}) es el costo de los trajes")
        print(f"Se compraron {num_zapatos} pares de zapatos, es decir: {num_zapatos}x es el costo de los pares de zapatos")
        print()
        print(f"Resolvemos la ecuación:")
        print(f"{num_trajes}(2x + {extra}) + {num_zapatos}x = {total}")
        print(f"{2*num_trajes}x + {num_trajes*extra} + {num_zapatos}x = {total}")
        print(f"({2*num_trajes + num_zapatos})x + {num_trajes*extra} = {total}")
        print(f"({2*num_trajes + num_zapatos})x = {total} - {num_trajes*extra}")
        print(f"({2*num_trajes + num_zapatos})x = {total - num_trajes*extra}")
        print(f"x = {total - num_trajes*extra} / {2*num_trajes + num_zapatos}")
        print(f"x = {x}")
        print()
        precio_traje = 2*x + extra
        print(f"Precio de un par de zapatos: {x} nuevos soles")
        print(f"Precio de un traje: 2×{x} + {extra} = {precio_traje} nuevos soles")
        print()
        print("Comprobación:")
        print(f"Trajes: {num_trajes} × {precio_traje} = {num_trajes * precio_traje}")
        print(f"Zapatos: {num_zapatos} × {x} = {num_zapatos * x}")
        print(f"Total: {num_trajes * precio_traje} + {num_zapatos * x} = {total} ✓")
        return
        
        intentos += 1
    print("No se pudo generar un problema válido en los intentos permitidos.")
    
generar_problema_88_3()