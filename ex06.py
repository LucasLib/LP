# Escrever um algoritmo que leia o nome de um aluno e as notas das três provas que ele obteve no semestre.
# No final informar o nome do aluno e a sua média (aritmética).

# INICIO
nome = input('Qual é seu nome? ')
nota1 = float(input('Qual foi sua primeira nota? '))
nota2 = float(input('Qual foi sua segunda nota? '))
nota3 = float(input('Qual foi sua terceira nota? '))

# PROCESSO
media = (nota1 + nota2 + nota3) / 3

# IMPRESSAO
print(f'A média da notas são: {media:.2f}')