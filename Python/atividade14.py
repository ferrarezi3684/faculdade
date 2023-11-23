import random

def gerar_dados_aluno():
    nome = f"Aluno_{random.randint(1, 100)}"
    disciplina = f"Disciplina_{random.randint(1, 5)}"
    nota1 = random.uniform(0, 100)
    nota2 = random.uniform(0, 100)
    nota3 = random.uniform(0, 100)
    return f"Nome: {nome}, Disciplina: {disciplina}, Nota1: {nota1:.2f}, Nota2: {nota2:.2f}, Nota3: {nota3:.2f}"

with open("alunos.txt", "w") as arquivo:
    for _ in range(50):
        dados_aluno = gerar_dados_aluno()
        arquivo.write(dados_aluno + "\n")
def verificar_situacao(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    if media >= 60:
        return "Aprovado"
    else:
        return "Reprovado"

with open("alunos.txt", "r") as arquivo:
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

with open("Aprovados.txt", "r") as aprovados_arquivo, open("Reprovados.txt", "r") as reprovados_arquivo:
    print("Conteúdo do arquivo 'Aprovados.txt':")
    print(aprovados_arquivo.read())
    
    print("\nConteúdo do arquivo 'Reprovados.txt':")
    print(reprovados_arquivo.read())
