primeiraNota = float(input('Informe a primeira nota:'))
segundaNota = float(input('Informe a segunda nota:'))

notaParcial = (primeiraNota+segundaNota)/2
if notaParcial == 10:
    print('Aprovado com Distinção.')
elif notaParcial >= 7:
    print('Aprovado.')
else:
    print('Reprovado.')
