import heapq

def dijkstra(grafo, inicio):
    # Inicialização
    distancias = {v: float('inf') for v in grafo}
    distancias[inicio] = 0
    anteriores = {v: None for v in grafo}
    fila = [(0, inicio)]

    while fila:
        distancia_atual, vertice_atual = heapq.heappop(fila)

        for vizinho, peso in grafo[vertice_atual].items():
            distancia = distancia_atual + peso
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                anteriores[vizinho] = vertice_atual
                heapq.heappush(fila, (distancia, vizinho))

    return distancias, anteriores


def reconstruir_caminho(anteriores, origem, destino):
    caminho = []
    atual = destino
    while atual != origem:
        caminho.insert(0, atual)
        atual = anteriores.get(atual)
        if atual is None:
            return []  # Caminho indisponível
    caminho.insert(0, origem)
    return caminho


def print_resultados(origem, distancias, anteriores):
    for destino in distancias:
        if destino == origem:
            continue  # Não imprime o caminho para si mesmo
        print(f"{origem} para {destino}")
        print(f"\tDistancia: {distancias[destino]:.1f}")
        caminho = reconstruir_caminho(anteriores, origem, destino)
        if caminho:
            print(f"\tCaminho: {' --> ' + ' --> '.join(caminho[1:])}")
        else:
            print(f"\tCaminho: Indisponível")


def printa_grafo(grafo):
    print("==== Grafo ====")
    for cidade, vizinhos in grafo.items():
        print(f"{cidade}:")
        for vizinho, distancia in vizinhos.items():
            print(f"  -> {vizinho} : {distancia}")
    print("================")


def ler_entrada():
    grafo = {}
    entrada = []
    try:
        while True:
            linha = input()
            if linha:
                entrada.append(linha.strip())
            else:
                continue
    except EOFError:
        pass

    i = 0
    while i < len(entrada):
        cidade = entrada[i]
        i += 1
        grafo[cidade] = {}
        while i < len(entrada) and ' ' in entrada[i]:
            vizinho, dist = entrada[i].split()
            grafo[cidade][vizinho] = float(dist)
            if vizinho not in grafo:
                grafo[vizinho] = {}
            i += 1
    return grafo


def main():
    grafo = ler_entrada()

    for origem in grafo:
        distancias, anteriores = dijkstra(grafo, origem)
        print_resultados(origem, distancias, anteriores)
        print("-" * 45)  # separador
    
    
if __name__ == "__main__":
    main()
