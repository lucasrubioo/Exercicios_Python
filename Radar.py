velocidade = float(input('Digite a velocidade do veiculo em (km/h): '))
if velocidade > 80:
    multa = (velocidade-80) * 7
    print('Voce foi multado pois ultrapassou o limite de velocidade 80km/h\nO valor da sua multa e de R${:.2f}'.format(multa))
print('Tenha um bom dia, Dirija com segurança !')