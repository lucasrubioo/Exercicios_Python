soma = 0
cont = 0
for c in range(1 , 501, 2):
    if c % 3 == 0:
    #soma = soma+c os dois formatos dao o mesmo resultado
        soma += c
        cont += 1
print('A soma dos {} intervalos tem o total de {}'.format(cont,soma))