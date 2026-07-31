# Operadores Lógicos
# and (e),  or (ou),  not (não)
# or - Qualquer condição verdadeiras avalia
# toda a expressão como verdadeira
# Se qualquer valor for considerado verdadeiro, 
# a expressão inteira será avaliada naquele valor
# São considerados falsy 
# 0 0 0 '' False
# Também existe o tipo None, 
# usado para representar um não valor 

entrada = input('[E]ntrar [S]air: ')
senha_permitida = '123456'

if entrada == 'E' or entrada == 'e':
    senha_digitada = input('Digite a senha: ')

    if senha_digitada == senha_permitida:
        print('Entrar')
    else:
        print('Senha incorreta')
else:
    print('Sair')
