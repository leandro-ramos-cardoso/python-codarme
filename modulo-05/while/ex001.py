n = int(input('Digite um número:\n'))
i = 0
soma = 0

while i <= n:
    soma = i + soma
    i = i + 1
print('A soma de todos os valores até {} é: {}'.format(n, soma))