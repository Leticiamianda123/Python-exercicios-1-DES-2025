# Renata quer solicitar um financiamento, mas precisa verificar se cumpre os critérios:

# Salário mensal acima de R$ 3.000,00
# A parcela não pode ser maior que 35% do salário

salario = float(input("digite o salario mesal de renata: $"))
parcela = float (input("digite o valor da parcela dos funcionarios: R$"))

if salario <= 3000:
    print("finaciamentonegado,salario abaixo do minimo exigido")
    