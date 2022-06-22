# nome=input("Digite seu nome: ")
# print("Nome digitado: " + nome)

i=0
while i<5:
    print(i)
    i+=1

#tuplas 
tuplas=("hrv","jetta","celta","gol")
print(tuplas)
tuplasConvertidas=list(tuplas)
tuplasConvertidas[0]="focus"
print(tuplasConvertidas)

#matrizes - coleção de arrays 
motos=[ 
    ["Modelo","hrv"],
    ["Fabricante","Honda"],
    ["Ano","2016"],
]
print(motos[0][0])
print(motos[1][1])

for linha,coluna in motos:
    print(" Linha: " + linha + " coluna " + coluna)
