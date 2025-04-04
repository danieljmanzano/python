# exercicio identico ao tabuleiro que fizemos em java antes. logica identica, só traduzi pra python
# por isso, vai ficar faltando comentario aqui. as explicações tao la no em java
from math import sqrt


class Table:
    def __init__(self):
        self.i = 0 # posição i referente ao 0 na matriz imaginaria
        self.j = 0 # posição j    "    "    "    "    "    "
        self.pos = 0 # posição real de 0 no vetor tabuleiro
        self.tabuleiro = [] # vetor que guarda os numeros do tabuleiro
        self.tam = 0 # quantas posições tem o tabuleiro
        self.lado = 0 # tamanho do lado da matriz imaginaria (do suposto tabuleiro)


    def set_table(self, tabuleiro, tam):
        self.tabuleiro = tabuleiro
        self.tam = tam
        self.lado = int(sqrt(tam))

        # aqui em baixo defino tudo referente à posição vazia do tabuleiro
        for k in range(tam):
            if tabuleiro[k] == 0:
                self.i = k % self.lado
                self.j = int(k / self.lado)
                self.pos = k
                break
        
    def move_up(self):
        # para nao ter que repetir os self toda vez, faço essa definiçao aqui de baixo
        tabuleiro, pos, lado, j = self.tabuleiro, self.pos, self.lado, self.j 
        
        if (j != lado - 1):
            self.j += 1
            self.tabuleiro[pos] = tabuleiro[pos + lado]
            self.tabuleiro[pos + lado] = 0
            self.pos += lado
    
    def move_down(self):
        tabuleiro, pos, lado, j = self.tabuleiro, self.pos, self.lado, self.j
        
        if (j != 0): 
            self.j -= 1
            self.tabuleiro[pos] = tabuleiro[pos - lado]
            self.tabuleiro[pos - lado] = 0
            self.pos -= lado

    def move_left(self):
        tabuleiro, pos, lado, i = self.tabuleiro, self.pos, self.lado, self.i
        
        if (i != lado - 1):
            self.i += 1
            self.tabuleiro[pos] = tabuleiro[pos + 1]
            self.tabuleiro[pos + 1] = 0
            self.pos += 1

    def move_right(self):
        tabuleiro, pos, i = self.tabuleiro, self.pos, self.i

        if (i != 0):
            self.i -= 1
            self.tabuleiro[pos] = tabuleiro[pos - 1]
            self.tabuleiro[pos - 1] = 0
            self.pos -= 1


    def print_table(self):
        lado, tabuleiro = self.lado, self.tabuleiro
        # Garante que lado seja inteiro
        lado = int(lado)
        
        # Calcula a largura de cada célula baseado no maior número
        max_num = max(abs(num) for num in tabuleiro) if tabuleiro else 0
        cell_width = len(str(max_num)) + 2  # +2 para espaçamento
        
        # Cria a linha divisória
        linha_divisoria = "+" + ("-" * cell_width + "+") * lado
        
        for i in range(lado):  # Para cada linha da matriz imaginária
            print(linha_divisoria)
            print("|", end="")
            for j in range(lado):  # Para cada coluna da matriz imaginária
                index = i * lado + j
                # Formata o número centralizado na célula
                print(f"{tabuleiro[index]:^{cell_width}}|", end="")
            print()  # Nova linha após cada linha do tabuleiro
        
        print(linha_divisoria)
        print()  # Linha vazia adicional para separação    


    def resultado(self):
        tam, tabuleiro = self.tam, self.tabuleiro

        for i in range(tam - 1):
            if tabuleiro[i] > tabuleiro[i + 1]:
                return False
            
        return True