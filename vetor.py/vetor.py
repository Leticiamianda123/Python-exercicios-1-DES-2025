#Lista (vetor) com 5 frutas 
 frutas = {"MAÇÃ","Banana,"Laranja","Uva, "manga"}




# mostra a lista de frutas para o jogador 
prit("lista de frutas:")
for i in renge (len(frutas)):
 print("f"{i + 1}-{frutas}[i]}")

 # sorteia uma posição aleatoria de 1 a 5 
 posicao_sorteado = rondom.radint(1,5)
 # o usuario vede tentar adivinhar qual fruta voce esta na posicao sorteada 
 palpite = input ("qual fruta voce acha que esta na posiçao sorteada?")
  


  # descobre a fruta correta com base na posiçao sorteada 
    fruta_certa = frutas [posicao_sorteada _ 1 ]
 
 #verifica se palpite esta correto 
 if palpite. capatalize () == frutas_certa:
   prit("parabens! voce acertou!")
   print(f"a fruta na posiçao {posiçao _ sorteada}era realmente {fruta_certa}.")
 else:
   print