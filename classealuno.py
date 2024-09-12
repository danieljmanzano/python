#nem sei o que to fazendo, só pra tentar exercitar ideia de classe e um pouco de função
#recebo informaçoes sobre individuos e com base em uma escolha do usuario vou tentar retornar uma que ta relacionada à entrada (idade no caso)
class aluno():
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

def buscainfo(busca, alunos):
    flag = 0
    for i in range (0, len(alunos), 1):
        if busca == alunos[i].nome:
            flag = 1
            return i
    if flag == 0:#se nao achou como nome
        for i in range (0, len(alunos), 1):
            if busca == alunos[i].cpf:
                flag = 1
                return i
    if flag == 0:#se nao achou nada
        return -1

alunos = []

print("digite quantos alunos quer registrar")
num:int = input()

print("digite as informações dos alunos (nome, idade, cpf)")
for i in range(0, int(num), 1):
    nome:str = input()
    idade:int = input()
    cpf:str = input() #muito paia um input pra cada variavel... tem como dale tipo um scanf aqui e ler umas 50 de uma vez? 

    alunoaux = aluno(nome, idade, cpf)
    alunos.append(alunoaux)

print("digite uma informação de um aluno especifico que quer encontrar")
busca:str = input()
if buscainfo(busca, alunos) == -1: 
    print("nao encontrado!")
else:
    print(f"a idade dele(a) é: {alunos[buscainfo(busca, alunos)].idade}") #ce loco vai tomano
