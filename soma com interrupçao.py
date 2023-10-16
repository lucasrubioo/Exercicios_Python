s = n = c = 0
while n != 999:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    c = c + 1
    s = s + n
print(f'Foram digitados {c} numeros e a soma deles e de {s}')
