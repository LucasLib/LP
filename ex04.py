# Escrever um algoritmo para determinar o consumo médio de um automóvel sendo fornecida a distância
# total percorrida pelo automóvel e o total de combustível gasto

# INICIO

CombustívelM = float(input('Qual a consumo da combustível utilizado em KM: '))
Distancia = float(input('Digite a distancia percorrida em Litro: '))

# PROCESSO 

CombustívelT = CombustívelM / Distancia 

# IMPRESSAO

print(f'O consumo médio foi de {CombustívelT:.3f}')