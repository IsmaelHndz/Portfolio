def total_ventas_por_producto(ventas):
    total_por_producto = {}
    for venta in ventas:
        producto = venta['producto']
        cantidad = venta['cantidad']
        precio_unitario = venta['precio_unitario']
        total_por_producto[producto] = total_por_producto.get(producto, 0) + cantidad * precio_unitario
    return total_por_producto

# Ejemplo de uso
ventas = [
    {'producto': 'Camisa', 'cantidad': 5, 'precio_unitario': 20},
    {'producto': 'Pantalón', 'cantidad': 3, 'precio_unitario': 30},
    {'producto': 'Camisa', 'cantidad': 2, 'precio_unitario': 20}
]
print(total_ventas_por_producto(ventas))