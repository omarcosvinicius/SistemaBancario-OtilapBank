import textwrap

# Sistema Bancário - Otilap Bank V2

def menu():
    # Exibe o menu de opções do sistema bancário.

    menu = """\n
    ================= MENU ================
    [1]\t Depositar
    [2]\t Sacar
    [3]\t Extrato
    [4]\t Nova Conta
    [5]\t Listar Contas
    [6]\t Novo usuário
    [7]\t Listar usuários
    [0]\t Sair
    => """
    return input(textwrap.dedent(menu))

# Funções do sistema bancário

# Função para realizar um depósito
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n||||| Depósito realizado com sucesso! |||||")
    else:
        print("\n||||| Operação falhou! O valor informado está errado. |||||")

    return saldo, extrato

# Função para realizar um saque
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print("\n ||||| Operação falhou! Você não tem saldo suficiente. |||||")
    
    elif excedeu_limite:
        print("\n ||||| Operação falhou! O valor do saque excede o limite. |||||")
    
    elif excedeu_saques:
        print("\n ||||| Operação falhou! Número máximo de saques excedido. |||||")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n ||||| Saque realizado com sucesso! |||||")
    
    else:
        print("\n ||||| Operação falhou! O valor informado está errado. |||||")
    
    return saldo, extrato

# Função para exibir o extrato
def exibir_extrato(saldo, /, *, extrato):
    print("\n||||||||||||| EXTRATO ||||||||||||||")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("||||||||||||||||||||||||||||||||||||||\n")

# Função para criar usuário
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (apenas números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n||||| Já existe usuário cadastrado com esse CPF. |||||")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (DD/MM/AAAA): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/UF): ")

    usuarios.append({
        "nome":nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("\n||||| Usuário cadastrado com sucesso! |||||")

# Função para filtrar usuário pelo CPF
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

# Função para criar conta
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário (apenas números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n||||| Conta criada com sucesso! |||||")
        return {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
        }
    print("\n||||| Usuário não encontrado, tarefa de criação de conta cancelada. |||||")

# Função para listar contas
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            Conta Corrente:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

# Função para listar usuários
def listar_usuarios(usuarios):

    if usuarios:
        for usuario in usuarios:
            print(f"\nNome: {usuario['nome']} \nCPF: {usuario['cpf']}")
            print("================================")
    else:
        print("Não existem usuários cadastrados.")

# Função principal do sistema bancário
def main():
    
    # Função principal que executa o sistema bancário.
    
    # Variáveis iniciais
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":  # Depositar
            valor = float(input("Informe o valor do depósito: R$ "))

            saldo, extrato = depositar(saldo, valor, extrato)
            
        elif opcao == "2":  # Sacar
            valor = float(input("Informe o valor do saque: R$ "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )
        
        elif opcao == "3":  # Extrato
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "4":  # Nova Conta
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        
        elif opcao == "5":  # Listar Contas
            listar_contas(contas)

        elif opcao == "6":  # Criar usuário
            criar_usuario(usuarios)
        
        elif opcao == "7":  # Listar usuários
            listar_usuarios(usuarios)
        
        elif opcao == "0":  # Sair
            print("Otilap Bank agradece por utilizar nossos serviços!")
            print("Saindo do sistema...")
            break

# Executa a função principal
main()