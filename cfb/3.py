import random
#números aleatórios 
num=random.randrange(1,20)
print(num)

num2=[
    random.randrange(1,20),
    random.randrange(1,20),
    random.randrange(1,20)
] #list, array em Python 
print(num2)

def soma(n1,n2):
    return n1+n2

print(soma(10,5))