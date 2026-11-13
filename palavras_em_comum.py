texto1 = set(input("Texto 1: ").lower().split())
texto2 = set(input("Texto 2: ").lower().split())

comuns = texto1.intersection(texto2)

print(f"\nPalavras em comum: {comuns}")


# texto1 = input("Texto 1: ").split()
# texto2 = input("Texto 2: ").split()
# palavras_em_comum = set()

# for palavra in texto1:
#     if palavra in texto2:
#         palavras_em_comum.add(palavra)

# print("\nPalavras em comum: ", palavras_em_comum)

# Faça como eu fiz: descobrindo palavras comuns entre dois textos

# Clara é editora de uma revista e deseja comparar dois artigos para identificar quais palavras aparecem em ambos. Sua tarefa é criar um programa que receba dois textos e exiba o conjunto de palavras comuns entre eles.

# Exemplo de entrada:

# Texto 1: O sol brilha forte no céu azul

# Texto 2: O céu azul anuncia um dia de sol intenso

# Saída esperada:

# Palavras em comum: {'o', 'azul', 'sol', 'céu'}
