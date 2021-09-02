numero1 = int(input('Digite um número:'))
numero2 = int(input('Digite um número diferente:'))

if numero1 > numero2:
    print('O número: {} é maior.'.format(numero1))
elif numero1 < numero2:
    print('O número: {} é maior.'.format(numero2))
else:
    print('Os números são iguais.')
