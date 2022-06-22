#POO
class Carro:
    velmax=0
    ligado=False
    cor=""
    def __init__(self,vm,li,c):
        self.velmax=vm
        self.ligado=li
        self.cor=c
    def mostrar(self):
        print("Velocidade máxima: " + str(self.velmax))
        print("Cor: " + str(self.cor))
        estado="sim" if self.ligado else "N"
        print("Ligado: " + estado)
        print("----------------------------------------")

carro1=Carro(10,False,"Azul")
carro2=Carro(20,True,"Branco")

carro1.mostrar()
carro2.mostrar()
