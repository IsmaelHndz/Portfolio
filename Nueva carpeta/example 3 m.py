import xml.etree.ElementTree as ET

def precio_promedio_productos(archivo):
    precios = []
    tree = ET.parse(archivo)
    root = tree.getroot()
    for producto in root.findall('producto'):
        precio = float(producto.find('precio').text)
        precios.append(precio)
    return sum(precios) / len(precios)

# Ejemplo de uso
archivo_xml = "datos.xml" # Asegúrate de tener un archivo XML con contenido
print(precio_promedio_productos(archivo_xml))