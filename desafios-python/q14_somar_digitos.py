numero = input('Digite um valor inteiro: ')
numero = numero.replace('-', '')


somatorio = 0


for digito in numero:
    valor = int(digito)
    somatorio += valor


print('A soma é:', somatorio)
