#  Juliana está coordenando entregas de projetos e precisa calcular o tempo total necessário 
# para finalizar três tarefas: X, Y e Z.
#  Se alguma tarefa estiver com o tempo de entrega negativo, deve-se exibir uma mensagem de 
# erro e não somar o totadia


dia01 = int(input("digite o tempo  nessesario para entregar atividade x"))
dia01 = int(input("digite o tempo nessesario para entregar atividade y "))
dia03 = int(input("digite o tempo nessesario para entregar atividade  z "))

if dia01 < 0 or dia02 < 0 or dia03 < o:
    print("erro negativo.")
else:
    soma = dia01 + dia02 + dia03 
    print("tempo total da atividade: {soma} dias")


