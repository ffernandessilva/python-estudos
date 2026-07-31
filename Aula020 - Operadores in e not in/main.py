# Operador in e not in
# Strings são iteráveis
# 0 1 2 3 4 5 
# F e l i p e
# 6-5-4-3-2-1
nome_teste = 'Felipe'
print('l' in nome_teste)
print('z' in nome_teste)
print('lipe' in nome_teste)
print ('-' * 10)
print('l' not in nome_teste)
print('z' not in nome_teste)
print('lipe' not in nome_teste)
print ('-' * 10)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else: 
    print(f'{encontrar} não está em {nome}')
