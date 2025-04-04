from table import Table

vetor = list(map(int, input().split())) 
# explicaçao dessa brincadeira de cima:
    # list faz que o retorno de map seja uma lista
    # map transforma o que ta no segundo argumento em int
    # input recebe tudo como uma coisa só, mas o .split separa tudo em coisas diferentes (sem nada dentro, ele trata os espaços)
    # entao a string de input é separada pelo split, as separações sao transformadas em int pelo map e entao o list coloca numa lista
tam = len(vetor)

t = Table()
t.set_table(vetor, tam)
t.print_table()

comandos = input().strip() # le a linha de comandos. o '.strip' meio que formata a entrada de um jeito mais daora, tira espaço extra do inicio e fim
for cmd in comandos: # vai andando no comandos pegando cada letra 
    if cmd == 'u':
        t.move_up()
    elif cmd == 'd':
        t.move_down()
    elif cmd == 'l':
        t.move_left()
    elif cmd == 'r':
        t.move_right()
    else:
        continue # ignora comando invalido
    
    t.print_table() # toda iteração printa a tabela


print(f"Posicao final: {t.resultado()}")

