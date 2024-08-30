texto = input("Digite o texto que deseja: ")

alfabeto = {
    'a':'A', 'b':'B', 'c':'C', 'd': 'D','e':'E', 'f':'F', 'g': 'G',
    'h':'H', 'i':'I', 'j':'J','k':'K','l': 'L', 'm':'M', 'n':'N', 'o': 'O', 'p':'P',
    'q':'Q', 'r':'R', 's':'S', 't':'T', 'u':'U', 'v':'V',
    'w':'W', 'x':'X', 'y':'Y', 'z':'Z'
}
odernando_palavras = texto.split()

for palavras in odernando_palavras:
    primeira_letra = palavras[0]
    
    letra_maiuscula = alfabeto[primeira_letra]
    
    nova_palavra = letra_maiuscula + palavras[1:]
    
    print(nova_palavra)