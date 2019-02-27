pesoPeixe= float(input('Digite o peso do peixe: '))
if pesoPeixe>50:
    excedente= pesoPeixe-50
else:
    excedente= 0

multa= excedente*4

if excedente == 0:
    print('O peixe esta abaixo do limite de 50 quilos')
else:
    print('O peixe esta {} quilos acima. O valor da multa eh R${}'.format(excedente,multa))