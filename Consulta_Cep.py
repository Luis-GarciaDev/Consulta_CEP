import requests
import os
import time as tm

escolha = int(input("""
ESCOLHA A FORMA DE PESQUISA:
1. POR NOME:
2. POR CEP:

Escolha: """))
url = " "

match escolha:
    case 1:
        estado = input("Digite o Estado: ")
        cidade = input("Digite a Cidade: ")
        nome_rua = input("Digite o nome da rua: ")
        url = requests.get(f"https://viacep.com.br/ws/{estado}/{cidade}/{nome_rua}/json/")
    case 2:
        cep = input("Digite o cep: ")
        url = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

tm.sleep(1)
tm.sleep(1)

"QUAIS ALTERAÇÕES FAZER ANTES DO COMMIT: "
#1- COLOQUE UMA MENSAGEM DE STATUS DE CONEXÃO COM BASE NO CÓDIGO RECEBIDO
#2- COLOQUE TM.SLEEP PARA ALGUNS PONTOS DO CÓDIGO
#3- COLOQUE O OS.SYSTEM("CLS") PARA LIMPAR A TELA

status = url.status_code

        

tm.sleep(1)
tm.sleep(1)
os.system("cls")
print("Status: ",url.status_code)
tm.sleep(1)
tm.sleep(1)
tm.sleep(1)
os.system("cls")

match status:
    case s if 200 <= s < 300:
        print("Conexão estabelecida com sucesso")
    case s if 300 <= s < 400:
        print("Redirecionado")
    case s if 400 <= s < 500:
        print("Erro usuário")
    case s if 500 <= s:
        print("Erro Servidor")
tm.sleep(1)
tm.sleep(1)
tm.sleep(1)
os.system("cls")
tm.sleep(1)
tm.sleep(1)
tm.sleep(1)

print(url.json())

print("\n\n")
