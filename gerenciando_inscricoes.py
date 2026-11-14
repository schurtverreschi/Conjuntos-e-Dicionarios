participantes = {
    "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"},
    "Workshop 2": {"Fernanda", "Gustavo", "Helena"},
}

nome_remover = input("Nome do participante a ser removido: ").title()
encontrado = False

for workshop, inscritos in participantes.items():
    if nome_remover in inscritos:
        inscritos.discard(nome_remover)
        print(f"\n{nome_remover} removido(a) de {workshop} com sucesso.")
        encontrado = True
        break

if not encontrado:
    print("\nNome informado não encontrado.")

print("\nLista atualizada de participantes:\n")
for workshop, inscritos in participantes.items():
    print(f"{workshop}: {inscritos}")


# Faça como eu fiz: gerenciando inscrições de um workshop

# Laura está organizando um workshop sobre tecnologia e precisa de um programa que permita remover participantes que desistiram do evento. O sistema armazena os participantes em um dicionário, onde cada chave é o nome e o valor é um conjunto com os dados do participante. O programa deve solicitar o nome de um participante e remover esse nome da lista de participantes registrados, caso exista.

# Exemplo de entrada:

# participantes = {
#     "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"},
#     "Workshop 2": {"Fernanda", "Gustavo", "Helena"}
# }


# Nome do participante a ser removido: Carla

# Saída esperada:

# Lista atualizada de participantes:

# Workshop 1: {'Alice', 'Bruno', 'Diego'}
# Workshop 2: {'Fernanda', 'Gustavo', 'Helena'}
