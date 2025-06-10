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
Opção [4] - Cadastrar cliente
Opção [5] - Cadastrar conta
Opção [6] - Sair
---------------------------------------------------
"""

# Variáveis globais para armazenar o saldo, limite de saque, extrato e contagem de saques
saldo = 0
limite_saque = 500
extrato = []
numero_saques = 0
limite_saques = 3

# Lista global para armazenar os usuários/clientes
usuarios = []

# Lista global para armazenar as contas correntes
contas = []

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

# Função para cadastrar usuário
def cadastrar_usuario():
    global usuarios
    print("\n--- Cadastro de Usuário/Cliente ---")
    nome = input("Nome completo: ").strip()
    data_nascimento = input("Data de nascimento (DD/MM/AAAA): ").strip()
    cpf = input("CPF (apenas números): ").strip()
    # Remove qualquer caractere que não seja número
    cpf = ''.join(filter(str.isdigit, cpf))
    # Verifica se o CPF já está cadastrado
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("Erro: Já existe um usuário cadastrado com este CPF.")
        time.sleep(5)
        return
    endereco = input("Endereço (logradouro, número - bairro - cidade/sigla estado): ").strip()
    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")
    time.sleep(5)

def cadastrar_conta():
    global contas, usuarios
    print("\n--- Cadastro de Conta Corrente ---")
    cpf = input("Informe o CPF do usuário (apenas números): ").strip()
    cpf = ''.join(filter(str.isdigit, cpf))
    # Busca o usuário pelo CPF
    usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
    if not usuario:
        print("Usuário não encontrado. Cadastre o usuário primeiro.")
        time.sleep(5)
        return
    agencia = "0001"
    numero_conta = len(contas) + 1
    conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario
    }
    contas.append(conta)
    print(f"Conta criada com sucesso! Agência: {agencia} | Número da conta: {numero_conta}")
    time.sleep(5)

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
            cadastrar_usuario()
        elif opcao == '5':
            cadastrar_conta()
        elif opcao == '6':
            print("Otilap Bank agradece por utilizar nossos serviços!")
            print("Saindo do sistema...")
            time.sleep(5) # Aguarda 5 segundos para sair do sistema
            break
        else:
            print("Opção inválida. Tente novamente.")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()