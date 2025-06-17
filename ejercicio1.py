# Problema 1: Revisión de Stock en Bodega
#
# Una tienda tiene 5 productos y cada uno tiene una cantidad en stock.
# Debes realizar lo siguiente:
#
# 1. Crea una lista llamada 'stocks' con la cantidad de stock de cada producto (puedes usar los valores que desees).
# 2. Calcula la suma total de productos disponibles usando la función sum().
# 3. Verifica si todos los productos tienen más de 10 unidades:
#    - Usa un ciclo (for) y una condicional (if) para revisar cada elemento de la lista.
#    - Si algún producto tiene 10 o menos unidades, muestra un mensaje indicando cuál(es) producto(s) tienen bajo stock.
#    - Si todos tienen más de 10, muestra un mensaje indicando que el stock es suficiente.
#
# Escribe tu solución debajo de este comentario.
stocks = [25, 15, 8, 30, 10]

total_productos = sum(stocks)
print(f"La suma total de productos en bodega es: {total_productos}")
print("-" * 30) 

productos_bajo_stock = []
for indice, cantidad in enumerate(stocks):

  if cantidad <= 10:
    productos_bajo_stock.append(indice + 1)

if productos_bajo_stock:
  print("Se encontraron productos con bajo stock.")
  for producto_id in productos_bajo_stock:
  
    print(f" -> El Producto {producto_id} tiene bajo stock: {stocks[producto_id - 1]} unidades.")
else:
  print(" El stock de todos los productos es suficiente (más de 10 unidades).")
