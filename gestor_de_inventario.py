from colorama import Back, Fore, Style, init
init(autoreset=True)


precio_producto = 2500.50
stock_producto = 10
registro_ventas = [{"vendedor": "Ana", "monto": 5000.0}]

def procesar_venta(precio, unidades, stock_actual):
    """
    Valida si hay stock suficiente y calcula el monto de la operación.
    
    Parámetros:
    precio (float): Precio unitario del producto.
    unidades (int): Cantidad de productos que el usuario desea comprar.
    stock_actual (int): Cantidad de productos disponibles en el inventario.
    
    Retorna:
    tuple: (nuevo_stock, monto) si la venta es exitosa.
    tuple: (None, 0) si el stock es insuficiente.
    
    """
    if unidades > stock_actual:
        return None, 0
    
    nuevo_stock = stock_actual - unidades
    monto = unidades * precio
    return nuevo_stock, monto
    
def resumen_jornada(registro_ventas):
    """
    Recorre el historial de ventas y genera un mensaje con el total recaudado.
    
    Parámetros:
    registro_ventas (list): Una lista que contiene diccionarios con las ventas del día.
    
    Retorna:
    str: Un mensaje formateado con el monto total acumulado.
    
    """
    total = sum(venta["monto"] for venta in registro_ventas)
    return f"{Fore.CYAN}Total recaudado en la jornada: ${total:,.2f}"

while stock_producto > 0:
    vendedor = input("\nIngresá tu nombre: ").strip().title()
    
    if not vendedor:
        print(f" {Fore.RED}No ingresaste tu nombre, intetalo nuevamente")
        continue
        
    pregunta = input(f"Hola {vendedor}, ¿querés realizar una venta? (si/no): ").strip().lower()
    
    if pregunta == "si":
        entrada_unidades = input("¿Cuantas unidades desea vender? ")
        
        if not entrada_unidades.isdigit():
            print(f"{Fore.RED}ERROR: Debe ingresar un número válido.")
            continue
        
        unidades = int(entrada_unidades)
        nuevo_stock, monto_operacion = procesar_venta(precio_producto, unidades, stock_producto)
        
        if nuevo_stock is not None:
            stock_producto = nuevo_stock
            registro_ventas.append({"vendedor": vendedor, "monto": monto_operacion})
            print(f"{Fore.CYAN}Venta exitosa. Quedan {stock_producto} unidades.")
        else:
            print(f"{Fore.RED}ERROR: Stock insuficiente para realizar la operación.")
            
    elif pregunta == "no":
        print(f"{Fore.CYAN}Cerrando turno del vendedor...")
        break
            
    else:
        print(f"{Fore.RED}Opción inválida, respondé 'si' o 'no'.")

print("\n" + "="*30)
print("="*30)
print(resumen_jornada(registro_ventas))