salario = float(input('Digite o salario atual do colaborador R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('O salario anterior era de R${:.2f} e com o reajuste passa para R${:.2f}'.format(salario,novo))
