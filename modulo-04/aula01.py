# Código em python criado baseado na aula 01 do módulo 03 para estudo de operadores aritméticos.

a = int(input(('Digite um número: ')))
b = int(input(('Digite outro número: ')))

print('=============={:^20}=============='.format('OPERADORES ARITMÉTICOS'))

print('A soma entre {} e {} vale {}.'.format(a, b, a + b))
print('A subtração entre {} e {} vale {}.'.format(a, b, a - b))
print('A multiplicação entre {} e {} vale {}.'.format(a, b, a * b))
print('A divisão entre {} e {} vale {}.'.format(a, b, a / b))
print('A divisão inteira entre {} e {} vale {}.'.format(a, b, a // b))
print('O resto entre {} e {} vale {}.'.format(a, b, a % b))
print('{} elevado à {} vale {}.'.format(a, b, a ** b))

print()

# ORDEM DE PRECEDÊNCIA
# () 
# **
# * / // %
# + -

print(3 + 4 * 5)
print((3 + 4) * 5)