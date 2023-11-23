import random

def main():
    numero_sorteado = random.randint(0, 100)
    tentativas = 0
    limite_tentativas = 10  # Pode ajustar esse valor conforme necessário

    while True:
        tentativa = int(input("Digite um número entre 0 e 100: "))
        tentativas += 1

        if tentativa == numero_sorteado:
            print(f"Parabéns! Você acertou o número {numero_sorteado} em {tentativas} tentativas.")
            break
        elif abs(tentativa - numero_sorteado) <= 5:
            print(f"Está quente! - em {tentativas} tentativa(s).")
        else:
            print(f"Está frio! - em {tentativas} tentativa(s).")

        if tentativas >= limite_tentativas:
            print(f"Você excedeu o número máximo de tentativas. O número sorteado era {numero_sorteado}.")
            break

if __name__ == "__main__":
    main()