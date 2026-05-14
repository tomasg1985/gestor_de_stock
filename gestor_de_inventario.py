stock_producto = 10
vendedores_registrados = []
montos_ventas = []

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
            monto_operacion = unidades * 2500.50
            
            vendedores_registrados.append(vendedor)
            montos_ventas.append(monto_operacion)
            
            print(f"Venta exitosa. Quedan {stock_producto} unidades.")
            
        elif pregunta == "no":
            print("Cerrando turno del vendedor...")
            break
            
        else:
            print("Opción inválida, respondé 'si' o 'no'.")

print("\n" + "="*30)
print(f"RESUMEN DE JORNADA")
print(f"Vendedores que operaron hoy: {vendedores_registrados}")
print(f"Unidades totales vendidas: {int(sum(montos_ventas) / 2500.50)}")
print(f"Total recaudado: ${sum(montos_ventas):.2f}")
print("="*30)