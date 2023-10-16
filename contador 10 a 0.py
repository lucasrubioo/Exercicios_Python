from emoji import emojize
from time import sleep
for c in range (10,-1, -1):
    sleep(1)
    print(c)
print(emojize(':sparkler: Feliz Ano Novo :fireworks: ' * 5 ,  language='alias'))
