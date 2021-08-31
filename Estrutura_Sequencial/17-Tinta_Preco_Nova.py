area = float(input("Informe a area a ser pintada em m²:"))
litros = area/6
quantGalao = litros/3.6
quantLata = litros/18

if (quantGalao != int(quantGalao)):
    quantGalao = int(quantGalao) + 1
    valorGalao = quantGalao * 25
else:
    valorGalao = quantGalao * 25

if (quantLata != int(quantLata)):
    quantLata = int(quantLata) + 1
    valorLata = quantLata * 80
else:
    valorLata = quantLata *80

if area > 107:
    litrosFolga = litros * 1.1
    diferLitros = litrosFolga % 18
    quantDiferGalao = diferLitros / 3.6

    if (quantDiferGalao != int(quantDiferGalao)):
        quantDiferGalao = int(quantDiferGalao) + 1
        valDiferGalao = quantDiferGalao * 25
        quantDiferLata = litros // 18
        valDiferLata = quantDiferLata * 80
        valorTotal = valDiferLata + valDiferLata
    else:
        valDiferGalao = quantDiferGalao * 25
        quantDiferLata = litros // 18
        valDiferLata = quantDiferLata * 80
        valorTotal = valDiferLata + valDiferLata

    print("Comprando galoes ira precisar de {}, custando R$ {}".format(quantGalao, float(valorGalao)))
    print("Comprando latas ira precisar de {}, custando R$ {}".format(quantLata, float(valorLata)))
    print("Comprando latas e galoes ira precisar de {} lata(s) e {} galao(oes) custando R$ {}".format(int(quantDiferLata), quantDiferGalao, valorTotal))
else:
    print("Comprando galoes ira precisar de {}, custando R$ {}".format(quantGalao, float(valorGalao)))
    print("Comprando latas ira precisar de {}, custando R$ {}".format(quantLata, float(valorLata)))
    print('Não a necessidade de comprar galoes e latas juntos!')
