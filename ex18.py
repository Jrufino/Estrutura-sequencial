fileSize=float(input('Digite o tamanho do arquivo em MB:'))
velLink=float(input('Digite a velocidade do link em Mbps:'))
velDownload=velLink/100

tempoBaixar= fileSize/velDownload
print('Voce vai demorar {0:.2f}s para baixar'.format(tempoBaixar))

