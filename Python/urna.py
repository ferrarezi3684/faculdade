def urna_eleicao():
    candidatos = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    votos_nulos = 0
    votos_brancos = 0
    
    while True:
        print("Candidatos:")
        print("1 - Candidato ladrao")
        print("2 - Candidato bonzinho")
        print("3 - Candidato bandido")
        print("4 - Candidato bandidao")
        print("5 - Candidato miliciano")
        print("6 - Voto Nulo")
        print("7 - Voto em Branco")
        print("0 - Finalizar a votação")
        
        voto = int(input("Digite o número do candidato (ou 6 para nulo, 7 para branco, 0 para finalizar): "))
        
        if voto == 0:
            break
        elif voto == 6:
            votos_nulos += 1
        elif voto == 7:
            votos_brancos += 1
        elif voto in candidatos:
            candidatos[voto] += 1
        else:
            print("Voto inválido!")
    
    print("\nResultado da votação:")
    for candidato, votos in candidatos.items():
        print("Candidato {}: {} votos".format(candidato, votos))
    
    print("Votos Nulos: {}".format(votos_nulos))
    print("Votos Brancos: {}".format(votos_brancos))
    
    vencedor = max(candidatos, key=candidatos.get)
    print("Candidato {} venceu com {} votos.".format(vencedor, candidatos[vencedor]))

urna_eleicao()