valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

if valor1 > valor2:
    maior = valor1
else:
    maior = valor2

print("O maior valor é:", maior)

ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = 2023  # Ano atual fictício para este exemplo

idade = ano_atual - ano_nascimento

if idade >= 16:
    print("Você pode votar este ano.")
else:
    print("Você não pode votar este ano.")

senha = int(input("Digite a senha: "))

if senha == 1234:
    print("ACESSO PERMITIDO")
else:
    print("ACESSO NEGADO")

quantidade_macas = int(input("Digite a quantidade de maçãs compradas: "))

if quantidade_macas < 12:
    valor_total = quantidade_macas * 0.30
else:
    valor_total = quantidade_macas * 0.25

print("Valor total da compra: R$ {:.2f}".format(valor_total))