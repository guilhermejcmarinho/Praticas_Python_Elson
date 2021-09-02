numero1 = int(input('Digite um número:'))

if numero1 > 0:
    print('O número: {} é positivo.'.format(numero1))
elif numero1 < 0:
    print('O número: {} é negativo.'.format(numero1))
else:
    print('Você digitou zero.')
