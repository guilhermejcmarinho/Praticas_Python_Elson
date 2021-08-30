kgPeixe = float(input('Entre com o peso do peixe: '))
if kgPeixe <= 50:
    print('Peso permitido.')
else:
    pesoAcima = round(kgPeixe - 50)
    multaTotal = float(pesoAcima * 4)
    print('Peso excedido: ', pesoAcima, 'quilos.')
    print('Multa a ser paga no valor de: R$', multaTotal)
