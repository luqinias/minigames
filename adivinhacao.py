import random
def jogar():
     print ("*********************************")
     print ("Bem vindo ao jogo de adivinhação!")
     print ("*********************************")

     numero_secreto = random.randrange(1,101)
     total_tentativas = 0
     pontos = 150

     print("Qual nível de dificuldade que você vai jogar?")
     print("(1)Fácil (2)Médio (3)Difícil")
     nivel = int(input("Defina o nível: "))

     if   (nivel == 1) :
          total_tentativas = 20
     if   (nivel == 2) :
          total_tentativas = 15
     elif (nivel == 3) :
          total_tentativas = 10         
     elif (nivel < 1 or nivel > 3) :
          print("Escolha um nível de dificuldade entre 1 e 3")
               

     for rodada in range (1, total_tentativas+1) :
          print("Tentativa {} de {}".format(rodada, total_tentativas))
          chute = int (input("Digite um número entre 1 e 100: "))
          print("Você digitou ", chute)

          if (chute < 1 or chute > 100):
               print("Você deve digitar um número entre 1 e 100!")
               continue

          acertou =  chute == numero_secreto
          erro_maior = chute > numero_secreto
          erro_menor = chute < numero_secreto

          if (acertou):        
               print("Você acertou e fez {} pontos!".format(pontos))
               break
          else:
               if (erro_maior):
                    print("Você errou! Seu chute foi maior que o número secreto")
               elif (erro_menor):
                    print("Você errou! Seu chute foi menor que o número secreto")
                    pontos_perdidos = abs(numero_secreto - chute)
                    pontos = pontos - pontos_perdidos
     print("Fim de jogo!")
     
if (__name__ == "__main__"):
     jogar()