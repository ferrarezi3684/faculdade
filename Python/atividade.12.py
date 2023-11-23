nome = input("Digite o nome do aluno: ")
av1 = float(input("Digite a nota da AV1: "))
av2 = float(input("Digite a nota da AV2: "))
av3 = float(input("Digite a nota da AV3: "))

media = (av1 + av2 + av3) / 3

with open("notas.txt", "a") as arquivo:
    arquivo.write(f"Nome: {nome}\n")
    arquivo.write(f"Notas: AV1 = {av1}, AV2 = {av2}, AV3 = {av3}\n")
    arquivo.write(f"Média: {media:.2f}\n")
    arquivo.write("\n")


def verificar_aprovacao(media):
    if media >= 6.0:
        return "Aprovado"
    else:
        return "Reprovado"

with open("notas.txt", "r") as arquivo:
    linhas = arquivo.readlines()

for i in range(0, len(linhas), 4):
    nome = linhas[i].strip().split(": ")[1]
    notas = linhas[i+1].strip().split(": ")[1].split(", ")
    media = float(linhas[i+2].strip().split(": ")[1])
    situacao = verificar_aprovacao(media)
    
    print(f"Aluno: {nome}")
    print(f"Notas: AV1 = {notas[0]}, AV2 = {notas[1]}, AV3 = {notas[2]}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")
    print()