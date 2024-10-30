import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Criar um vetor t
t = np.linspace(0, 10, 100)  # Intervalo de 0 a 10 com 100 pontos

# Definir a função f(t)
x = np.cos(t)      # Componente x
y = np.sin(t)      # Componente y
z = np.exp(-t)     # Componente z

# Criar uma figura e um eixo 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plotar os dados
ax.plot(x, y, z, label='f(t) = (cos(t), sin(t), e^-t)', color='b')

# Ajustar os limites dos eixos
ax.set_xlim([-5, 5])   # Limites do eixo X
ax.set_ylim([-5, 5])   # Limites do eixo Y
ax.set_zlim([-5, 5])    # Limites do eixo Z

# Adicionar rótulos e título
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_zlabel('Eixo Z')
ax.set_title('Gráfico da função f(t) = (cos(t), sin(t), e^-t)')
ax.legend()

# Mostrar o gráfico
plt.show()

#tentando estudar calc tive que pegar esse codigo pra plotar o grafico dum bagulho que eu nao consegui desenhar
#ja fica de lição pra python tambem. bem daora