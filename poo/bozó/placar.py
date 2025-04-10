class Placar:
    """
    Esta classe representa o placar de um jogo de Bozó. Permite que combinações
    de dados sejam alocadas às posições e mantém o escore de um jogador.
    """
    
    def __init__(self):
        self.POSICOES = 10
        self.placar = [0] * self.POSICOES
        self.taken = [False] * self.POSICOES
    
    def add(self, posicao, dados):
        """
        Adiciona uma sequencia de dados em uma determinada posição do placar.
        
        Args:
            posicao: Posição a ser preenchida (1-10). As posições 1 a 6 correspondem às quantidas
	                 de uns até seis, ou seja, as laterais do placar. As outas posições são: 7 - full hand;
	                 8 - sequencia; 9 - quadra; e 10 - quina
            dados: Um array de inteiros, de tamanho 5. Cada posição corresponde a um valor 
	               de um dado. Supões-se que cada dado pode ter valor entre 1 e 6. 
            
        Raises:
            ValueError: Se a posição estiver ocupada ou for inválida
        """
        if posicao < 1 or posicao > self.POSICOES:
            raise ValueError("Valor da posição ilegal")
        if self.taken[posicao-1]:
            raise ValueError("Posição ocupada")
            
        k = 0
        if 1 <= posicao <= 6:
            k = posicao * self.conta(posicao, dados)
        elif posicao == 7:  # full hand
            k = 15 if self.check_full(dados) else 0
        elif posicao == 8:  # sequencia
            k = 20 if self.check_seq_maior(dados) else 0
        elif posicao == 9:  # quadra
            k = 30 if self.check_quadra(dados) else 0
        elif posicao == 10:  # quina
            k = 40 if self.check_quina(dados) else 0
            
        self.placar[posicao-1] = k
        self.taken[posicao-1] = True
    
    def get_score(self):
        """Computa a soma dos valores obtidos, considerando apenas as posições que já estão ocupadas."""
        return sum(valor for i, valor in enumerate(self.placar) if self.taken[i])
    
    def conta(self, n, vet):
        """Conta quantas vezes o número n aparece no vetor."""
        return vet.count(n)
    
    def check_full(self, dados):
        """Verifica se os dados formam um full hand (trinca + par)."""
        v = sorted(dados.copy())
        return (v[0] == v[1] == v[2] and v[3] == v[4]) or (v[0] == v[1] and v[2] == v[3] == v[4])
    
    def check_quadra(self, dados):
        """Verifica se os dados formam uma quadra."""
        v = sorted(dados.copy())
        return (v[0] == v[1] == v[2] == v[3]) or (v[1] == v[2] == v[3] == v[4])
    
    def check_quina(self, dados):
        """Verifica se os dados formam uma quina (todos iguais)."""
        v = dados.copy()
        return all(x == v[0] for x in v)
    
    def check_seq_maior(self, dados):
        """Verifica se os dados formam uma sequência maior (1-5 ou 2-6)."""
        v = sorted(dados.copy())
        return all(v[i] == v[i+1]-1 for i in range(4))
    
    def __str__(self):
        """
        Retorna uma representação string do placar, mostrando posições livres e ocupadas.
        Exemplo:
        (1)    |   (7)    |   (4) 
        --------------------------
        (2)    |   20     |   (5) 
        --------------------------
        (3)    |   30     |   (6) 
        --------------------------
               |   (10)   |
               +----------+
        """
        s = ""
        for i in range(3):
            # Linha superior (posições 1-3, 7-9, 4-6)
            num = f"{self.placar[i]:4d}" if self.taken[i] else f"({i+1}) "
            s += f"{num}   |   "
            
            num = f"{self.placar[i+6]:4d}" if self.taken[i+6] else f"({i+7}) "
            s += f"{num}   |   "
            
            num = f"{self.placar[i+3]:4d}" if self.taken[i+3] else f"({i+4}) "
            s += f"{num}\n" + "-"*26 + "\n"
        
        # Última linha (posição 10)
        num = f"{self.placar[9]:4d}" if self.taken[9] else "(10)"
        s += f"       |   {num}   |\n"
        s += "       +----------+\n"
        return s