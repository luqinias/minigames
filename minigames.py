import forca
import adivinhacao

print ("*********************************")
print ("*******Escolha o seu jogo!*******")
print ("*********************************")

print("(1) Forca (2)Adivinhação")
jogo = int(input("Qual jogo? "))

if (jogo == 1):
    print("Jogando Forca!")               
    forca.jogar()

elif (jogo == 2):
    print("Jogando Adivinhação!")
    adivinhacao.jogar()

