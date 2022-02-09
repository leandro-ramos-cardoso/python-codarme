# Escreva um programa com as seguintes especificações:

# Uma variável “valor_compras” que receba um valor do tipo float, representando o valor total das compras.
# Uma variável “desconto” que receba um valor do tipo float, representando o desconto a ser aplicado sobre o valor total das compras.
# Uma variável “quantidade_itens”, que represente a quantidade de itens que foram comprados.

# Seu programa deve imprimir dois resultados:
# 1 - O valor final das compras, considerando o desconto aplicado.
# 2 - O custo médio de cada item (considerando o valor final das compras).

# OBS: Lembre que podemos utilizar símbolos como (+, -, *, /) para fazer cálculos em Python.

valor_compras = float(input('Informe o valor da compra: '))
desconto = float(input('Informe o valor do desconto: '))
quantidade_itens = int(input('Informe a quantidade de itens: '))
valor_final = (valor_compras * quantidade_itens) - desconto
liquido = valor_final / quantidade_itens

print()
print('============={:^15}============='.format('EXERCICIO 02'))
print()
print('Valor final das compras -> R$ {:.2f}'.format(valor_final))
print('Custo médido -> R$ {:.2f}'.format(liquido))
