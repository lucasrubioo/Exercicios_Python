soma = maiscaro = cont = menor = barato = 0
while True:
    nome = str(input('Qual o nome do produto? : ')).strip()
    valor = float(input('Qual o valor do produto? R$ '))
    soma += valor
    cont += 1
    if valor > 1000:
        maiscaro += 1
    if cont == 1:
        menor = valor
        barato = nome
    else:
        if valor < menor:
            menor = valor
            barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar ? [S/N] -> ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O valor da compra foi de R${soma}')
print(f'Tivemos {maiscaro} produto(s) com o valor superior a R$1000,00')
print(f'O menor preço foi do item {barato.upper()} custando o valor de R${menor:.2f}')
print('Acabou')