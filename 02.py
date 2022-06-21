print("Jogo Python!")
print("---------------------")

numero_secreto = 43
maximo_tentaivas = 3
rodada = 1

while(rodada <= maximo_tentaivas):
    print("Tentativa {} de {},".format(rodada, maximo_tentaivas)) 
    tentativa = input("Digite o seu número: ")
    print("Você tentou o número: ", tentativa)

    if(numero_secreto == int(tentativa)):
        print("Acertou o número")
    else:
        if(int(tentativa) > numero_secreto):
            print("Seu chute foi muito alto")
        elif(int(tentativa) < numero_secreto):
            print("O chute foi menor do que o número desejado")
    rodada = rodada + 1
print("Fim de jogo")
