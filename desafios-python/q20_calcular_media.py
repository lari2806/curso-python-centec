quantidade_numeros = int(input('Digite a quant. de números: '))


somatorio = 0


for x in range(quantidade_numeros):
    valor = float(input(f'Digite o {x + 1}º valor: '))


    somatorio += valor

print('Média:', somatorio / quantidade_numeros)
