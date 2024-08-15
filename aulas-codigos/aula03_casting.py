#casting é a conversãod de tipos de dados, manipula as informções mudando o tipo da variável.

#Exemplos de Casting.

texto = "3.30"
texto2 = "7.75"

#transformando as Strings em floats.
tranformacao_numero1 = float(texto)

print(5 + tranformacao_numero1)

tranformacao_numero2 = float(texto2)

print(5 + tranformacao_numero2)

print(tranformacao_numero1 + tranformacao_numero2)

#Transformar em inteiro

texto3 = "3"
texto4 = "7"

#transformando as Strings em inteiros.
tranformacao_inteiro1 = int(texto3)
transformacao_inteiro2 = int(texto4)

print(tranformacao_inteiro1 + transformacao_inteiro2)

#transformando tipo float para inteiro
valor = int(8.3)
#Ao transformar um float em inteiro NÃO arredonda o número, somente pega a parte inteira do valor.
print(valor)

#Transformando tipo float para String 
valor2 = str(2.5)
print(valor2)

print(f"Minha idade é {str(17)}")
#O str(17) indica que o 17 é uma String 