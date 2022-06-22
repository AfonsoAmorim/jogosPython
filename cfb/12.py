class NPC: #superClasse
    def __init__(self,nome,time,forca,municao):
        self.nome=nome
        self.time=time
        self.forca=forca
        self.municao=municao
        self.vivo=True
        self.energia=100
    def info(self):
        print("Nome: " + self.nome)
        print("Time: " + str(self.time))
        print("Força: " + str(self.forca))
        print("Munição: " + str(self.municao))
        print("Vivo: " + ("sim" if self.vivo else "não"))
        print("Energia: " + str(self.energia))
        print("-----------------------------------------")

class Soldado(NPC):
    def __init__(self, nome, time):
        self.forca=200
        self.municao=200
        super().__init__(nome, time, self.forca,self.municao)

class Guarda(NPC):
    def __init__(self, nome, time):
        self.forca=20
        self.municao=10
        super().__init__(nome, time, self.forca, self.municao)

class Elite(NPC):
    def __init__(self, nome, time):
        self.forca=5
        self.municao=55
        super().__init__(nome, time, self.forca, self.municao)