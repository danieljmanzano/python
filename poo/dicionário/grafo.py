import heapq

class Grafo:
    def __init__(self):
        self.grafo = {}
        self.ordem_cidades = [] # usada para print. meio hardcode mas é pra ficar como no runcodes


    def dijkstra(self, inicio):
        distancias = {v: float('inf') for v in self.grafo} # incializa distâncias como infinito
        distancias[inicio] = 0
        anteriores = {v: None for v in self.grafo}
        fila = [(0, inicio)]

        while fila:
            distancia_atual, vertice_atual = heapq.heappop(fila)

            for vizinho, peso in self.grafo[vertice_atual].items():
                distancia = distancia_atual + peso
                if distancia < distancias[vizinho]:
                    distancias[vizinho] = distancia
                    anteriores[vizinho] = vertice_atual
                    heapq.heappush(fila, (distancia, vizinho))

        return distancias, anteriores


    def reconstruir_caminho(self, anteriores, origem, destino):
        caminho = []
        atual = destino
        while atual != origem:
            caminho.insert(0, atual)
            atual = anteriores.get(atual)
            if atual is None:
                return []  # caminho indisponível
        caminho.insert(0, origem)
        return caminho

    def ler_entrada(self):
        cidade_atual = None
        try:
            while True:
                linha = input()
                if not linha.strip():
                    continue

                # CABEÇALHO (cidade)
                if not linha.startswith((' ', '\t')):
                    cidade = linha.strip()
                    self.grafo[cidade] = {}
                    self.ordem_cidades.append(cidade)   # <— só aqui
                    cidade_atual = cidade

                # ARESTA (vizinho)
                else:
                    partes = linha.strip().split()
                    vizinho, distancia = partes[0], float(partes[1])
                    self.grafo[cidade_atual][vizinho] = distancia
                    if vizinho not in self.grafo:
                        self.grafo[vizinho] = {}
        except EOFError:
            pass

    # método de print para debug
    def print_grafo(self):
        print("==== Grafo ====")
        for cidade, vizinhos in self.grafo.items():
            print(f"{cidade}:")
            for vizinho, distancia in vizinhos.items():
                print(f"  -> {vizinho} : {distancia}")
        print("================")

    # método de print para o exercício
    def print_resultados(grafo_obj, origem, distancias, anteriores):
        for destino in grafo_obj.ordem_cidades:   # <— iterando só as cidades de cabeçalho
            if destino == origem:
                continue
            print(f"{origem} para {destino}")
            print(f"\tDistancia: {distancias[destino]:.1f}".replace('.', ','))
            caminho = grafo_obj.reconstruir_caminho(anteriores, origem, destino)
            if caminho:
                print(f"\tCaminho: {' --> ' + ' --> '.join(caminho[1:])}")
            else:
                print("\tCaminho: Indisponível")
