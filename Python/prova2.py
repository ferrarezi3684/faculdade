# Inicialize dicionários para manter o controle das estatísticas
paises = {}
pilotos = {}
equipes = {}

with open('formula1.txt', 'r') as file:
    linhas = file.readlines()

for linha in linhas:
    campos = linha.strip().split(';')
    ano = campos[0].strip()
    pais = campos[1].strip()
    piloto = campos[2].strip()
    equipe = campos[3].strip()
    if pais in paises:
        paises[pais] += 1
    else:
        paises[pais] = 1
    if piloto in pilotos:
        pilotos[piloto] += 1
    else:
        pilotos[piloto] = 1
    if equipe in equipes:
        equipes[equipe] += 1
    else:
        equipes[equipe] = 1
pais_mais_vitorioso = max(paises, key=paises.get)
vitórias_pais = paises[pais_mais_vitorioso]
piloto_mais_vitorioso = max(pilotos, key=pilotos.get)
vitórias_piloto = pilotos[piloto_mais_vitorioso]
equipe_mais_vitoriosa = max(equipes, key=equipes.get)
vitórias_equipe = equipes[equipe_mais_vitoriosa]

print(f"O país que mais venceu na Fórmula 1 foi {pais_mais_vitorioso} com {vitórias_pais} vitórias.")
print(f"O piloto que mais venceu na Fórmula 1 foi {piloto_mais_vitorioso} com {vitórias_piloto} vitórias.")
print(f"A equipe que mais venceu na Fórmula 1 foi {equipe_mais_vitoriosa} com {vitórias_equipe} vitórias.")
