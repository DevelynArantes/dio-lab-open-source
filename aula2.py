primeira_pergunta = int (input ("Qual é a sua idade? "))
segunda_pergunta = input("Você está com autorização dos pais? (sim/não): ")

maior_de_idade = True if primeira_pergunta >= 18 else False
autorizacao = False if segunda_pergunta == 'nao' else True

if maior_de_idade is True and autorizacao is False:
    print("Entrada permitida")

elif not maior_de_idade and not autorizacao:
    print("Entrada negada. Volte com autorização!")

elif not maior_de_idade and autorizacao:
    print("Entrada permitida com autorização dos pais.")