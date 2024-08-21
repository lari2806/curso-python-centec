numero = input("Digite um número: ")
numero = int(numero)

resultado= 1

for fatorial in range(numero,0,-1):
    print(fatorial, end="")
    if fatorial != 1:
        print(" x ", end="")
    resultado = resultado * fatorial
print(" =", resultado)