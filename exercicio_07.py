import json
import os

db_clientes = "db_clientes.json"
# clientes = []

def carregar_dados():
    if os.path.exists(db_clientes):
        with open(db_clientes, "r", encoding="utf-8") as arq_josn:
            return json.load(arq_josn)
    else:
        return []




def obter_dados_cliente():
    nome_cliente = input("Digite seu nome: ")
    cpf_cliente = int(input("Digite seu cpf: "))
    rg_cliente = int(input("Digite o seu rg: "))
    data_de_nascimento_cliente = input("Digite sua data de nascimento: ")
    endereco_cliente = input("Digite o seu endereço: ")
    cidade_cliente = input("Digite sua cidade: ")
    estado_cliente = input("Digite o seu estado: ")
    telefone_cliente = int(input("Digite o seu número de telefone"))
    celular_cliente = int(input("Digite o seu celular: "))
    email_cliente = input("Digite o seu email: ")

    cliente = {
        "nome_ cliente": nome_cliente, 
        "cpf_cliente": cpf_cliente,
        "rg_cliente": rg_cliente,
        "data_de_nascimento_cliente": data_de_nascimento_cliente, 
        "endereco_cliente": endereco_cliente,
        "cidade_cliente": cidade_cliente, 
        "estado_cliente": estado_cliente,
        "telefone_cliente": telefone_cliente,
        "celular_cliente": celular_cliente,
        "email_cliente": email_cliente, 

     }

    return cliente

def cadastrar_cliente(dados_cliente):
    clientes = carregar_dados()
    clientes.append(dados_cliente)

    with open(db_clientes, "w", encoding="utf-8") as arq_josn:
        json.dump(clientes, arq_josn, indent=4, ensure_ascii=False)


def mostrar_dados_clientes(dados_clientes):
    for cliente in dados_clientes:
        print(f"""
              Nome do Cliente: {cliente["nome_cliente"]}
              CPF do Cliente: {cliente["cpf_cliente"]}
              RG do Cliente: {cliente["rg_cliente"]}
              Data de nascimento do Cliente: {cliente["data_nasc_cliente"]}
              Endereço do Cliente: {cliente["endereco_cliente"]}
              Cidade do Cliente: {cliente["cidade_cliente"]}
              Telefone do Cliente: {cliente["telefone_cliente"]}
              Celular do Cliente: {cliente["celular_cliente"]}
              Email do Cliente: {cliente["email_cliente"]}
""")
          
def iniciar_sistema():
    clientes = carregar_dados()
    while True:
        print("")
        print("="*80)
        print("Opção 1 - mostrar lista de clientes")
        print("Opção 2 - cadastrar clientes")
        print("Opção 3 - sair do sistema.")
        print("="*80)

        opcao = input("Escolha uma das opções do menu: ")

        if opcao == "1": 
            mostrar_dados_clientes(clientes)
        elif opcao == "2": 
            cadastrar_cliente(obter_dados_cliente())
        elif opcao == "3": 
            opcao("Sistema finalizado!")
            break 
        else: 
            print("Opção inválida, escolha uma das opções no menu.")

iniciar_sistema()

