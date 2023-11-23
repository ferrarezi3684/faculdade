# Criar um arquivo com os dados dos alunos
with open("dados_alunos.txt", "w") as arquivo:
    for i in range(50):
        nome = input(f"Digite o nome do aluno {i + 1}: ")
        disciplina = input(f"Digite a disciplina do aluno {i + 1}: ")
        nota1 = float(input(f"Digite a nota 1 do aluno {i + 1}: "))
        nota2 = float(input(f"Digite a nota 2 do aluno {i + 1}: "))
        nota3 = float(input(f"Digite a nota 3 do aluno {i + 1}: "))
        arquivo.write(f"Nome: {nome}, Disciplina: {disciplina}, Nota1: {nota1}, Nota2: {nota2}, Nota3: {nota3}\n")


def verificar_situacao(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    if media >= 60:
        return "Aprovado"
    else:
        return "Reprovado"

with open("dados_alunos.txt", "r") as arquivo:
    linhas = arquivo.readlines()


with open("Aprovados.txt", "w") as aprovados_arquivo, open("Reprovados.txt", "w") as reprovados_arquivo:
    for linha in linhas:
        partes = linha.strip().split(", ")
        nome = partes[0].split(": ")[1]
        disciplina = partes[1].split(": ")[1]
        nota1 = float(partes[2].split(": ")[1])
        nota2 = float(partes[3].split(": ")[1])
        nota3 = float(partes[4].split(": ")[1])
        
        situacao = verificar_situacao(nota1, nota2, nota3)
        
        if situacao == "Aprovado":
            aprovados_arquivo.write(f"Nome: {nome}, Disciplina: {disciplina}, Situação: {situacao}\n")
        else:
            reprovados_arquivo.write(f"Nome: {nome}, Disciplina: {disciplina}, Situação: {situacao}\n")

print("Arquivos 'Aprovados.txt' e 'Reprovados.txt' gerados com sucesso!")
