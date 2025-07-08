'''
ideia de projeto de tratamento de dados (e machine learning):
    classificação de espécies de flores iris com base em medidas de sépalas e pétalas.
    de onde tirei o dataset: https://www.kaggle.com/datasets/uciml/iris

como essa é minha primeira vez fazendo algo do tipo, to tentando comentar tudo que posso.
 ^^ (pode parecer bobeira, mas espero usar isso para entender melhor futuramente se fizer algo melhor)
'''

# bibliotecas para manipulação e análise de dados
import pandas as pd
import numpy as np

# bibliotecas para visualização de dados
import matplotlib.pyplot as plt
import seaborn as sns

# módulos do scikit-learn para machine learning
# para dividir o dataset em treino e teste
from sklearn.model_selection import train_test_split
# modelo de classificação KNN (K-Nearest Neighbors)
from sklearn.neighbors import KNeighborsClassifier
# para avaliar o desempenho do modelo
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# definições da visualização dos gráficos
sns.set_style("dark") # estilo dos gráficos
plt.rcParams['figure.figsize'] = (10, 6) # tamanho padrão de figuras nos gráficos


def carrega_dataset(caminho_do_arquivo):
    try:
        df_iris = pd.read_csv(caminho_do_arquivo)
        print("informações gerais do arquivo: ")
        df_iris.info()
        print(f"\n" + "="*50 + "\n")
        return df_iris
    
    except:
        print(f"erro em carregar arquivo: {caminho_do_arquivo}")
        return None
    
def visualizacao(dataset):
    # visão geral com pairplot
    print("gerando o pairplot... (isso pode levar alguns segundos)")
    sns.pairplot(dataset.drop("Id", axis=1), hue="Species", markers=["o", "s", "D"])
    plt.suptitle("Pairplot do Dataset Iris", y=1.02) # título
    plt.savefig("pairplot") # salva como pairplot.png

    # comparando a distribuição de cada característica por espécie
    print("\ngerando boxplots...")
    plt.figure(figsize=(12, 10))
    # gráfico 1: comprimento da sépala
    plt.subplot(2, 2, 1) # (2 linhas, 2 colunas, primeiro gráfico)
    sns.boxplot(x="Species", y="SepalLengthCm", data=dataset)    
    plt.title("Comprimento da Sépala por Espécie")
    # gráfico 2: largura da sépala
    plt.subplot(2, 2, 2) # (2 linhas, 2 colunas, segundo gráfico)
    sns.boxplot(x="Species", y="SepalWidthCm", data=dataset)
    plt.title("Largura da Sépala por Espécie")
    # gráfico 3: comprimento da pétala
    plt.subplot(2, 2, 3) # (2 linhas, 2 colunas, terceiro gráfico)
    sns.boxplot(x="Species", y="PetalLengthCm", data=dataset)
    plt.title("Comprimento da Pétala por Espécie")
    # gráfico 4: largura da pétala
    plt.subplot(2, 2, 4) # (2 linhas, 2 colunas, quarto gráfico)
    sns.boxplot(x="Species", y="PetalWidthCm", data=dataset)
    plt.title("Largura da Pétala por Espécie")
    # ajusta os gráficos para evitar sobreposição
    plt.tight_layout()
    plt.savefig("boxplots") # salva como comparação.png

    # heatmap de correlação
    print("\ngerando heatmap de correlação...")
    # cálculo de correlação nas colunas numéricas
    correlacao = dataset.drop("Id", axis=1).corr(numeric_only=True)
    # uso do seaborn para plotar o heatmap em si
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlacao, annot=True, cmap='coolwarm', linewidths=.5)
    plt.title("Mapa de Calor da Correlação entre as Características")
    plt.savefig("heatmap") # salva como heatmap.png

    # mostra todos os plots
    plt.show()


def main():
    caminho_do_arquivo = input()
    ds = carrega_dataset(caminho_do_arquivo)
    visualizacao(ds)


if __name__ == "__main__":
    main()
