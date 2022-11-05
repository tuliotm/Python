# Exercício em sala, lita de cadastros

def listas_cadastros(database):
  if len(database) == 0:
    print("Não existem cadastros")

  else:
    for i in database.keys():
        s = f"Código: {i} |" \
            f"Nome: {database[i]['nome']} |" \
            f"Email: {database[i]['email']} |" \
            f"Data: {database[i]['data']}"
        print(s)

database = {}

# While interativo
while True:
  opcao = int(input(
    "1 - Cadastrar uma pessoa\n"
    "2 - Listar os cadastros\n"
    "3 - Deletar um cadsatro\n"
    "4 - Alterar um cadastro\n"
    "0 - Sair do cadastro\n"
    "Digite sua opção: "
  ))

  if opcao == 1:
     codigo = int(input("Digite o código: "))
     nome = input("Digite o nome: ")
     email = input("Digite o email: ")
     data = input("Digite o dia/mês do nascimento: ")

     database[codigo] = {"nome": nome, "email": email, "data": data}

  elif opcao == 2:
    print("--- LISTAGEM DE CADASTROS ---")
    listas_cadastros(database)

  elif opcao == 3:
    print("--- Selecione o item a ser deletado ---")
    listas_cadastros(database)
    codigo = int(input("Digite o codigo a ser deletado: "))

    del database[codigo]

  elif opcao == 4:
        print("--- Selecione o item a ser alterado ---")
        listas_cadastros(database)
        codigo = int(input("Digite o codigo a ser alterado: "))
        op = int(input("1 - Nome\n"
                       "2 - Email\n"
                       "3 - Data\n"
                       "O que você deseja alterar?: "))
        if op == 1:
            nome = input("Digite o novo nome: ")
            database[codigo]['nome'] = nome
        if op == 2:
            email = input("Digite o novo email: ")
            database[codigo]['email'] = email
        if op == 3:
            data = input("Digite a nova data: ")
            database[codigo]['data'] = data
  elif opcao == 0:
        break
