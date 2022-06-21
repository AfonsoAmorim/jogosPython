print("Jogo Python!")
print("---------------------")

numero_secreto = 43

tentativa = input("Digite o seu número: ")
print("Você tentou o número: ", tentativa)

if(numero_secreto==int(tentativa)):
    print("Acertou o número")
else:
    print("Você errou!!")

