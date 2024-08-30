texto = input("Digite o texto que deseja para iniciar a contagem: ")
contagem_caracteres = {}

for c in texto:
    if c in contagem_caracteres:
        contagem_caracteres[c] +=1
    else:
        contagem_caracteres[c] = 1
        
print(contagem_caracteres)
