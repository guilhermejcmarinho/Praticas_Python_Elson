arquivo = int(input('Tamanho do arquivo para download em MB:'))
velocidade = int(input('Velocidade de download em MBps:'))

print('Tempo estimado de download: {}s'.format(int(arquivo / velocidade)))
