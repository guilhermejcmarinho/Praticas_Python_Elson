pais_a = 80000
pais_b = 200000

anos = 0

print('Populacao pais A: {} habitantes.'.format(round(pais_a)))
print('Populacao pais B: {} habitantes'.format(round(pais_b)))

while pais_a <= pais_b:
    pais_a = pais_a * 1.03
    pais_b = pais_b * 1.015
    anos = anos + 1

print('\nNumeros de anos para igualar ou ultrapassar a populacao: {} anos.'.format(anos))
print('\nPopulacao pais A: {} habitantes.'.format(round(pais_a)))
print('Populacao pais B: {} habitantes'.format(round(pais_b)))
