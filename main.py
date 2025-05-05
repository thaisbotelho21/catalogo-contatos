# Lista para armazenar os contatos
agenda = []

# Função para adicionar um novo contato
def adicionar_contato():
    nome = input("Nome: ")
    endereco = input("Endereço: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    
    contato = {
        "nome": nome,
        "endereco": endereco,
        "telefone": telefone,
        "email": email
    }
    agenda.append(contato)
    print("Contato adicionado com sucesso!\n")

# Função para listar todos os contatos
def listar_contatos():
    if not agenda:
        print("Nenhum contato na agenda.\n")
        return
    
    print("Contatos Salvos:")
    for i, contato in enumerate(agenda, start=1):
        print(f"\nContato {i}:")
        for chave, valor in contato.items():
            print(f"{chave.capitalize()}: {valor}")
    print()

# Função para editar um contato
def editar_contato():
    listar_contatos()
    try:
        indice = int(input("Digite o número do contato que deseja editar: ")) - 1
        if 0 <= indice < len(agenda):
            print("Deixe em branco caso não queira alterar o campo.")
            nome = input("Novo nome: ") or agenda[indice]["nome"]
            endereco = input("Novo endereço: ") or agenda[indice]["endereco"]
            telefone = input("Novo telefone: ") or agenda[indice]["telefone"]
            email = input("Novo email: ") or agenda[indice]["email"]

            agenda[indice] = {
                "nome": nome,
                "endereco": endereco,
                "telefone": telefone,
                "email": email
            }
            print("Contato atualizado com sucesso!\n")
        else:
            print("Contato não encontrado.\n")
    except ValueError:
        print("Entrada inválida. Use um número.\n")

# Função para excluir um contato
def excluir_contato():
    listar_contatos()
    try:
        indice = int(input("Digite o número do contato que deseja excluir: ")) - 1
        if 0 <= indice < len(agenda):
            agenda.pop(indice)
            print("Contato excluído com sucesso!\n")
        else:
            print("Contato não encontrado.\n")
    except ValueError:
        print("Entrada inválida. Use um número.\n")

# Menu principal
def menu():
    while True:
        print("Agenda de Contatos")
        print("1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Editar Contato")
        print("4. Excluir Contato")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_contato()
        elif opcao == "2":
            listar_contatos()
        elif opcao == "3":
            editar_contato()
        elif opcao == "4":
            excluir_contato()
        elif opcao == "5":
            print("Saindo da agenda...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Iniciar o programa
menu()
