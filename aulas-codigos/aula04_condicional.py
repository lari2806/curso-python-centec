entrada = input("Digite sua idade: ")

idade = int(entrada)

print("Sua idade é ", idade)

# SE a idade for maior ou igual que 18 anos então: 
# é maior de idade
if idade >= 18 and idade<65:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
if idade >=65:
    print("Você é aposentado.")  
else:
    print("Você não é aposentado.") 

#TOME CUIDADO COM A IDENTAÇÃO ou TABULAÇÃO.
