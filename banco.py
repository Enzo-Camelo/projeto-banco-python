extrato = ""
limite = 500 
numero_saques = 0
LIMITE_SAQUES = 3
saldo = 0 

menu = """
Qual operação deseja realizar?

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """



while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("A operação falhou! O valor informado é inválido.")


    
    elif opcao == "s":
        
        if saldo > 0:

            if numero_saques < LIMITE_SAQUES:
                valor = float(input("Informe o valor do saque: "))

                if valor <= saldo:

                    if valor > 0:

                        if valor < limite:
                            saldo -= valor
                            extrato += f"Saque: R$ {valor:.2f}\n"
                            numero_saques += 1
                        else:
                            print("Operação falhou! O valor excede o limite de R$ 500.00.")

                    else:
                        print("Operação falhou! Não é possível sacar um valor negativo.")

                else:
                    print("Saldo insuficiente.")
            
            else:
                print("Você excedeu o limite de saques.")

        else:
            print("Você não possui saldo suficiente para esta operação.")
    


    elif opcao == "e":
        print("------------------ EXTRATO ------------------")
        if extrato == "":
            print("Nenhuma movimentação foi realizada na conta ainda.")
        else:
            print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("---------------------------------------------")
    


    elif opcao == "q":
        print("Obrigado por escolher nosso banco!\nVolte sempre!")
        break



    else:
        print("Opção inválida.\nPor favor escolha uma das opções do menu.")
