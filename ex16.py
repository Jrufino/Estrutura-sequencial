areaPintura=float(input('Digite a area a ser pintada em m2:'))
coberturaTinta= 3
lataTinta=18
precoLata=80
qtdLatas= ((areaPintura/coberturaTinta)/lataTinta)
valorFinal=(qtdLatas*precoLata)

print('Voce precisara comprar {0:.2f} latas'.format(qtdLatas))
print('O valor sera R${0:.2f}'.format(valorFinal))