#Faça um algoritmo que receba dois números e ao final mostre a soma, subtração, multiplicação e a divisão dos números lidos.

# INICIO

Number1 = int(input('Digite um numero inteiro: '))
Number2= int(input('Digite outro numero inteiro: '))

# PROCESSO

soma = Number1 + Number2
subtração = Number1 - Number2
multiplicação = Number1 * Number2
divisão = Number1 / Number2

# IMPRESSÃO

print(f'A sua soma é {soma}, sua subtração é {subtração}, sua multiplicação é {multiplicação}, sua divisão é {divisão}.')