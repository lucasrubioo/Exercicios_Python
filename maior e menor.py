a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))
menor = a
# Testando qual o menor numero
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Testando qual o maior numero
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor numero e {}'. format(menor))
print('O maior numero e {}'.format(maior))
