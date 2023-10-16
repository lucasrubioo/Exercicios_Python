#import random #(importa o modulo inteiro)
from time import sleep
from random import randint #(importa apenas uma funçao do modulo)
c = randint(0,5) # randomiza um numero inteiro
print('-=-'* 20)
print('Ola, vamos brincar ?\nTente adivinhar o numero que estou pensando entre 0 - 5 :)')
n = int(input('Em qual numero estou pensando?: ...'))
print('PROCESSANDO ....')
sleep(2)
if c == n:
    print('PARABENS, voce me venceu !!!')
else:
    print('PERDEU, Eu pensei no numero: {}\nTente outra vez x_x'.format(c))
