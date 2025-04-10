import dado

class RolaDados:
    def __init__(self):
        self.dados = []

    # cria n dados. padrão: 1 dado, 6 lados e a seed (gerador para número aleatório) é 0
    def rolaDados(self, n=1, seed=0):
        for i in range(n):
            self.dados[i] = dado.Dado(6, seed)

    # simula a rolagem de n dados. retorna uma lista com os dados
    def rolar(self, quais=[]):
        for i in quais:
            if i < len(self.dados):
                self.dados[i].rolar()

        return self.dados
    


