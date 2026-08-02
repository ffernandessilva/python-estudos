"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario = input("Digite o horário atual: ")

if horario.isdigit():
    horario = int(horario)
    if horario < 0 or horario > 23:
        print("Horário inválido.")
    elif horario >= 18 and horario <= 23:
        print("Boa noite!")
    elif horario >= 12  and horario <= 17:
        print("Boa tarde!")
    else:
        print("Bom dia!")
else:
     print("Você não digitou um número inteiro ou um número")

            