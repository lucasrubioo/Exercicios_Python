km = float(input('Digite quantos Km tera sua viagem:'))
print('Voce esta prestes a iniciar sua viagem !! :)')
if km > 200:
    valor = km * 0.45
else:
    valor = km * 0.50
print('O valor da sua viagem e de R${:.2f} com {:.0f}km'.format(valor,km))