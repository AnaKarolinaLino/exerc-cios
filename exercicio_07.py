clientes = []

def obter_dados_clientes():
    nome_cliente = input("Digite o Nome: ")
    cpf_cliente = int(input("Digite o CPF: "))
    rg_cliente = int(input("Digite o RG: "))
    data_nasc_cliente = input("Digite a Data de Nascimento: ")
    endereco_cliente = input("Digite o Endereço: ")
    cidade_cliente = input("Digite a Cidade: ")
    estado_cliente = input("Digite o Estado: ")
    telefone_cliente = int(input("Digite o Telefone: "))
    celular_cliente = int(input("Digite o Celular: "))
    email_cliente = input("Digite o E-MAIL: ")

    cliente = {
        "nome_cliente": nome_cliente,
        "cpf_cliente": cpf_cliente,
        "rg_cliente": rg_cliente,
        "data_nasc_cliente": data_nasc_cliente,
        "endereco_cliente": endereco_cliente,
        "cidade_cliente": cidade_cliente,
        "estado_cliente": estado_cliente,
        "telefone_cliente": telefone_cliente,
        "celular_cliente": celular_cliente,
        "email_cliente": email_cliente

     }
    
    return cliente

def cadastrar_cliente(dados_cliente):
    clientes.append(dados_cliente)

    return clientes

def mostrar_dados_clientes(dados_clientes):
    for cliente in dados_clientes:
        print(f"""
              Nome do Cliente: {cliente["nome_cliente"]}
              CPF do Cliente: {cliente["cpf_cliente"]}
              RG do Cliente: {cliente["rg_cliente"]}
              Data de Nascimento do Cliente: {cliente["data_nasc_cliente"]}
              Endereço do Cliente: {cliente["endereco_cliente"]}
              Cidade do Cliente: {cliente["cidade_cliente"]}
              Estado do Cliente: {cliente["estado_cliente"]}
              Telefone do Cliente: {cliente["telefone_cliente"]}
              Celular do Cliente: {cliente["celular_cliente"]}
              EMAIL do Cliente: {cliente["email_cliente"]}
    """)
        

def iniciar_sistema():
    while True:
        print("")
        print("="*80)
        print("Opção 1 - Mostrar Lista de Clientes")
        print("Opção 2 - Cadastrar Clientes")
        print("Opção 3 - Sair do Sistema")
        print("="*80)

        opcao = input("Escolha uma das opções do Menu: ")

        if opcao == "1":
            mostrar_dados_clientes(clientes)
        elif opcao == "2":
            cadastrar_cliente(obter_dados_clientes())
        elif opcao == "3":
            print("Sistema Finalizado!")
            break
        else:
            print("Opção inválida, escolha uma das opções do menu.")


iniciar_sistema()
