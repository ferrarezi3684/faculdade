class Voo:
    def __init__(self, data, horario):
        self.data = data
        self.horario = horario
        self.passageiros = []

    def adicionar_passageiro(self, nome):
        if len(self.passageiros) < 100:
            self.passageiros.append(nome)
            print(f"{nome} foi adicionado ao voo com sucesso!")
        else:
            print("Não há mais vagas disponíveis para este voo.")

    def remover_passageiro(self, nome):
        if nome in self.passageiros:
            self.passageiros.remove(nome)
            print(f"{nome} foi removido do voo.")
        else:
            print(f"{nome} não está neste voo.")

    def listar_passageiros(self):
        print("Lista de passageiros no voo:")
        for passageiro in self.passageiros:
            print(passageiro)

# Exemplo de uso da classe Voo
if __name__ == "__main__":
    voo1 = Voo("10/09/2023", "10:00")

    voo1.adicionar_passageiro("Alice")
    voo1.adicionar_passageiro("Bob")
    voo1.adicionar_passageiro("Charlie")

    voo1.listar_passageiros()

    voo1.remover_passageiro("Bob")

    voo1.listar_passageiros()
