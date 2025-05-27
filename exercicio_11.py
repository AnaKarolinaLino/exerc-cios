import json
import os

carro = 'cadastro_veiculo.json'

def carregar_dados():
    if os.path.exists(carro):
        with open(carro, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return[]
    

def obter_dados():
    
    marca_veiculo = input("Digite a marca do veículo: ")
    modelo_veiculo = input("Digite o modelo do veículo: ")
    ano_veiculo = int(input("Digite o ano em que o veículo foi fabricado: "))
    cor_veiculo = input("Digite a cor do veículo: ")

    veiculo = {
        "marca_veiculo": marca_veiculo,
        "modelo_veiculo": modelo_veiculo,
        "ano_veiculo": ano_veiculo,
        "cor_veiculo": cor_veiculo
        
    }

    return veiculo

def cadastrar_veiculo(carregar_veiculo):
    db_veiculos = carregar_dados()
    db_veiculos.append(carregar_veiculo)

    with open(carro, "w", encoding="utf-8") as arq_json:
        json.dump(db_veiculos, arq_json, indent=4, ensure_ascii=False)


def mostrar_veiculos(receber_carro):
    if receber_carro:
         for veiculo in receber_carro:
             print(f"""
              Marca do veículo: {veiculo["marca_veiculo"]}
              Modelo do veículo : {veiculo["modelo_veiculo"]}
              Ano do veículo: {veiculo["ano_veiculo"]}
              Cor do veículo: {veiculo["cor_veiculo"]}
              """)
    else:
        print("Não há veículos cadastrados.")
             



