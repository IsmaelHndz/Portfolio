import json
import ast

def sort_by_price_ascending(json_string):
    datos = json.JSONDecoder().decode(json_string)
    for i in range(len(datos)):
        print (datos[i])

    for element in datos:
        price = element.split('"price:"')
    print(sorted(price))
    return None

print(sort_by_price_ascending('[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]'))

