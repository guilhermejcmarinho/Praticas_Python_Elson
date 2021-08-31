salHora = float(input('Informe o sálario por hora: '))
horaTraba = float(input('Informe a quantidade de horas trabalhadas: '))

salBruto = salHora * horaTraba
rfSal = salBruto * 0.11
inssSal = salBruto * 0.08
sindiSal = salBruto * 0.05
salLiquido = salBruto - sindiSal - rfSal - inssSal

print('+ Salário Bruto: R$', salBruto)
print('- IR (11%): R$', rfSal)
print('- INSS (8%): R$', inssSal)
print('- Sindicato (5%): R$', sindiSal)
print('- Salário Líquido: R$', round(salLiquido, 2))
