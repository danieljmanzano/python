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

# Lê os comandos de movimento
comandos = input().strip()  # Lê a linha de comandos (ex: "dr")

# Executa cada comando
for cmd in comandos:
    if cmd == 'u':
        t.move_up()
    elif cmd == 'd':
        t.move_down()
    elif cmd == 'l':
        t.move_left()
    elif cmd == 'r':
        t.move_right()
    else:
        continue  # Ignora comandos inválidos
    
    t.print_table()  # Mostra o tabuleiro após cada movimento

# Verifica o resultado final
print(f"Posicao final: {t.resultado()}")

