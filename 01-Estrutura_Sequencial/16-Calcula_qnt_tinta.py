import math

qntMetros = float(input('Informe a quantidade de m² a serem pintados:'))

tintaTotal = math.ceil(qntMetros/3)
qntLatas = math.ceil(tintaTotal/18)
precoTotal = qntLatas*80

print('Quantidade de tinta: {} Litro(s).'.format(tintaTotal))
print('Quantidade de Latas: {} Lata(s).'.format(qntLatas))
print('Custo pela(s) {} lata(s) é de R$ {},00'.format(qntLatas, precoTotal))
