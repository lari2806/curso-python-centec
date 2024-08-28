quantidade_numeros = int(input('Digite a quant. de números: '))


soma = 0


for x in range(quantidade_numeros):
    valor = float(input(f'Digite o {x + 1}º valor: '))


    soma += valor

print('Média:', soma / quantidade_numeros)
