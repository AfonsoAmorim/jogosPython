curso="Curso de back end"
curso2="Novo curso"
dia=22
cursoEData="{} e de {} no dia {}"

print(curso[0:5])
print("Tamanho: " + str(len(curso)))
print(curso.upper())
print(curso.replace("back","Java"))
usoSplit=curso.split(" ")
print(usoSplit[1])
 
resposta="Python" in curso #verificando se Python está em curso
print(resposta)

resposta2=curso+curso2
print(resposta2)

print(cursoEData.format(curso,curso2,dia)) #utilizando o format



