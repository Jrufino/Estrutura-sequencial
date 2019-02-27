salHora=float(input('Digite seu salario por hora: '))
horasTrabalhadas= int(input('Digite a quantidade de horas trabalhadas: '))

salMensalBruto=salHora*horasTrabalhadas
impostoRenda=salMensalBruto*0.11
inss=salMensalBruto*0.08
sindicato=salMensalBruto*0.05
salLiquido=salMensalBruto-impostoRenda-inss-sindicato

print('Salario mensal bruto: R${}'.format(salMensalBruto))
print('INSS: R${}'.format(inss))
print('Contribuicao Sindical: RS{}'.format(sindicato))
print('Salario liquido: R${}'.format(salLiquido))


