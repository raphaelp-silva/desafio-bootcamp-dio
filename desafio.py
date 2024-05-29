menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

#trabalhando na operação de DEPOSITO
    if opcao == "d":
        valor_deposito = float(input("Qual é o valor que você deseja depositar? R$"))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Valor em depósito: R$ \033[32m {valor_deposito:.2f} \033[m \n"
        else: print("Operação inválida, revise e tente novamente!")
#trabalhando na operação de SAQUE
    elif opcao == "s":
        valor_saque = float(input("Qual é o valor que você deseja sacar? R$"))

        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saques:
            print("Você excedeu o limite de saque diário, tente novamente amanhã!")
        elif excedeu_saldo:
            print("Você excedeu o valor do seu saldo! tente novamente com outro valor")
        elif excedeu_limite:
            print("Você excedeu o limite ed R$ 500,00 reais por saque. Tente outro valor!")
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ \033[31m {valor_saque:.2f} \033[m \n"
            numero_saques += 1
        else:
            print("Operação inválida! tente novamente")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")


    elif opcao == "q":
        print("Obrigado por trabalhar conosco! até a próxima")
        break

    else:
        print("Operação inválida, por favor selecione outra opção.")
       