#fazendo qualquer coisa para começar a aprender a sintaxe, nem sei o que é isso ok
from math import *

def func(x):
    x = x ** x
    return x

lista = [0, 0, 0, 0, 0]

for n in range(0, 5, 1):
    x = input()
    lista[n] = func(int (x))
    print(lista[n])

print(lista)

lista.sort()
print(f'\nlista em ordem: {lista}')

lista.reverse()
print(f'\nlista ao contrario: {lista}')