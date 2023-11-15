#Programa desenvolvido na linguagem Python
#Desevolvido por Marcio Almeida de Souza
#Desenvolvido a partir de novembro de 2023
#Objetivo: estudo
#marciosouzagcm@gmail.com

#foi importado função para tranformar ano de nascimento em idade
from datetime import datetime

#lista para armazenar os dados pessoais
dados_pessoais =[]

#lista pessoa para tratar de dados sensiveis com base na LGPD
pessoa = []

while True:
    #solicitação dos dados pessoais
    pessoa = {
        "nome": input("Informe seu nome, sobrenome: "),
        "data_nascimento": int(input("Informe seu ano de nascimento: ")),
        "idade": 0,
        "sexo": input("Informe seu sexo [M/F]: "),
        "endereco": input("Informe seu endereço, numeral, complemento, bairro, Município, Estado, CEP: "),
        "tempo_de_contribuicao": int(input("Informe quanto de contribuição no INSS você tem (anos): ")),
        "email": input("Informe seu email: "),
        #criterios para solicitar aposentadoria em 2023 são aproximadamente 25 criterios e ser descritos durante o desenvolvimento deste projeto
        "tipo_de_aposentadoria": input("Informe o critério a ser pesquisado para aposentadoria: 1. idade, 2. tempo de contribuição, 3. idade + tempo de contribuição, 4. aposentadoria especial. Resp.: ")
    }
    #função que transforma ano de nascimento em idade
    pessoa["idade"] = datetime.now().year - pessoa["data_nascimento"]

    #condicionais para criterio 1 =(idade, sexo, tempo de contribuição), caso cumpra os requisitos estará habilitado a solicitar aposentadoria
    if pessoa["tipo_de_aposentadoria"] == "1" and pessoa["sexo"] == "M" and pessoa["idade"] >= 65 and pessoa["tempo_de_contribuicao"] >= 15:
        print("HABILITADO A SOLICITAR APOSENTADORIA")
    elif pessoa["tipo_de_aposentadoria"] == "1" and pessoa["sexo"] == "F" and pessoa["idade"] >= 60 and pessoa["tempo_de_contribuicao"] >= 15:
        print("HABILITADA A SOLICITAR APOSENTADORIA")
    else:
        print("VOCÊ NÃO ESTÁ HABILITADO A SOLICITAR APOSENTADORIA")
    #deseja cadastrar outra pessoa
    resposta = input('DESEJA CADASTRAR OS DADOS DE OUTRA PESSOA? [S/N]? ')
    if resposta.upper() == "N":
        break
#impressão dos dados digitados
print ([pessoa])