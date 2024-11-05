import math

#dados do problema
m = 3.4  #kg
vx, vy, vz = 7.3, 7.8, 8.9 #m/s
k = 9.9  #N/m
A = 4.8  #m

#calculando o módulo da velocidade inicial
v = math.sqrt(vx**2 + vy**2 + vz**2)

#calculando as energias
E1 = 0.5 * m * v**2
E2 = 0.5 * k * A**2

#calculando a razão
razao = E1 / E2

#imprimindo o resultado
print(razao)