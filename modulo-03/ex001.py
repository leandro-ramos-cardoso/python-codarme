# Escreva um programa que receba um número inteiro do usuário e imprima True caso o número seja par e False, caso o número seja ímpar.

num = int(input(('Digite um número: ')))

if num % 2 == 0:
    print('{} é par.'.format(num))
else:
    print('{} é impar.'.format(num))