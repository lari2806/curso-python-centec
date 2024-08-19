
print("1 - Celsius para fahrenheit")
print("2 - fahrenheit para celsius")
temperatura = input("Digite qual temperatura você quer converter: \n")
temperatura = float(temperatura)

if temperatura == 1:
  celsius = input("Digite a temperatura em celsius:\n")
  celsius = float(celsius)
  fahrenheit = celsius * 1.8 + 32
  print("A temperatura em fahrenheit é ", fahrenheit)
elif temperatura == 2:
    fahrenheit =  input("Digite a temperatura em fahrenheit : \n")
    fahrenheit = float(fahrenheit)
    celsius = (fahrenheit - 32) / 1.8
    print("A temperatura convertida para celsius é ", celsius)
else:
    print("Opção inválida.")
