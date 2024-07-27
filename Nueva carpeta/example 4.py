def total_ventas_combinadas(ventas1, ventas2):
    ventas_combinadas = {}
    for venta in ventas1 + ventas2:
        producto = venta['producto']
        cantidad = venta['cantidad']
        precio_unitario = venta['precio_unitario']
        ventas_combinadas[producto] = ventas_combinadas.get(producto, 0) + cantidad * precio_unitario
    return ventas_combinadas

# Ejemplo de uso
ventas1 = [
    {'producto': 'Camisa', 'cantidad': 5, 'precio_unitario': 20},
    {'producto': 'Pantalón', 'cantidad': 3, 'precio_unitario': 30},
    {'producto': 'Camisa', 'cantidad': 2, 'precio_unitario': 20}
]
ventas2 = [
    {'producto': 'Zapatos', 'cantidad': 2, 'precio_unitario': 50},
    {'producto': 'Camisa', 'cantidad': 3, 'precio_unitario': 20}
]
print(total_ventas_combinadas(ventas1, ventas2))