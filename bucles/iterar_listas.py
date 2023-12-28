
animales = ['turron','perro', 'gato', 'loro']
numeros = [ 10, 45, 33, 55]
    
for animal in animales:
    
    print(f'ahora la variable animal es {animal}')
    
for numero in numeros:
    resultado = numero + 10
    print(resultado)
    
    #iterar sobre dos listas del mismo tamaño al mismo tiempo
for  numero, animal in zip(numeros,animales ):
    print(f'recorriendo lista 1: {animal}')
    print(f'recorriendo lista 2: {numero}')
    
for num in range(5,10):
    print(num)
    
#recorrer una lista con su indice

for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'El indice es: {indice} y su valor es: {valor}')

#usando el else

for numero in numeros:
    print(f'ejectuando el ultimo bucle, valor actual: {numero}')
else:
    print('El bucle ha terminado gilipollas')