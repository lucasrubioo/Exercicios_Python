from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Opçoes:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Sua Jogada ->'))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POO!')
print('=-='*10)
print('O Computador escolheu {}'.format(itens[computador]))
print('O Jogador escolheu {}'.format(itens[jogador]))
print('=-='*10)
if computador == 0: #pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador VENCEU!')
    elif jogador ==2:
        print('Computador VENCEU!')
    else:
        print('Jogada INVALIDA!')
elif computador == 1: #papel
    if jogador == 0:
        print('Computador VENCEU!')
    if jogador == 1:
        print('EMPATE')
    if jogador ==2:
        print('Jogador VENCEU!')
    else:
        print('Jogada INVALIDA!')
elif computador == 2: #tesoura
    if jogador == 0:
        print('Jogador VENCEU!')
    if jogador == 1:
        print('Computador VENCEU!')
    if jogador == 2:
        print('EMPATE')
    else:
        print('Jogada Invalida!')
