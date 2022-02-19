# Implemente uma calculadora que recebe 3 valores do usuário:

# a. Operando a (pode ser um inteiro ou float).
# b. Operando b (pode ser um inteiro ou float).
# c. Operador op 

# i. op pode ser uma string representando o operador, por exemplo, "+" ou "-
#". Outra opção é utilizar números, por exemplo, 1 para soma , 2 para subtração , etc.

# O seu programa deve receber esses 3 valores e imprimir o resultado da operação.
# Caso o operador seja de divisão e o segundo operando seja o valor zero, o
# programa deve imprimir uma mensagem: “Não é possível realizar divisão por zero!”.

print('=========={:^10}=========='.format('CALCULADORA'))
print()

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
print()

print('=========={:^10}=========='.format('OPERAÇÕES'))
print('1 - SOMA')
print('2 - SUBTRAÇÃO')
print('3 - MULTIPLICAÇÃO')
print('4 - DIVISÃO')
print()

op = int(input('Escolha a opção desejada: '))

if op == 1:
    print('A soma entre {} e {} vale {}.'.format(a, b, a + b))
elif op == 2:
    print('A subtração entre {} e {} vale {}.'.format(a, b, a - b))
elif op == 3:
    print('A multiplicação entre {} e {} vale {}.'.format(a, b, a * b))
elif op == 4:
    if b != 0:
        print('A divisão entre {} e {} vale {}.'.format(a, b, int(a / b)))
    else: 
        print('Não é possível realizar divisão por zero!')
