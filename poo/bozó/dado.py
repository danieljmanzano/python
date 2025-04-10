import random

class Dado:
    # cria um dado. padrão: 6 lados e a seed (gerador para número aleatório) é 0
    def __init__(self, n=6, seed=0): 
        self.n = n      
        self.seed = random.seed(seed)
        self.atual = 0

    # simula a rolagem de um dado. retorna um número aleatório que possa ser o valor do lado do dado
    def rolar(self):
        self.atual = random.randint(1, self.n)
        return self.atual

    # retorna o valor do lado atual do dado
    def getLado(self):
        return self.atual

    # representa o lado atual do dado como uma string
    def toString(self):
        s = "+-----+\n"

        s010 = "|  *  |\n"
        s100 = "|*    |\n"
        s001 = "|    *|\n"
        s000 = "|     |\n"
        s101 = "|*   *|\n"
        s111 = "|* * *|\n"

        if (self.n != 6):
            print("Não há representação para esses dados")

        if (self.atual == 1):
            s = s000 + s010 + s000
        elif (self.atual == 2):
            s = s100 + s000 + s001
        elif (self.atual == 3):
            s = s100 + s010 + s001
        elif (self.atual == 4):
            s = s101 + s000 + s101
        elif (self.atual == 5): 
            s = s101 + s010 + s101
        elif (self.atual == 6):
            s = s111 + s000 + s111

        s += "+-----+\n"

        return s
        