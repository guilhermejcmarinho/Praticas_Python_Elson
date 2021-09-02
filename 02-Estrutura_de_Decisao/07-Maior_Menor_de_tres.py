numero01 = int(input('Informe o primeiro numero:'))
numero02 = int(input('Informe o segundo numero:'))
numero03 = int(input('Informe o terceiro numero:'))

if numero01>numero02 and numero01>numero03:
    if numero02>numero03:
        print('Primeiro numero {} é o maior, terceiro {} menor.'.format(numero01, numero03))
    else:
        print('Primeiro numero {} é o maior, segundo {} menor.'.format(numero01, numero02))
elif numero01<numero02 and numero02>numero03:
    if numero01>numero03:
        print('Segundo numero {} é o maior, terceiro {} menor.'.format(numero02, numero03))
    else:
        print('Segundo numero {} é o maior, primeiro {} menor.'.format(numero02, numero01))
elif numero01 < numero02 and numero01 < numero03:
        print('Terceiro numero {} é o maior, primeiro {} menor.'.format(numero03, numero01))
else:
    print('Terceiro numero {} é o maior, segundo {} menor.'.format(numero03, numero02))
