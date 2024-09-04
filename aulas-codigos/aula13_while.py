numero = 5

while numero < 10:
    print(numero,"este numero menor que 10")
    
    numero += 1

print(numero,"este numero maior ou igual a 10")

opcao = 1

while opcao>= 1 and opcao<=3:
    print("MENU DE OPÇOES")
    print("opção 1")
    print("opção 2")
    print("opção 3")
    print("Digite 4 para sair")
    opcao = int(input("Digite a opção que deseja: "))
    
print("Você saiu do menu.")