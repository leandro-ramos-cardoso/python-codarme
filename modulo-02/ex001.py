# Escreva um programa que contenha 4 variáveis e que imprima na tela o tipo de cada uma delas. A saída do seu programa deve ser na seguinte ordem:

# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'bool'>

print('============{:^20}============'.format('EXERCICIO 01'))

nome = 'Manuela'
x = 28
z = 10.5
a = 2 == 2

print('Tipo da váriavel {} -> {}'.format(nome, type(nome)))
print('Tipo da váriavel {} -> {}'.format(x, type(x)))
print('Tipo da váriavel {} -> {}'.format(z, type(z)))
print('Tipo da váriavel {} -> {}'.format(a, type(a)))
