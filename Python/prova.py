while True:
    numero = input("Digite um número ou ('sair' para sair): ")
    
    if numero.lower() == 'sair':
        break
    
    try:
        numero = int(numero)
        opcao = input("Digite '1' para listar em ordem crescente ou '2' para listar em ordem decrescente: ")

        if opcao == '1':
            for i in range(numero + 1):
                print(i, end=' ')
        elif opcao == '2':
            for i in range(numero, -1, -1):
                print(i, end=' ')
        else:
            print("Opção inválida. Digite 'crescente' ou 'decrescente'.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro ou 'sair' para sair.")
