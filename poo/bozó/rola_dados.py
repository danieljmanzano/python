from random import Random
from dado import Dado

class RolaDados:
    """
    Classe auxiliar que permite gerenciar um conjunto de vários dados simultaneamente.
    Operações como rolar alguns dos dados ou exibir o resultado de todos eles são implementadas.
    """
    
    def __init__(self, n, seed=0):
        """
        Construtor que cria e armazena vários objetos do tipo Dado.
        @param n: Número de dados a serem criados
        @param seed: Semente para criar dados. Se for 0 cria sem semente
        """
        self.dados = []
        if seed != 0:
            rd = Random()
            rd.seed(seed)
        
        for _ in range(n):
            if seed == 0:
                self.dados.append(Dado())
            else:
                self.dados.append(Dado(6, rd.randint(1, 10000)))
    
    def rolar(self, quais=None):
        """
        Rola alguns ou todos os dados.
        @param quais: Lista de booleanos indicando quais dados devem ser rolados (opcional)
        @return: Valores de todos os dados após a rolagem
        """
        if quais is None:
            return [d.rolar() for d in self.dados]
        
        resultados = []
        for i in range(min(len(quais), len(self.dados))):
            if quais[i]:
                resultados.append(self.dados[i].rolar())
            else:
                resultados.append(self.dados[i].get_lado())
        return resultados
    
    def rolar_string(self, s):
        """
        Rola alguns dos dados com base em uma string de entrada.
        @param s: String com os números dos dados a serem rolados (ex: "1 3 5")
        @return: Valores de todos os dados após a rolagem
        """
        b = [False] * len(self.dados)
        try:
            indices = [int(num)-1 for num in s.split() if num.isdigit()]
            for i in indices:
                if 0 <= i < len(b):
                    b[i] = True
        except ValueError:
            pass
        return self.rolar(b)
    
    def __str__(self):
        """Retorna uma representação string de todos os dados."""
        linhas = []
        dados_str = [str(d).split('\n') for d in self.dados]
        
        for i in range(5):  # Cada dado tem 5 linhas na representação
            linha = ""
            for dado in dados_str:
                if i < len(dado):
                    linha += dado[i] + "    "
            linhas.append(linha)
        
        return "\n".join(linhas)

# teste da classe. 
if __name__ == "__main__":
    rd = RolaDados(5)
    rd.rolar()
    print("1          2          3          4          5")
    print(rd)
    
    while True:
        try:
            s = input("Digite os dados a rolar (ex: 1 3 5) ou Enter para todos: ")
            if not s.strip():
                rd.rolar()
            else:
                rd.rolar_string(s)
            print(rd)
        except (EOFError, KeyboardInterrupt):
            break