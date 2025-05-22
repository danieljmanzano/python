from rola_dados import RolaDados
from placar import Placar
import sys

# codigo principal do conjunto todo aqui. basicamente, é a tradução pra python dos codigos que o professor forneceu em java
# aliás, o código em java ta na pasta "java" na subpasta "bozó". nao mexi em nada lá, só peguei o que o professor passou pra nós
# comentários e etc. aqui são baseados no código original, então talvez nem eu saiba explicar tudo que tem aqui

class Bozo:
    """
    Classe inicial do programa Bozó. Possui apenas o método main, que cuida da execução do jogo.
    """
    
    # Número de rodadas do jogo. Como o placar possui dez posições, são dez rodadas.
    NRODADAS = 10

    @staticmethod
    def main():
        """
        Método principal do programa. Cuida da execução do jogo e possui um laço,
        no qual cada iteração representa uma rodada do jogo. Em cada rodada, o jogador
        joga os dados até 3 vezes e depois escolhe a posição do placar que deseja preencher.
        No final das rodadas a pontuação total é exibida.
        """
        try:
            seed = int(input("Digite a semente (zero para aleatório): "))
            if seed == 0:
                seed = None
            
            rd = RolaDados(5, seed)
            pl = Placar()
            print(pl)
            
            for rodada in range(Bozo.NRODADAS):
                print(f"****** Rodada {rodada + 1}")
                input("Pressione ENTER para lançar os dados")
                print()

                # Primeira tentativa
                rd.rolar()
                print("1          2          3          4          5")
                print(rd)
                print()

                # Segunda tentativa
                print("Digite os números dos dados que quiser TROCAR. Separados por espaços.")
                muda = input().strip()
                rd.rolar_string(muda)
                print("1          2          3          4          5")
                print(rd)
                print()
                
                # Terceira tentativa
                print("Digite os números dos dados que quiser TROCAR. Separados por espaços.")
                muda = input().strip()
                values = rd.rolar_string(muda)
                print("1          2          3          4          5")
                print(rd)
                
                print("\n\n\n")
                print(pl)
                
                pos = 0
                while pos <= 0:
                    try:
                        pos = int(input("Escolha a posição que quer ocupar com essa jogada ===> "))
                        if pos > Bozo.NRODADAS or pos <= 0:
                            pos = 0
                            raise ValueError
                        pl.add(pos, values)
                    except (ValueError, Exception):
                        pos = 0
                        print("Valor inválido. Posição ocupada ou inexistente.")
                
                print("\n\n")
                print(pl)
            
            print("***********************************")
            print("***")
            print(f"*** Seu escore final foi: {pl.get_score()}")
            print("***")
            print("***********************************")

        except KeyboardInterrupt:
            print("\nJogo interrompido pelo usuário.")
            sys.exit(0)

if __name__ == "__main__":
    Bozo.main()