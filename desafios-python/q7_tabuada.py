numero = input("Digite um valor que você quer utilizar: ")
numero = int(numero)

print("::: Tabuada do número ", numero,":::")

for valor in range(1,11,1):
    print(numero, "x", valor, "=", (numero * valor))

