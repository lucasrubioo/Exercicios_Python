n = int(input('Digite um numero: '))
tot = 0
for c in range (1, n + 1):
    if n % c == 0:
        print('\033[33m', end= ' ')
        tot += 1 #tot = tot + 1
    else:
        print('\033[31m', end= ' ')
    print('{}'.format(c), end= ' ')
if tot == 2:
    print('\n\33[mO numero foi divisivel por {} vezes, portanto ele e primo'.format(tot))
else:
    print('\n\33[mO numero foi divisivel por {} vezes, portanto ele NAO e primo'. format(tot))
