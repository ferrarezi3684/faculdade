class Veiculo:
    def __init__(self, marca):
        self.marca = marca

    def mover(self):
        pass

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def som(self):
        pass

class AnimalMotorizado(Veiculo, Animal):
    def __init__(self, marca, nome):
        Veiculo.__init__(self, marca)
        Animal.__init__(self, nome)

    def mover(self):
        return f"{self.marca} {self.nome} está se movendo."

    def som(self):
        return f"{self.nome} faz um som."

animal_motorizado = AnimalMotorizado("Honda", "Bicho")

print(animal_motorizado.mover())  
print(animal_motorizado.som())    
