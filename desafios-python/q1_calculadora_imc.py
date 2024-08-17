peso = input("Digite seu peso em kilos: ")
peso = float(peso)

altura = input("Digite sua altura: ")
altura = float(altura)

imc = peso / (altura ** 2)

print("====Seu IMC é=====")
print("{:.2f}".format(imc) , "")

if imc <= 18.4:
    print("Classficação: magreza.")
    
if imc > 18.5 and imc < 24.9:
    print("Classificação: Adequado.")
    
if imc > 25 and imc < 29.9:
    print("Classificação: pré-obeso")
    
if imc > 30 and imc < 34.9:
    print("Classificação: Obesidade Grau I")

if imc > 35 and imc < 39.9:
    print("Classificação: Obseidade Grau II")
    
if imc > 40:
    print("Classificação: Obesidade Grau III")