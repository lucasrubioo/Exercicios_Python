n = ( int(input('Digite um numero: ')),
      int(input('Digite um outro numero: ')),
      int(input('Digite mais um numero: ')),
      int(input('Digite o ultimo numero: ')) )
print(f'O numero 9 apareceu {n.count(9)} vezes na lista.')
if 3 in n:
    print(f'O numero 3 foi localizado por primeiro na posiçao {n.index(3)+1} da lista.')
else:
    print('Tivemos 0 numeros 3 digitados')
print(f'Os valores pares digitados foram ' , end= '')
for c in n:
    if c % 2 == 0:
        print(c, end= ' ')

