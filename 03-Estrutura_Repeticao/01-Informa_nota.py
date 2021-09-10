nota = int(input('Informe uma nota de 0 a 10:'))
while nota < 0 or nota > 10:
    nota = int(input('Informe uma nota de 0 a 10:'))
else:
    print('Nota informada: {}'.format(nota))
    