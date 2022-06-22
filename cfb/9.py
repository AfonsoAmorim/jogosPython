def soma(x,y):
    return x+y
print(soma(10,20))

def bomDia():
    print("Bom dia usuário!")
bomDia()

def somarNnumeros(*num): #soma vários valores no input
    r=0
    for n in num:
        r+=n
    print("Soma = " + str(r))

somarNnumeros(10,20,30,30,10,10,4)


