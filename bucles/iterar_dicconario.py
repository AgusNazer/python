
#como iterar un diccionario
dicc = {
    'nombre': 'agus',
    'apellido': 'verga',
    'edad': 32
    }

#obtener solo las claves
for key in dicc:
    key 
    print(f'la clave es: {key}')

# obtener clave y valor
for datos in dicc.items():
    key = datos[0]
    value = datos[1]
    print(f'la clave es: {key} y su valor es: {value}')