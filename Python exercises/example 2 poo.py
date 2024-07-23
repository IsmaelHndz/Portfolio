class Rectangulo:
    def _init_(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

# Ejemplo de uso
rectangulo1 = Rectangulo(5, 3)
print(rectangulo1.calcular_area())
print(rectangulo1.calcular_perimetro())