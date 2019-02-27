import math

areaPintura=float(input('Digite a area a ser pintada em m2: '))
coberturaTinta=6
litrosLata=18
precoLata=80
litrosGalao=3.6
precoGalao=25
quantidadeLitros=areaPintura/coberturaTinta

print('Litros necessarios: {0:.2f}'.format(quantidadeLitros))

qtdLatas= quantidadeLitros/litrosLata
qtdGaloes=quantidadeLitros/litrosGalao
resto=quantidadeLitros%litrosLata
'''print('resto {}'.format(resto))'''

qtdArredondadaLatas= math.ceil(qtdLatas)
qtdArredondadaGaloes= math.ceil(qtdGaloes)

qtdOtimaLatas=qtdArredondadaLatas-1
qtdOtimaGaloes=math.ceil(resto/litrosGalao)
menorPreco=(qtdOtimaLatas*precoLata)+(qtdOtimaGaloes*precoGalao)

if menorPreco>(qtdArredondadaLatas*precoLata):
    menorPreco=(qtdArredondadaLatas*precoLata)
    qtdOtimaLatas=qtdArredondadaLatas
    qtdOtimaGaloes=0
else:
    pass

print('Se for comprar soh latas a quantidade sera {0:.2f}'.format(qtdArredondadaLatas))
print('Nesse caso o valor sera R${0:.2f}'.format(qtdArredondadaLatas*precoLata))
print('Se for comprar soh galoes a quantidade sera {0:.2f}'.format(qtdArredondadaGaloes))
print('Nesse caso o valor sera R${0:.2f}'.format(qtdArredondadaGaloes*precoGalao))

print('Compra mista otimizada:')
print('Latas: {}'.format(qtdOtimaLatas))
print('Galoes: {}'.format(qtdOtimaGaloes))
print('Menor preco: R${0:.2f}'.format(menorPreco))