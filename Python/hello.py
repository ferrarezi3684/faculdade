dic = {"Medico": 30000.00, "Professor": 1000.00, "Analista de Dados": 50000}
print(dic)
print(dic.values())
print(dic.keys())
print(dic.items())
print("Salario do professor = " + str(dic["Professor"]))
dic["Professor"] = 40000
print("Novo Salario do professor = " + str(dic["Professor"]))
dic2 = dic.copy()
del dic["Medico"] 
print(dic.items())
print(dic2.items())
dic.clear()
print(dic.items())
print(dic2.items())