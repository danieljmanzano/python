#programa basico de achar o maior numero em um vetor
#por algum motivo nao funciona com numero grande (nao chega nem em 100 plmds)
def maior(vetor, tam):
    aux = vetor[0]
    for i in range(1, int(tam), 1):
        if vetor[i] > aux:
            aux = vetor[i]
    return aux

print("digite o tamanho de seu vetor")
tam:int = input()
vetor = []
print("digite os numeros do vetor")
for i in range (0, int(tam), 1):
    aux:int = input()
    vetor.append(aux)

print(f"maior no vetor: {maior(vetor, int(tam))}")