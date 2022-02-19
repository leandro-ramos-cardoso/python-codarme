# Escreva um programa de autenticação que receba um nome de usuário e senha ( input ) informe se:

# Autenticação foi bem-sucedida.
# Se o nome de usuário não existe.
# Se a senha está incorreta.

# Os valores corretos de nome de usuário e senha devem estar armazenados em
# constantes, como no exemplo abaixo:

user = 'admin'
password = '123123'

login = input('Digite o nome do usuário: ')
senha = input('Digite a senha: ')

if (user == login) and (password == senha):
    print('Autenticação foi bem-sucedida')
elif user != login:
    print('Nome de usuário não existe.')
elif password != senha:
    print('Senha incorreta')
