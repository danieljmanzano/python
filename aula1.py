import random
lista = [1, 2, 'c', 4]

print("hello world ah lelek lek lek lek lek lek lek")

for i in range(0, 4, 1):
    print(lista[i])
print("\n")
lista.append(1)
lista[i + 1] = "oi"

for i in range(0, 5, 1):
    print(lista[i])
print("\n")
lista.remove(2)

for i in range(0, 2, 1):
    print(lista[i])

a = {}
a[1] = "chave"
a["chave"] = "segredo"
variavel = input()
print(a[variavel])

flag = 0
lista_rand = []
for i in range(0, 100000001):
    lista_rand.append(i)
while True:
    n = random.choice(lista_rand)
    
    flag += 1
    print(n)
    if(n == 32145): break

print("parabens")
print(f"{flag} tentativas")
#kkkkkkkkkk que boberaiada 
#testes de coisas que tava vendo durante a aula do data