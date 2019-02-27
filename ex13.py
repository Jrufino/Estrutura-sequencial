altura=float(input('Digite a altura da pessoa: '))
sexo=input("Sexo: ")
sexo= sexo.upper()
if sexo == 'M':
    pesoIdeal=(72.7*altura)-58
elif sexo == 'F':
    pesoIdeal=(62.1*altura)-44.7
else:
    print('O sexo inserido nao foi valido')

print('O peso ideal dessa pessoa eh {}'.format(pesoIdeal))