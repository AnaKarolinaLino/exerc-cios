import json
import os

filmes = 'cadastro_filmes.json'

def carregar_dados():
    if os.path.exists(filmes):
        with open(filmes, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return []
    
def obter_dados():
    nome_filme = input("Informe o nome do filme: ")
    classificacao = int(input("Informe a classificação do filme: "))
    descricao = input("Informe a descrição do filme: ")
    categoria = input("Informe a categoria do filme: ")

    data_filme = {
        "nome_filme": nome_filme,
        "classificacao": classificacao,
        "descricao": descricao,
        "categoria": categoria
    }

    return data_filme

def cadastrar_filme(receber_filme):
    db_filmes = carregar_dados()
    db_filmes.append(receber_filme)

    with open(filmes, "w", encoding="utf=8") as arq_json:
        json.dump(db_filmes, arq_json, indent=4, ensure_ascii=False)

def mostrar_filmes(filmes):
    if filmes:
     for filme in filmes:
        print(f"""
              Nome do Filme: {filme["nome_filme"]}
              Classificaçãõ do Filme: {filme["classificacao"]}
              Descrição do Filme: {filme["descricao"]}
              Categoria do Filme: {filme["categoria"]}
              """)
    else:
        print("Não exise nenhum filme cadastrado.")


def iniciar_sistema():
    db_filmes = carregar_dados()

    while True:
        print("")
        print("="*80)
        print("Opção 1 - Mostrar Lista de Filmes")
        print("Opção 2 - Cadastrar Filme")
        print("Opção 3 - Sair do Sistema.")
        print("="*80)

        opcao = input("Esccolha uma das opções no menu: ")

        if opcao == "1":
            mostrar_filmes(db_filmes)
        elif opcao == "2":
            cadastrar_filme(obter_dados())
        elif opcao == "3":
            print("Sistema Finalizado!")
            break
        else:
            print("Opção inválida, escolha uma das opções do menu.")  

iniciar_sistema()

