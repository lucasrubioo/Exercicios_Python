print('\033[7;30;45m-=-=' * 15)
print('Analisador de triangulos !!')
print('-=-=' * 15)
r1 = float(input('Digite o valor do primeiro segmento: '))
r2 = float(input('Digite o valor do segundo segmento: '))
r3 = float(input('Digite o valor do terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Esses segmentos podem formar um triangulo !! :)')
else:
    print('Esses segmentos NAO podem formar um triangulo')
