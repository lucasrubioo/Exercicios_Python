from random import randint
v = soma = 0
print('=== JOGO PAR OU IMPAR ===')
while True:
    numjogador = int(input('Escolha o numero que deseja jogar -> '))
    computador = randint(0, 10)
    soma = computador + numjogador
    jogador = ' '
    while jogador not in 'PARIMPAR':
        jogador = str(input('Voce deseja ser PAR ou IMPAR ? ')).upper().strip()
        print(f'Voce jogou {numjogador} eo computador jogou {computador}, sendo o total de {soma}')
        if jogador == 'PAR':
            if soma % 2 == 0:
                print('PAR Voce Venceu !')
                v = v +1
            else:
                print('Voce Perdeu')
                break
        elif jogador == 'IMPAR':
             if soma % 2 == 1:
                 print('IMPAR Voce Venceu !')
                 v = v + 1
             else:
                 print('Voce Perdeu')
                 break
        print(f'Voce teve {v} vitorias antes de perder')


