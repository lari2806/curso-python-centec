print("Menu calculadora, escolha uma opção")
print("A - Somar")
print("B - Subtrair")
print("C - Multiplicar")
print("D - Dividir")
opcao = input("Digite a opção que deseja: ")



if opcao == "a" or opcao == "A":
    opcao = "Somar"
elif opcao == "b" or opcao == "B":
    print("Subtrair")
elif opcao == "c" or opcao == "C":
    print("Multiplicar")
elif opcao == "d" or opcao == "D":
    print("Dividir")
else:
    print("Opção inválida.")
print("Sua opcao foi ", opcao)