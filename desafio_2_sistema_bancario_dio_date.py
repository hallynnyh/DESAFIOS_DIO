from datetime import datetime

def deposito(valor_deposito, extrato, saldo):

    if valor_deposito < 0:
        print('Não é possível realizar deposito de números negativos. Por favor, tente novamente')
    else:
        extrato.append((valor_deposito, datetime.now(), "Depósito"))
        saldo += valor_deposito
        print(f'Depósito realizado com sucesso! O novo saldo é de R$ {saldo:.2f}')
    return saldo

def saque(valor_saque, extrato, saldo, limite_saque):

    numero_saques = 0

    for i in range(len(extrato)):
        if extrato[i][2] == "Saque":
            numero_saques += 1
    
    if numero_saques >= limite_saque:
        print('Você atingiu o limite de saques diários. Por favor, tente novamente')
    elif valor_saque < 0 or valor_saque > 500:
        print('Não é possível realizar o saque. Por favor, tente novamente')
    elif valor_saque > saldo:
        print('Saldo insuficiente. Por favor, tente novamente')
    else:
        extrato.append((- valor_saque, datetime.now(), "Saque"))
        saldo -= valor_saque
        print(f'Saque realizado com sucesso! O novo saldo é de R$ {saldo:.2f}')
    return saldo

def imprimir_extrato(extrato, saldo):
   
    for i in range(len(extrato)):
        print(f'{extrato[i][2]}')
        print(f'Data: {extrato[i][1].strftime("%d/%m/%Y %H:%M:%S")}')
        print(f'Valor: R$ {(extrato[i][0]):.2f}')
    
    print(f'Extrato do dia {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}: R${saldo:.2f}')
        

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
LIMITE_SAQUES = 10

while True:

    opcao = input(menu).lower()

    if opcao == "d":
        valor_deposito = float(input('Digite o valor que deseja depositar: R$ '))
        saldo = deposito(valor_deposito, extrato, saldo)
 
    elif opcao == "s":
        valor_saque = float(input('Digite o valor que deseja sacar: R$ '))
        saldo = saque(valor_saque, extrato, saldo, LIMITE_SAQUES)

    elif opcao == "e":
        imprimir_extrato(extrato, saldo)
                
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")