# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

senha = input('Senha: ')

if not senha:
    print('Você nao digitou nada.')
elif senha == '123456':
    print('Entrou.')
else:
    print('Senha incorreta.') 
