while True:
    n = int(input('Digite o numero que deseja ver a tabuada: '))
    if n < 0:
        break
    for c in range (1,11):
        print(f'{n} X {c} = {n*c}')
print('Programa finalizado !')