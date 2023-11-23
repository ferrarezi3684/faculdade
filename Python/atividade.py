fruta1 = "Maçã"
fruta2 = "Banana"
fruta3 = "Pera"
fruta4 = "Uva"
fruta5 = "Abacaxi"

preco1 = 1.00
preco2 = preco1 * 2
preco3 = preco1 / 2
preco4 = preco3 * 3
preco5 = preco4 / 2

lista_de_frutas = [
    (fruta1, preco1),
    (fruta2, preco2),
    (fruta3, preco3),
    (fruta4, preco4),
    (fruta5, preco5)
]

for fruta, preco in lista_de_frutas:
    print("A fruta {} custa {:.2f}".format(fruta, preco))