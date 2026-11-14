lista_laura = set(input("Lista de Laura: ").lower().split(", "))
lista_ana = set(input("Lista de Ana: ").lower().split(", "))

comum = lista_ana.intersection(lista_laura)
laura = lista_laura.difference(lista_ana)
ana = lista_ana.difference(lista_laura)

print(f"\nItens em ambas as listas: {', '.join(comum)}")
print(f"Itens exclusivos de Laura: {', '.join(laura)}")
print(f"Itens exclusivos de Ana: {', '.join(ana)}")

# Faça como eu fiz: comparando listas de compra

# Laura e Ana resolveram fazer compras juntas, mas criaram duas listas diferentes. Elas querem um programa que mostre:

#     Quais itens apareceram nas duas listas
#     Quais foram exclusivos de Laura
#     Quais foram exclusivos da Ana

# Escreva um programa que solicite as listas e mostre os resultados dessas comparações.

# Exemplo de entrada:

# Lista de Laura: leite, pão, café, açúcar
# Lista de Ana: pão, café, biscoito, chocolate

# Saída esperada:

# Itens em ambas as listas: pão, café
# Itens exclusivos de Laura: leite, açúcar
# Itens exclusivos de Ana: biscoito, chocolate
