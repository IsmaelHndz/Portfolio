class BaseDatos:
    def _init_(self):
        self.registros = []
    
    def agregar_registro(self, registro):
        self.registros.append(registro)
    
    def eliminar_registro(self, criterio):
        self.registros = [registro for registro in self.registros if criterio(registro) == False]
    
    def buscar_registro(self, criterio):
        return [registro for registro in self.registros if criterio(registro)]

# Ejemplo de uso
class Registro:
    def _init_(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

bd = BaseDatos()
bd.agregar_registro(Registro("Juan", 30))
bd.agregar_registro(Registro("Maria", 25))
bd.agregar_registro(Registro("Pedro", 40))

bd.eliminar_registro(lambda x: x.nombre == "Maria")
print(bd.buscar_registro(lambda x: x.edad > 30))