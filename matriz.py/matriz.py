# lista de alunos (vetor)
alunos = ["alice,""bruno,""carla"]

#dias das semana (colunas da matriz )
dias = ["seg," "ter," "qua" ,"qui"]

# cria uma matriz vazia de reservas (valores e padrão :'ausente')
reserva = [["ausente " for _ in alunos]

# preencher a matriz com dados inserido pelo usuario 
print("preencha com 'S' para presença  e 'x'para ausẽncia:") 

for i,aluno  in enumerante (alunos ):
print(f"\nAluno: {aluno }")
for j, dia in enumerente (dias ):
entrada = input(f"{dias }: ")
if entrada.upper()== 'S' :
reserva [I] [j] =="presente "

# Exibir a tabela final 
print("\ntabela de reservas:")
print(f"")