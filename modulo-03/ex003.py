# Considere o programa abaixo

# resultado = 2 + 3 * 2 ** 2
# print(resultado)

# É possível conseguir resultados diferentes, sem alterar os números e operadores, apenas com a utilização de parênteses. Por exemplo:

# resultado = (2 + 3) * 2 ** 2
# print(resultado)
# 20

# Utilize parênteses de modo que o programa imprima os seguintes resultados: 14, 38 e 100


resultado = 2 + (3 * 2) ** 2 # 38
resultado2 = 2 + (3 * (2 ** 2)) # 14
resultado3 = ((2 + 3) * 2) ** 2 # 100

print(resultado)
print(resultado2)
print(resultado3)