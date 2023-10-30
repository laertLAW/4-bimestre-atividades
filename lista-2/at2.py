km = float(input('digite a distancia em km: '))
if km <= 200:
    valor1 = km*0.50
    print(" você vai pagar R${}".format(valor1))
else:
    valor2 = km*0.45
    print('voce vai pagar R${}'.format(valor2))
