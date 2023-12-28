diccionario = {
    'nombre': 'agus',
    'apellido': 'q se yo',
    'cuan_crack_soy': 1000
}

claves = diccionario.keys()
#obtener un objeto con get ( si no ecnuentra nada el programa continua)
claves = diccionario.get('nombre')

print(claves) 