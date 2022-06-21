print("Jogo Python!")
print("---------------------")

numero_secreto = 43

tentativa = input("Digite o seu número: ")
print("Você tentou o número: ", tentativa)

if(numero_secreto==int(tentativa)):
    print("Acertou o número")
else:
    if(int(tentativa) > numero_secreto):
        print("Seu chute foi muito alto")
    elif(int(tentativa)<numero_secreto):
        print("O chute foi menor do que o número desejado")

print("Fim de jogo")



