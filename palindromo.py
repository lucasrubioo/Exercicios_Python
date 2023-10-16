frase = str(input('Digite a frase: ')).strip().upper() #strip remove os espaços do começo e fim da frase, upper deixa a frase toda em maiusculo
palavras = frase.split() #split separa a string pelos espaços
junto =''.join(palavras) #join subistitui os espaços da srting por o que tiver entre '' nesse caso por nada removendo os espaços entre as frases
inverso = ''
for letra in range (len(junto)-1, -1, -1): # len pega a ultima letra da str junto -1 porque a str sempre fica com uma variavel a menos, o ultimo -1 e para ir voltando uma letra por vez para inverter a frase
    inverso = inverso + junto[letra] # inverso =+ junto[letra] o + substitui a redundancia da variavel 'inverso'
print(junto, inverso)
if inverso == junto:
    print('E UM PALINDROMO')
else:
    print('NAO E UM PALINDROMO')
