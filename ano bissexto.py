import datetime
ano = int(input('Que ano quer analisar ? Para analisar o ano atual digite 0: '))
if ano == 0:
    ano = datetime.date.today().year # Atribui o ano atual da maquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
# Se o resto da divisao por 4 do ano for igual a 0 e o resto da divisao por 100 for diferente de 0 ou o resto da divisao por 400 for igual a 0 o ano e bissexto
    print('O Ano de {} e Bissexto !'.format(ano))
else:
    print('O Ano de {} nao e Bissexto'.format(ano))