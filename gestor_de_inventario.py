stock_producto = 10
ventas_totales = 0
recaudacion = 0.0

while stock_producto > 0:
    vendedor = input("\nIngresá tu nombre: ").strip().title()
    pregunta = input(f"Hola {vendedor}, ¿querés realizar una venta? (si/no): ").strip().lower()
    
    if pregunta == "si":
        unidades = int(input("¿Cuantas unidades desea vender? "))
        
        if unidades > stock_producto:
            print("ERROR: Stock insuficiente.")
            continue
        
        elif unidades <= stock_producto:
            stock_producto -= unidades
            ventas_totales += unidades
            recaudacion += unidades * 2500.50
            
            print(f"Venta exitosa. Quedan {stock_producto} unidades.")
            
        elif pregunta == "no":
            print("Cerrando turno del vendedor...")
            break
            
        else:
            print("Opción inválida, respondé 'si' o 'no'.")

print("\n" + "="*30)
print(f"RESUMEN DE JORNADA")
print(f"Vendedor: {vendedor}")
print(f"Unidades vendidas: {ventas_totales}")
print(f"Total recaudado: ${recaudacion:.2f}")
print("="*30)