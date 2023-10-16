soma = 0
cont = 0
for c in range (1,7):
    num = int(input('Digite {} numero: '.format(c)))
    if c % 2 == 0:
        soma = soma + num
        cont += 1
print('Ao todo foram {} numeros pares e a soma dos valores foram {}'.format(cont,soma))
