numero01 = int(input('Informe o primeiro numero:'))
numero02 = int(input('Informe o segundo numero:'))
numero03 = int(input('Informe o terceiro numero:'))

if numero01>numero02 and numero01>numero03:
    print('Primeiro numero: {} é o maior.'.format(numero01))
elif numero01<numero02 and numero02>numero03:
    print('Primeiro numero: {} é o maior.'.format(numero02))
else:
    print('Primeiro numero: {} é o maior.'.format(numero03))
