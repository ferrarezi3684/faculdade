# Classe mãe (superclasse)
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def som(self):
        pass

# Classes filhas (subclasses)
class Cachorro(Animal):
    def som(self):
        return f"{self.nome} faz au au!"

class Gato(Animal):
    def som(self):
        return f"{self.nome} faz miau!"

class Pato(Animal):
    def som(self):
        return f"{self.nome} faz quack!"

cachorro = Cachorro("Rex")
gato = Gato("Felix")
pato = Pato("Donald")


print(cachorro.som())  
print(gato.som())      
print(pato.som())      
