import datetime

carros=["HRV","JETTA","FORDA KA"]

interatorCarros=iter(carros)
print(next(interatorCarros))
print(next(interatorCarros))
print(next(interatorCarros))

#----------------------------------------------------------
dataatual=datetime.datetime.now()
print(dataatual)
print(dataatual.day)
print(dataatual.month)