#def uniquevalue(original_value):
import random

def imprimecosas():
    print('hola')
    print('chau')
    print('tengo hambre')

def comparar_wumpus(posicion_wumpus):
    while True:
        objeto = random.randint(1,17)
        if (objeto != posicion_wumpus):
            break
    return objeto

wumpus= random.randint(1,17)
arrow = comparar_wumpus(wumpus)

print (wumpus)
print(f'{arrow}')
def sumar(a, b):
    suma=a+b
    return suma
