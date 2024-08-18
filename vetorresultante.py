import numpy #biblioteca usada para calcular o valor do vetor
import sigfig #biblioteca usada para arredondar o valor do vetor

vetor = numpy.array([1.1, 9.1]) #guardo os valores de vx e vy
modvetor = numpy.linalg.norm(vetor) #calculo o valor de v com base nos dois anteriores
modvetor = round(modvetor, 1) #arredondo o resultado final
print(modvetor) #printo