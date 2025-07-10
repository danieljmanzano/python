'''
ideia de projeto de tratamento de dados (e machine learning):
    classificação de espécies de flores iris com base em medidas de sépalas e pétalas.
    de onde tirei o dataset: https://www.kaggle.com/datasets/uciml/iris

como essa é minha primeira vez fazendo algo do tipo, to tentando comentar tudo que posso.
 ^^ (pode parecer bobeira, mas espero usar isso para entender melhor futuramente se fizer algo melhor)

no sentido geral, nada do que fiz aqui foi uma ideia totalmente original/própria. o que tentei alcançar com isso era simplesmente
começar a entender um pouco desse assunto fazendo algo interessante e que faz sentido. eventualmente quero desenvolver algo desse 
tipo por conta própria sabendo do que estou fazendo. por enquanto tamo de brincation aqui
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

# carrega o dataset a partir do arquivo desejado
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
    
# gera as visualizações dos dados (cria plots de gráficos relativos aos dados do dataset inicial)
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
    print("="*50)

    if 'Id' in ds.columns:
        ds = ds.drop('Id', axis=1) # tira a coluna de id

    # separar features (X) e alvo (y) -----------------------------------------------------------------------------------------------
    X = ds.drop('Species', axis=1) # X é formado por todas as colunas menos a de espécies
    y = ds['Species'] # y é apenas a coluna de espécies
    print(f"\nshape de X: {X.shape}\nshape de y: {y.shape}\n")

    # codificar a variável alvo (label encoding) ------------------------------------------------------------------------------------
    from sklearn.preprocessing import LabelEncoder # scikit-learn precisa que o alvo seja numérico
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)
    # verificando o que foi alterado (não precisa de fato, só para ver mesmo)
    print("alvo original (y):", y.unique())
    print("alvo codificado (y_encoded):", np.unique(y_encoded))
    print("mapeamento de classes:", list(le.classes_))

    # dividir em dados de treino e teste --------------------------------------------------------------------------------------------
    # test_size=0.3 significa que 30% dos dados serão para teste e 70% para treino
    # random_state=42 garante que a divisão seja sempre a mesma
    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.3, random_state=42, stratify=y_encoded)
    print("shape de X_train:", X_train.shape)
    print("shape de X_test:", X_test.shape)
    print("shape de y_train:", y_train.shape)
    print("shape de y_test:", y_test.shape)
    print("\n" + "="*50 + "\n")

    # escolher e treinar um modelo (no nosso caso, usando k-nearest neighbors) ------------------------------------------------------
    # instanciando o modelo. pelos testes locais, k=5 gera a maior acurácia (0.9778)
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train) # <-------- treinamento de fato aqui

    # avaliação do modelo -----------------------------------------------------------------------------------------------------------
    y_pred = knn.predict(X_test) # usa o modelo treinado para prever os resultados do teste
    # calculando métricas
    acuracia = accuracy_score(y_test, y_pred)
    print(f"acurácia do modelo: {acuracia:.4f}")
    print(f"isso significa que o modelo acertou {acuracia:.2%} das previsões no conjunto de teste.")
    print("\n" + "="*50 + "\n")

    # relatório de classificação ----------------------------------------------------------------------------------------------------
    print("relatório de classificação:")
    print(classification_report(y_test, y_pred, target_names=le.classes_)) # "target names" mostra os nomes das classes

    # matriz de confusão ------------------------------------------------------------------------------------------------------------
    print("gerando heatmeap da matriz de confusão...")
    cm = confusion_matrix(y_test, y_pred)
    # usa um heatmap para melhor visualização
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=le.classes_, yticklabels=le.classes_)
    plt.xlabel('Previsto')
    plt.ylabel('Real')
    plt.title('Matriz de Confusão')
    plt.savefig("iris_matriz_confusao.png") # salva a matriz como imagem
    plt.show()


if __name__ == "__main__":
    main()
