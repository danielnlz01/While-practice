a=int(input("Dame a\n"))
b=int(input("Dame b\n"))

while (a!=(b+1)):
  if (a%2==0):
    print(a)
  a+=1
  
total=0
numeros_leidos=0
  
while True:
  numero=int(input("Dame el número\n"))
  total=total+numero
  numeros_leidos+=1
  if (total>=1000):
    break
  
print(total)
print(numeros_leidos)

numero=int(input("Dame el número\n"))
contador=1
suma=0
while contador<numero:
  if(numero%contador)==0:
    suma=suma+contador
  contador+=1
if(suma==numero):
  print("Es perfecto")
else:
  print("No es perfecto")
  
numero=int(input("Dame el número\n"))
contador=numero-1
suma=0
while contador>0:
  if(numero%contador)==0:
    suma=suma+contador
  contador-=1
if(suma==numero):
  print("Es perfecto")
else:
  print("No es perfecto")
  

