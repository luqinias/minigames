import random

def jogar():
     
     imprimir_mensagem_bemvindo()     
     palavra_secreta = escolher_palavrasecreta()
     
     letras_acertadas = ["_" for letra in palavra_secreta]
     #substituir letra por caractere
     print(letras_acertadas)

     enforcou = False
     acertou = False
     tentativas = 0
     
     while(not enforcou and not acertou):
          
          chute = pede_chute_jogador()
          
          if(chute in palavra_secreta):
               marca_chute_correto(chute, letras_acertadas, palavra_secreta)           
          else:
               tentativas += 1
          #condição para adição de tentativas
          enforcou = tentativas==6
          acertou = "_" not in letras_acertadas
          print(letras_acertadas)
          

     if(acertou):
          imprime_mensagem_vencedor()
     else:
          imprime_mensagem_perdedor(palavra_secreta)






def imprimir_mensagem_bemvindo():
     print ("*********************************")
     print ("Bem vindo ao jogo de Forca!")
     print ("*********************************")

def escolher_palavrasecreta():
     arquivo = open("palavras.txt", "r")
     palavras = []

     for linha in arquivo:
          linha = linha.strip()
          palavras.append(linha)

     arquivo.close()

     numero = random.randrange(0,len(palavras))
     palavra_secreta = palavras[numero].upper()
     return palavra_secreta

def pede_chute_jogador():
     chute = input("Qual letra? ")
     chute = chute.strip().upper()
     return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
     index = 0
     for letra in palavra_secreta:
          if (chute == letra):
               letras_acertadas[index] = letra 
          index += 1

def imprime_mensagem_vencedor():
     print("Você ganhou!!")

def imprime_mensagem_perdedor(palavra_secreta):
     print("Você perdeu!! A palavra secreta era: {}".format(palavra_secreta))

if (__name__ == "__main__"):
     jogar()
