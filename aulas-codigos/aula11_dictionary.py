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