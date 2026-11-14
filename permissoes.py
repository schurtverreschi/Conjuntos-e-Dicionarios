principal = set(input("Permissões principais: ").split(", "))
solicitado = set(input("Permissões solicitadas: ").split(", "))

if solicitado.issubset(principal):
    print("As permissões solicitadas fazem parte das permissões principais.")
else:
    print("As permissões solicitadas não fazem parte das permissões principais.")

# Faça como eu fiz: verificando permissões

# Marina trabalha no setor de segurança de uma empresa e precisa verificar se um determinado conjunto de permissões faz parte das permissões principais de um sistema. Sua tarefa é desenvolver um programa que receba duas listas de permissões e verifique se a segunda lista está contida na primeira.

# Exemplo de entrada:

# > CASO 01:

# Permissões principais: leitura, escrita, execução, compartilhamento
# Permissões solicitadas: leitura, escrita

# > CASO 02:

# Permissões principais: leitura, escrita, execução, compartilhamento
# Permissões solicitadas: leitura, exclusão

# Saída esperada:

# > CASO 01:

# As permissões solicitadas fazem parte das permissões principais.

# > CASO 02:

# As permissões solicitadas não fazem parte das permissões principais.
