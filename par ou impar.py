numero = int(input('Digite um numero qualquer e lhe direi se ele e PAR ou IMPAR\n-->'))
resultado = numero % 2
if resultado == 0:
    print('O numero {} e PAR !!'.format(numero))
else:
    print('O numero {} e IMPAR !!'.format(numero))
