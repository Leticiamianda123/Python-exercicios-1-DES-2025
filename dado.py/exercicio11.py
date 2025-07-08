

#Crie um programa que receba o peso (kg) e a altura (m) de uma pessoa e calcule o IMC.
#Abaixo do peso (< 18.5)
#Peso normal (18.5 a 24.9)
#Sobrepeso (25 a 29.9)
#Obesidade (>= 30)

peso = float(input("Digite seu peso em kg(ex70.5):"))
altura = float(input("Digite sua altura em metros (ex:1.75):"))


if altura <=0:
        print("altura invalida. A altura deve ser maior que zero.")
  else:
 
        imc = peso / (altura ** 2)

    if imc < 18.5:
        print = ("Abaixo do peso")
    elif imc >= 18.5 <= imc <= 24.9:
        (classificacao = "Peso normal")
    elif 25 <= imc <= 29.9:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"

    






