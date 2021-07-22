# 11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram 
# para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado 
# no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.
# Desenvolvido por Jonathan Silveira - Instagram: @ jonathandev01

salario = float(input("Digite o salário do colaborador: "))
if salario <= 280:
    print("O valor do novo salário do colaborador com rejuste é: ", salario * 0.2 + salario)
elif salario > 280 or salario < 700:
    print("O valor do novo salário do colaborador com rejuste é: ", salario * 0.15 + salario)
elif salario > 700 or salario < 1500:
    print("O valor do novo salário do colaborador com rejuste é: ", salario * 0.10 + salario)
elif salario > 1500:
    print("O valor do novo salário do colaborador com rejuste é: ", salario * 0.05 + salario)