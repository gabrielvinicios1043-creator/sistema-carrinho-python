# Sistema simples de carrinho de compras em Python

carrinho = []

while True:
    esc = input(
        "\nEscolha uma opção:\n"
        "[1] - Adicionar produto\n"
        "[2] - Ver Carrinho\n"
        "[3] - Ver total do carrinho\n"
        "[4] - Sair\n"
    )

    if esc == "1":
        produto = input("Qual o nome do produto? ")
        preco = float(input("Qual o valor do produto? "))
        carrinho.append([produto, preco])
        print("Produto adicionado com sucesso!")

    elif esc == "2":
        if carrinho:
            print("\nItens no carrinho:")
            for item in carrinho:
                print(f"- {item[0]} | R$ {item[1]:.2f}")
        else:
            print("Carrinho vazio!")

    elif esc == "3":
        if carrinho:
            total = sum(item[1] for item in carrinho)
            print(f"\nTotal do carrinho: R$ {total:.2f}")
            print(f"Quantidade de itens: {len(carrinho)}")
        else:
            print("Carrinho vazio!")

    elif esc == "4":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida!")
