class jogo:
    def __init__(self, nome, plataforma, preco, quantidade):
        self.nome = nome
        self.plataforma = plataforma
        self.preco = preco
        self.quantidade = quantidade
class estoque:
    def __init__(self):
        self.lista_jogos = []
    def listar(self):
        if len(self.lista_jogos) == 0:
            print("O estoque está vazio.")
        else:
            for jogo in self.lista_jogos:
                print(f"Nome: {jogo.nome} | Preço: R${jogo.preco:.2f} | Estoque: {jogo.quantidade}")
    def adicionar(self):
        #Nome do jogo
        lista_plataformas = ["xbox", "pc", "ps5", "switch"]
        nome = input("Digite o nome do jogo: ")
        print(f"Nome do jogo: {nome}\n")
        #Plataforma
        plataforma = ""
        while plataforma not in lista_plataformas:
            plataforma = input("Digite a plataforma do jogo: ").lower()
            if plataforma not in lista_plataformas:
                print("Plataforma Indisponivel!\nAs plataformas disponiveis são:\n-Xbox\n-PC\n-PS5\n-Switch\nDigite uma das 4!")
        formatar_nomes = {"xbox": "Xbox", "pc": "PC", "ps5": "PS5", "switch": "Switch"}
        plataforma = formatar_nomes[plataforma]
        print(f"Plataforma: {plataforma}\n")
        #Preço do jogo
        while True:
            try:
                preco = float(input("Digite o preço do jogo: "))
                break
            except ValueError:
                    print("Erro: Digite um valor numérico válido!")
        print(f"Preço do jogo: R${preco:.2f}\n")
        #Quantidade
        while True:
            try:
                quantidade = int(input("Digite a quantidade: "))
                break
            except ValueError:
                    print("Erro: Digite um valor numérico inteiro válido!")
        print(f"Quantidade disponível no estoque: {quantidade}\n")
        print("Jogo cadastrado.")

        novo_jogo = jogo(nome, plataforma, preco, quantidade)
        self.lista_jogos.append(novo_jogo)
    def atualizar_estoque(self):
        while True:
            try:
                modificar_quantidade = int(input("Digite quantas unidades vai comprar ou vender (digite valor negativo se quiser vender): "))
                break
            except ValueError:
                print("Erro: Digite um valor numérico inteiro válido!")
        while True:
            try:
                opcao = int(input("Digite o número da linha do seu jogo(A primeira linha começa pelo 0!): "))
                if opcao >= len(self.lista_jogos) or opcao < 0:
                    print("Digite uma opção válida!")
                else:
                    break
            except ValueError:
                print("Erro: Digite um valor numérico inteiro válido!")
        self.lista_jogos[opcao].quantidade += modificar_quantidade
        print(f"Estoque atualizado com sucesso!\n")
    def remover(self):
        while True:
            try:
                linha = int(input("Digite o numero da linha que deseja remover(Começando do 0): "))
                self.lista_jogos.pop(linha)
                break
            except ValueError:
                print("Erro: Digite um valor numérico inteiro válido!")
            except IndexError:
                print(f"Erro: Digite o numero de uma lista existente! (Escolha entre 0 e {len(self.lista_jogos)-1})")
meu_estoque = estoque()
while True:
    print("\n=== 🎮 GAME STORE MANAGEMENT ===")
    print("1. Cadastrar Novo Jogo")
    print("2. Listar Estoque")
    print("3. Atualizar Quantidade")
    print("4. Remover Jogo")
    print("5. Sair do Programa")
    print("================================")

    opcao = input("Escolha uma opção (1-5): ")

    if opcao == "1":
        meu_estoque.adicionar()
    if opcao == "2":
        meu_estoque.listar()
    if opcao == "3":
        meu_estoque.atualizar_estoque()
    if opcao == "4":
        meu_estoque.remover()
    if opcao == "5":
        print("Até breve!")
        break