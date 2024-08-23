lista =[3,6,7,12,50,-15,-20]
numero = 0
numero_menor = float('inf')

for verificacao in lista:
    if numero < verificacao or numero == 0 and numero > verificacao:
        numero = verificacao
    if numero_menor > verificacao:
        numero_menor = verificacao
print("O maior número da lista é ",numero)
print("o menor número da lista é ", numero_menor)