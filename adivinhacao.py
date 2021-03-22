import random

print("Bem vindo ao jogo de adivinhação")
print("-----------------------------------")

numero_secreto = random.randrange(1, 101)
rodada = 1
pontos_totais = 1000
#print(numero_secreto)


print("(1) Facil (2) Medio (3) Dificil")
dificuldade = int(input("Qual o nivel de dificuldade?"))

while (dificuldade < 1) or (dificuldade > 3):
    print("Selecione a dificuldade correta. /n")
    print("(1) Facil (2) Medio (3) Dificil")
    dificuldade = int(input("Qual o nivel de dificuldade?"))

if(dificuldade == 1):
    tentativas_total = 20
elif(dificuldade == 2):
    tentativas_total = 10
else:
    tentativas_total = 5


for rodada in range(1,tentativas_total +1):
    print("Tentativa {} de {}".format(rodada, tentativas_total))
    chute = input("Digite o seu numero de 1 a 100: ")
    numero = int(chute)

    if (numero < 1 or numero > 100):
        print("Voce deve digitar um numero entre 1 e 100!")
        continue

    acerto = numero == numero_secreto
    maior = numero > numero_secreto

    if(acerto):
        print("Você acertou!")
        print("Sua pontuação foi {}!".format(pontos_totais))
        break
    else:
        if(maior):
            print("Seu chute foi maior que o numero secreto!/n Errou!")
        else:
            print("Seu chute foi menor que o numero secreto!/n Errou!")
        pontos_perdidos = abs(numero_secreto - numero)
        pontos_totais = pontos_totais - pontos_perdidos

        print("---------------------------")
print("Fim do jogo")