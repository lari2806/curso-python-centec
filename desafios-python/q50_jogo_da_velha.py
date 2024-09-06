matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for i in matriz:
    print(i)
    
def jogador1():
    escolha = int(input("Jogador 1 escolha uma casa:\n> "))
    if escolha == 1:
        matriz[0][0] = "X"
    if escolha == 2:
        matriz[0][1] = "X"
    if escolha == 3:
        matriz[0][2] = "X"
    if escolha == 4:
        matriz[1][0] = "X"
    if escolha == 5:
        matriz[1][1] = "X"
    if escolha == 6:
        matriz[1][2] = "X"
    if escolha == 7:
        matriz[2][0] = "X"
    if escolha == 8:
        matriz[2][1] = "X"
    if escolha == 9:
        matriz[2][2] = "X"
    for i in matriz:
         print(i)
    jogador2()
        
def jogador2():
    jogador2 = int(input("Jogador 2 escolha uma casa:\n> "))
    if jogador2 == 1:
        matriz[0][0] = "O"
    if jogador2 == 2:
        matriz[0][1] = "O"
    if jogador2 == 3:
        matriz[0][2] = "O"
    if jogador2 == 4:
        matriz[1][0] = "O"
    if jogador2 == 5:
        matriz[1][1] = "O"
    if jogador2 == 6:
        matriz[1][2] = "O"
    if jogador2 == 7:
        matriz[2][0] = "O"
    if jogador2 == 8:
        matriz[2][1] = "O"
    if jogador2 == 9:
        matriz[2][2] = "O"
      
    for i in matriz:
     print(i)
    jogador1()
print(jogador1())
