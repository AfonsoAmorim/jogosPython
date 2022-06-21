num = 10

def numeroDez():
    print(num)
numeroDez()

def escopoGlobal():
    global canal
    canal="Teste escopo global"
escopoGlobal()
print(canal)