# Alice é responsável por escrever um programa que verifica se um cupom de desconto pode ser utilizado. O programa recebe 3 valores e retorna True caso o cupom possa ser utilizado, ou False , caso contrário.

# Os três valores que o programa recebe são:
# 1. Valor de compra (float)
# 2. Valor do frete (float)
# 3. Cliente é cadastrado no programa de fidelidade (string “s” (sim) ou “n” (não))

# O cupom tem a seguinte regra:

# Caso o valor da compra somado ao frete seja superior a R$ 100, ou o cliente seja cadastrado no programa de fidelidade, o cupom de desconto pode ser utilizado. Caso contrário, o cupom não pode ser utilizado. Seu objetivo é implementar o programa que atenda a especificação acima.

valor_compra = float(input('Digite o valor de compra: '))
valor_frete = float(input('Digite o valor do frete: '))
cli_fidel = input('O cliente é cadastrado no programa de fidelidade? (S/N)? ')

if (valor_compra + valor_frete) > 100 or cli_fidel == 's':
    print('Cupom de desconto pode ser usado.')
else:
    print('O cliente não atende aos requisitos para utlizar o cupom de desconto.')