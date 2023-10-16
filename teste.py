def soma (*parcelas):
    aux = 0
    for valor in parcelas:
        aux += valor
    return aux
print(soma(4,8,9))
