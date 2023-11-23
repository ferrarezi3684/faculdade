class Conta:
    def __init__(self, agencia, numero_conta, nome_cliente, cpf, saldo_inicial=0.0):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.nome_cliente = nome_cliente
        self.cpf = cpf
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    def imprimir_saldo(self):
        print(f"Saldo atual da conta: R${self.saldo:.2f}")