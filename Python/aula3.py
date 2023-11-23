def tabuada(numero):
    x  = 0
    while (x <= 10):
        print(str(numero) + " x " + str(x) + " = " + str(numero * x))
        x +=1

        
numero = int(input("Favor informe um numero inteiro: "))
tabuada(numero)