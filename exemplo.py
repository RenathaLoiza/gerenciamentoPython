import random

#sistema de genrenciamento 

procedimentos={
    "Limpeza de pele":{"preço": 40.00},
    "Desing com Henna":{"preço": 60.00},
    "Estenção de cilios":{"preço": 200.00},
    "Depilação corpo inteiro":{"preço": 100.00},
    "Drenagem":{"preço": 150.00}
}

total_vendas = 0.0

def exibir_produtos():
    print("\nProdutos disponíveis:")
    for procedimentos, info in procedimentos.items():
        print(f"{procedimentos} - Preço: R${info['preço']:.2f} unidades")
    print()
def realizar_venda():
    global total_vendas
    produto_vendido = input("Digite o nome do produto que deseja comprar: ")

    # Verifica se o produto existe e se há estoque
    if produto_vendido in procedimentos:
        quantidade = int(input(f"Digite a quantidade de {produto_vendido} que deseja comprar: "))
        if procedimentos[produto_vendido]["estoque"] >= quantidade:
            valor_venda = quantidade * procedimentos[produto_vendido]["preço"]
            procedimentos[produto_vendido]["estoque"] -= quantidade
            total_vendas += valor_venda
            print(f"Venda realizada: {quantidade}x {produto_vendido} - Total: R${valor_venda:.2f}\n")
        else:
            print("Quantidade em estoque insuficiente.\n")
    else:
        print("Produto não encontrado.\n")

# Função para exibir o total das vendas
def exibir_vendas():
    print(f"\nTotal de vendas realizadas: R${total_vendas:.2f}\n")

# Função para aplicar uma promoção
def sortear_promocao():
    produto_sorteado = random.choice(list(procedimentos.keys()))
    desconto = random.randint(10, 50)  # Desconto entre 10% e 50%
    procedimentos[produto_sorteado]["preço"] *= (1 - desconto / 100)
    print(f"\nPromoção! O produto {produto_sorteado} está com {desconto}% de desconto!\n")

def cadastro_Cliente():
    name= input("Digite seu nome")
    email=input("Digite seu email")
    telefone=int(input("digite seu telefone com DDD"))
    print(f"Produto {nome} cadastrado com sucesso!\n")

def menu():
    print("1- Cadastrar Cliente ") 
    print("2- Lista de procedimentos")
    print("3- Escolher procedimento ")
    print("4- Realizar venda")
    print("5- Exibir total de vendas")
    print("6- Total de compras")
    print("7- sair")


opcao= input("Digite uma opção")





