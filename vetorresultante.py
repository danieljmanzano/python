#atividade de fisica, precisava de um codigo em maple ou mathematica ou python resolvendo o problema
#tendo o valor de V (vetor) nos eixos x e y, tenho que calcular o modulo dele arredondado (valores foram 1.1 e 9.1, saída esperada é 9.2)

import numpy #biblioteca usada para calcular o valor do vetor
import sigfig #biblioteca usada para arredondar o valor do vetor
a = float(input())
b = float(input())
vetor = numpy.array([a, b]) #guardo os valores de vx e vy
modvetor = numpy.linalg.norm(vetor) #calculo o valor de v com base nos dois anteriores
modvetor = round(modvetor, 1) #arredondo o resultado final
print(modvetor) #printo