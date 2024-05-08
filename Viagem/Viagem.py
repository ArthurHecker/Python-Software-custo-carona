import os

#Criar as funções de acesso ao bando de dados
file_path = os.path.abspath(r"D:\Users\Crino\Programs\Viagem\BancoDeDados.txt")

with open(file_path, "r") as f:
    linhas = f.readlines()
    anoAtual = int(linhas[0].strip())
    precoGasolina = float(linhas[1].strip())

def adicionar_info(info):
    with open(file_path, "a") as f:
        f.write(info + "\n")

def acessar_info():
    with open(file_path, "r") as f:
        info = f.readlines()
    return info

def menu():
    print("\n")
    print("        SOFTWARE DE CONTAGEM DE PREÇOS DE PASSAGENS       \n")
    print("Você gostaria de acessar as informações de preços, deseja registrar uma nova informação de preço, ou deseja alterar uma informação existente?\n")
    print("(1) Acessar as informações de preços.\n")
    print("(2) Registrar uma nova informação de preço.\n")
    print("(3) Alterar uma informação existente.\n")
    print("(4) Sair.\n")

def acao1():
# bloco de código para acessar as informações de preços
    print("\n")
    print("A primeira linha representa o ano inicial do curso\n")
    print("A segunda linha representa o preço diário da ida e volta\n")
    print("As linhas seguintes representa o histórico de informações registradas no banco de informações\n")
    print("\n")
    informacoes = acessar_info()
    for info in informacoes:
        print(info.strip())

def acao2():
# bloco de código para registrar uma nova informação de preço
    # Receptor de ano
    i = 0
    print("\n")
    print("Qual o ano que deseja registrar uma nova informação de preço?\n")
    print("Escreva um número de 1 a 5.\n")
    ano = int(input("Esteja ciente que o ano 1 representa o ano inicial do curso e, o 5 é o ano máximo da conclusão da curso:\n"))
    inf = ""
    # Evitar que o usuario escreva algo que não seja números
    while i == 0:
        try:
            # Quando for números
            if ano < 1 or ano > 5:
                while ano < 1 or ano > 5:
                    ano = 0
                    print("\n")
                    print("\nEsse ano é inválido.\n")
                    print("Qual o ano que deseja registrar uma nova informação de preço?\n")
                    print("Escreva um número de 1 a 5.\n")
                    ano = int(input("Esteja ciente que o ano 1 representa o ano inicial do curso e, o 5 é o ano máximo da conclusão da curso:\n"))
            else:
                ano += anoAtual-1    
                i = 1
        # Quando não for números.
        except ValueError:
            print("\nDigite apenas números.")

    # Receptor de mês        
    i = 0
    print("Qual o número do mês que deseja registrar uma nova informação de preço?\n")
    mes = int(input("Por exemplo: Janeiro = 1, Fevereiro = 2, Março = 3.\n"))
    # Evitar que o usuario escreva algo que não seja números
    while i == 0:
        try:
            # Quando for números
            if mes < 1 or mes > 12:
                while mes < 1 or mes > 12:
                    mes = 0
                    print("\nEsse mês é inválido.\n")
                    print("Qual o número do mês que deseja registrar uma nova informação de preço?\n")
                    mes = int(input("Por exemplo: Janeiro = 1, Fevereiro = 2, Março = 3.\n"))
            else:    
                i = 1
        # Quando não for números
        except ValueError:
            print("\nDigite apenas números.")

    # Quantos dias de viagem foram realizados no mês
    i = 0
    dias = int(input("Quantos dias foram realizadas as aulas presencialmente?\n"))
    while i ==0:
        try:
            # Quando for números
            precoPorDia = precoGasolina * 1.523297491
            precoDoMes = dias*precoPorDia
            precoterco = precoDoMes / 3
            precoArthur = float(precoterco + (precoDoMes * 1.075) - precoDoMes)
            precoGuilherme = float(precoterco + (precoDoMes * 1.2336) - precoDoMes)
            print("\n")
            print("\n")
            print("O PREÇO TOTAL DO MÊS É {:.2f} REAIS, O PREÇO A SER PAGO PELO ARTHUR É {:.2f} REAIS E O PREÇO A SER PAGO PELO GUILHERME É {:.2f} REAIS.".format(precoDoMes, precoArthur, precoGuilherme))
            print("\n")
            print("\n")

            # Registrar no banco de dados
            inf += f"Data:{mes:02}/{ano} | Preco Total:{precoDoMes:.2f}, Preco Arthur:{precoArthur:.2f}, Preco Guilherme:{precoGuilherme:.2f}"
            adicionar_info(inf)
            i = 1

        # Quando não for números
        except ValueError:
            print("\nDigite apenas números.")
       
def acao3():
#Bloco para alteração de ano e preço da quilometragem por litro
    with open(file_path, "r+") as f:
        # Ler as informações atuais
        info = f.readlines()
        # Ir para o começo do arquivo
        f.seek(0)
        # Perguntar ao usuário para atualizar o ano
        anoAtual = input("Digite o novo ano: ")
        # Escrever o novo ano no arquivo
        f.write(anoAtual + "\n")
        # Perguntar ao usuário para atualizar o preço do combustível
        preco = input("Digite o novo preço da gasolina: ")
        # Escrever o novo preço do combustível no arquivo
        f.write(preco + "\n")
        # Escrever as informações restantes no arquivo
        for linha in info[2:]:
            f.write(linha)

#Printar ações do usuário
acao = 0
while True:
    menu()
    #Evitar que o usuario escreva algo que não seja números
    try:
    #Quando for números.
        acao = int(input("Digite o número correspondente da ação que deseja realizar: \n"))
        if acao < 1 or acao > 4:
            print("\nEssa ação é inválida.")

        elif acao == 1:
            acao1()

        elif acao == 2:
            acao2()

        elif acao == 3:
            acao3()

        else:
            # opção de sair: interrompe o loop e finaliza o programa
            break

    #Quando não for números
    except ValueError:
        print("\nDigite apenas números.")
