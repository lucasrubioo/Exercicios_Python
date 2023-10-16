valor = float(input('Digite o valor para aplicar o desconto \nR$:'))
desconto=(valor * 0.05)
final = valor - desconto
print('O valor de R${} com o desconto de R${} referente a 5% do valor fica em R${} '.format(valor,desconto,final))