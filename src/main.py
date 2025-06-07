import time

# Este código implementa um sistema bancário simples com funcionalidades de depósito, saque e consulta de saldo.
# O usuário pode realizar depósitos, saques (com limites) e consultar o saldo e extrato de transações.
# O código é modularizado com funções específicas para cada operação, facilitando a manutenção e compreensão.
# Sistema Otilap Bank

#String com o menu de operações disponíveis
menu = """
---------- Menu de Operações Otilap Bank ----------
Opção [1] - Realizar depósito
Opção [2] - Realizar saque
Opção [3] - Consultar saldo/extrato
Opção [4] - Sair
---------------------------------------------------
"""

# Variáveis globais para armazenar o saldo, limite de saque, extrato e contagem de saques
saldo = 0
limite_saque = 500
extrato = []
numero_saques = 0
limite_saques = 3

# Funções para realizar as operações bancárias
# Função para realizar depósito
def realizar_deposito(valor):
    global saldo
    if valor > 0:
        # Realiza o depósito
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito realizado com sucesso! Saldo atual: R$ {saldo:.2f}")
        # Simula um atraso para o processamento do depósito
        print("Processando depósito...")        
        time.sleep(5)  # Aguarda 5 segundos para simular processamento
    else:
        print("Valor de depósito inválido.")
        print("\nRetornando ao menu principal...")
        time.sleep(5)

# Função para realizar saque
def realizar_saque(valor):
    global saldo, numero_saques
    if valor > saldo:
        print("Saldo insuficiente para saque.")
        print("\nRetornando ao menu principal...")
        time.sleep(5) 
    elif valor > limite_saque:
        print(f"Valor de saque excede o limite de R$ {limite_saque:.2f}.")
        print("\nRetornando ao menu principal...")
        time.sleep(5)
    elif numero_saques >= limite_saques:
        print(f"Limite de saques diários atingido ({limite_saques} saques).")
        print("\nRetornando ao menu principal...")
        time.sleep(5)
    else:
        # Realiza o saque
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print(f"Saque realizado com sucesso! Saldo atual: R$ {saldo:.2f}")
        # Simula um atraso para o processamento do depósito
        print("\nProcessando saque...")
        time.sleep(5) # Aguarda 5 segundos para simular processamento

# Função para consultar saldo e extrato
def consultar_saldo_extrato():
    global saldo, extrato
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    time.sleep(5) # Aguarda 5 segundos para simular processamento para exibir extrato
    if extrato:
        print("Extrato:")
        print("---------------------------------------------------")
        
        # Exibe cada transação no extrato
        for i, transacao in enumerate(extrato, start=1):            
            print(f"{i}. {transacao}")
        
        print(f"Total de transações: {len(extrato)}")
        print("---------------------------------------------------")        
        time.sleep(5) # Aguarda 5 segundos para voltar ao menu principal        
    else:
        print("Nenhuma operação realizada.")
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("\nRetornando ao menu principal...")
        time.sleep(5) # Aguarda 5 segundos para voltar ao menu principal

# Função principal que exibe o menu e processa as opções do usuário
def main():
    while True:
        print(menu)
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            valor = float(input("Informe o valor do depósito: R$ "))
            realizar_deposito(valor)
        elif opcao == '2':
            valor = float(input("Informe o valor do saque: R$ "))
            realizar_saque(valor)
        elif opcao == '3':
            consultar_saldo_extrato()
        elif opcao == '4':
            print("Otilap Bank agradece por utilizar nossos serviços!")
            print("Saindo do sistema...")
            time.sleep(5) # Aguarda 5 segundos para sair do sistema
            break
        else:
            print("Opção inválida. Tente novamente.")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()