while True:
    try:
        numero = input("Digite um número: ")
        numero = int(numero)

        operacao = input("Digite a operação (bin, oct, hex): ")
        while operacao not in ["bin", "oct", "hex"]:
            print("Operação inválida. Tente novamente.")
            operacao = input("Digite a operação (bin, oct, hex): ")

        if operacao == "bin":
            resultado = bin(numero)
        elif operacao == "oct":
            resultado = oct(numero)
        elif operacao == "hex":
            resultado = hex(numero)

        print("Resultado:", resultado)

    except ValueError:
        print("Número inválido. Tente novamente.")
    except KeyboardInterrupt:
        print("\nPrograma encerrado pelo usuário.")
        break
