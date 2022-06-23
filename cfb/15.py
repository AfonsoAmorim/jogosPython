carros=[]

class Carro:
    nome=""
    potencia=0
    velMax=0
    ligado=False
    def __init__(self,nome,potencia):
        self.nome=nome
        self.potencia=potencia
        self.velMax=int(potencia)*2
        self.ligado=False
    def info(self):
        print("Nome: "+self.nome)
        print("Potência: "+str(self.potencia))
        print("Velocidade Máxima: "+str(self.velMax))
        print("Ligado: "+("sim" if self.ligado==True else "não"))
    def ligar(self):
        self.ligado=True
    def desligar(self):
        self.ligado=False

def NovoCarro():
    n=input("Digite carro: ")
    p=input("Digite a potência: ")
    car=Carro(n,p)
    carros.append(car)
    print("Carro criado")


