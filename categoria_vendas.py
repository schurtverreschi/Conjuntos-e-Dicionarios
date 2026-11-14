vendas = {
    "Eletrônicos": [
        {"produto": "Smartphone", "quantidade": 5, "valor_unitário": 2000},
        {"produto": "Tablet", "quantidade": 3, "valor_unitário": 1500},
    ],
    "Eletrodomésticos": [
        {"produto": "Geladeira", "quantidade": 2, "valor_unitário": 3000},
        {"produto": "Micro-ondas", "quantidade": 4, "valor_unitário": 800},
    ],
    "Livros": [
        {"produto": "Livro A", "quantidade": 10, "valor_unitário": 50},
        {"produto": "Livro B", "quantidade": 5, "valor_unitário": 100},
    ],
}

print("\nTotal de vendas por categoria:\n")

for categoria, itens in vendas.items():
    total = sum(item["quantidade"] * item["valor_unitário"] for item in itens)
    print(f"{categoria}: R$ {total:.2f}")


# Faça como eu fiz: analisando vendas por categoria

# Natalia é gerente de uma loja virtual e precisa de um sistema que receba os registros de vendas organizados por categoria de produto. Cada categoria contém uma lista de dicionários representando as vendas individuais, com informações sobre o produto, a quantidade vendida e o valor unitário. Sua tarefa é criar um programa que exiba o total de vendas por categoria.

# Exemplo de entrada:

# vendas = {
#     "Eletrônicos": [
#         {"produto": "Smartphone", "quantidade": 5, "valor_unitário": 2000},
#         {"produto": "Tablet", "quantidade": 3, "valor_unitário": 1500}
#     ],
#     "Eletrodomésticos": [
#         {"produto": "Geladeira", "quantidade": 2, "valor_unitário": 3000},
#         {"produto": "Micro-ondas", "quantidade": 4, "valor_unitário": 800}
#     ],
#     "Livros": [
#         {"produto": "Livro A", "quantidade": 10, "valor_unitário": 50},
#         {"produto": "Livro B", "quantidade": 5, "valor_unitário": 100}
#     ]
# }

# Saída esperada:

# Total de vendas por categoria:

# - Eletrônicos: R$ 14500.00
# - Eletrodomésticos: R$ 9200.00
# - Livros: R$ 1000.00
