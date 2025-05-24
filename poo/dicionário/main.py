from grafo import Grafo

def main():
    g = Grafo()
    g.ler_entrada()
    # g.print_grafo() # descomentar para debug

    for origem in g.ordem_cidades:
        distancias, anteriores = g.dijkstra(origem)
        g.print_resultados(origem, distancias, anteriores)
        print("-" * 45)

if __name__ == "__main__":
    main()
