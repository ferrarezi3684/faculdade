nota1= float (input("digite a nota 1: "))
print(nota1)
nota2 = float (input("digite a nota 2: "))
print(nota2)
media = (nota1 + nota2) / 2 
print (media)
if (media <= 3) :
    print ("reprovado")
elif  (media < 5) :
    print ("optativa")
else:
    print ("aprovado")