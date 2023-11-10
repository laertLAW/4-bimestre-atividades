salario_atual = float(input("Digite o seu salário atual: "))
if salario_atual <= 280:
    aumento = 20
elif salario_atual <= 750:
    aumento = 15
elif salario_atual <= 1500:
    aumento = 10
else:
    aumento = 5

diferença = salario_atual * (aumento/100)
nov = 