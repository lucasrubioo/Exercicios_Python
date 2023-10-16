import datetime
ano = datetime.date.today().year
maior = 0
menor = 0
for c in range (1,8):
    nasc = int(input('Digite a {}° data de nascimento:'.format(c)))
    idade = ano - nasc
    if idade >= 21:
        print('Essa pessoa e maior!')
        maior = maior + 1
    else:
        print('Essa pessoa e menor!')
        menor = menor + 1
print('Das pessoas analisadas {} sao maiores e {} sao menores !'.format(maior,menor))





