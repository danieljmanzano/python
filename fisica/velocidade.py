import numpy
import sigfig
import math

#exercicio de fisica. tenho tres expressoes para funções que representam posição em função do tempo, uma para cada dimensão (x(t), y(t) e z(t))
#a partir das expressões e dos valores dados para os parametros que fazem parte das expressões, preciso calcular o modulo do vetor velocidade resultante

a = float(input()) # os parametros sao dados como inputs no programa
b = float(input())
t = float(input())
w = float(input())

#para descobrir a velocidade, derivo as funções do vetor posição todas em função de tempo
x = -a * w * math.sin(w * t) # x(t) = a * cos(w * t) -> dx/dt = -a * w * sin(w * t)
y = a * w * math.cos(w * t) # y(t) = a * sin(w * t) -> dy/dt = a * w * cos(w * t)
z = 2 * b * t # z(t) = b * t² -> dz/dt = 2 * b * t

#tendo as velocidades nas diferentes coordenadas, calculo o vetor resultante e seu módulo arredondado
vetor = numpy.array([x, y, z])
modvetor = numpy.linalg.norm(vetor)
modvetor = round(modvetor, 1)

print(f"\nvalor da velocidade em x: {x}")
print(f"valor da velocidade em y: {y}")
print(f"valor da velocidade em z: {z}")
print(f"valor do modulo do vetor aproximado: {modvetor}")




