dic = {"Nome": "thiago", "UltimoNome": "Gomes", "Idade": 36, "Curso": "Sistemas de informação", "Endereço": "Rua maria vicentina"}
print(dic.items())
print("Meu nome é " + dic["Nome"])
print("Meu ultimo nome é " + str(dic["UltimoNome"]))
del dic["Curso"]
print(dic)
dic["UltimoNome"] = "Ferrarezi"
print(dic)
print("Meu endereco é  " + str(dic["Endereço"]))
dic2 = dic.copy()
dic2["Nome"] = "BABY"
dic2["Idade"] = 25
print(dic2)