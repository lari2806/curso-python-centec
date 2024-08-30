pessoa = {
    #Adicionando valores de dados em pares chave:valor.
    
    # no lado direito é o valor das chaves.
    "nome" : "Larissa",
    "idade" : 17,
    "altura" : 1.52,
    "veiculo": {
        # O valor da chave.
        "Carro" : "Honda",
        "ano" : 2005
    }
    
}
print(pessoa)
print(pessoa["nome"])
print(pessoa["veiculo"]["Carro"])
print(len(pessoa))

print("Utilizando dicionary em listas")

lista_pessoas = [
    #Definindo um elemento do array
    {
        "nome": "Larissa",
        "idade" : 17
    },
    #mais um elemento
    {
        "nome": "Savio",
        "idade": 16
    }
    
]

print("................. ELEMENTOS CONTIDOS NA LISTA .................... ")
print(lista_pessoas, "\n")


print("..............PRIMEIRO ELEMENTO DA LISTA.........................")
print(lista_pessoas[0]["nome"])