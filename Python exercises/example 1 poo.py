class Producto:
    def _init_(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def calcular_total(self):
        return self.precio * self.cantidad

# Ejemplo de uso
producto1 = Producto("Camisa", 20, 3)
print(producto1.calcular_total())