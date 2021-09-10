nomeusr = input('Nome de usuario:')
senha = input('Password:')

while senha == nomeusr:
    print('\nPassword não deve ser igual ao usuario, repita.\n')
    nomeusr = input('Nome de usuario:')
    senha = input('Password:')

print('Dados validos!')
