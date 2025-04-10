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

        # aqui embaixo defino tudo referente à posição vazia do tabuleiro
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


    # para printar o tabuleiro, tenho que formatar a saída de um jeito muito específico de acordo com o exercício
    def print_table(self):
        lado, tabuleiro = self.lado, self.tabuleiro
        lado = int(lado) # garantindo que o lado seja inteiro (sempre é, mas pra dar certo de usar o lado ali nos 'range' de baixo sem dar erro)
                
        linha_divisoria = "+" + ("------+") * lado
        
        for i in range(lado):  
            print(linha_divisoria)
            print("|", end="") # isso aqui (end ="") serve pra nao quebrar linha

            for j in range(lado): 
                index = i * lado + j

                if (tabuleiro[index] != 0): # para centralizar o número do "jeito certo" (de acordo com o exercício), fiz casos em que ele pode ter até 4 dígitos
                    if (len(str(tabuleiro[index])) == 1):
                        print(f"   {tabuleiro[index]}  |", end="")
                    elif (len(str(tabuleiro[index])) == 2):
                        print(f"  {tabuleiro[index]}  |", end="")
                    elif (len(str(tabuleiro[index])) == 3): 
                        print(f"  {tabuleiro[index]} |", end="")
                    else:   
                        print(f" {tabuleiro[index]} |", end="")

                else: # caso seja 0, imprimo o espaço vazio com a largura correta
                    print("      |", end="")

            print() # quebra linha
        
        print(linha_divisoria)
        print()  
        

    def resultado(self):
        tam, tabuleiro = self.tam, self.tabuleiro

        for i in range(tam - 1):
            if tabuleiro[i] > tabuleiro[i + 1]:
                return False
            
        return True