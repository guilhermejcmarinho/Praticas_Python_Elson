import math

qntMetros = float(input('Informe a quantidade de m² a serem pintados:'))

tintaTotal = round(qntMetros/6, 2)
qntGalao = math.ceil(tintaTotal/3.6)
qntLatas = math.ceil(tintaTotal/18)
precoGalao = qntGalao*25
precoLata = qntLatas*80

if precoGalao > precoLata:
    maisBarato = precoLata
else:
    maisBarato = precoGalao

print('Quantidade de tinta: {} Litro(s).'.format(tintaTotal))
print('\nQuantidade de {} galao(oes) de 3,6 Litros.'.format(qntGalao))
print('Custo por {} galao(oes) é de R$ {},00'.format(qntGalao, precoGalao))
print('\nQuantidade de {} lata(s) de 18 Litros.'.format(qntLatas))
print('Custo por {} lata(s) é de R$ {},00'.format(qntLatas, precoLata))
print('\nO mais barato é R$ {},00'.format(maisBarato))

