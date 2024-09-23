import random

class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, nome, telefone):
        contato = Contato(nome, telefone)
        self.contatos.append(contato)
        frases = [
            f"Contato {nome} adicionado! Agora você tem mais um número para esquecer!",
            f"{nome} está na lista! Não se esqueça de ligar de vez em quando!",
            f"{nome} adicionado com sucesso! Quem sabe um dia vocês se falam!",
        ]
        print(random.choice(frases))

    def remover_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.remove(contato)
                frases = [
                    f"Contato {nome} removido! Esperamos que não tenha sido por um motivo ruim!",
                    f"Contato {nome} foi removido! Menos um número para lembrar!",
                    f"Contato {nome} saiu da lista! Talvez ele(a) volte um dia!",
                ]
                print(random.choice(frases))
                return
        print(f"Contato {nome} não encontrado. Talvez ele(a) já tenha se removido sozinho(a)!")

    def listar_contatos(self):
        if not self.contatos:
            print("Nenhum contato na agenda. Parece que você é um(a) lobo(a) solitário(a)!")
        else:
            for contato in self.contatos:
                print(f"Nome: {contato.nome}, Telefone: {contato.telefone}")

def menu():
    agenda = Agenda()
    while True:
        print("\n1. Adicionar Contato")
        print("2. Remover Contato")
        print("3. Listar Contatos")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            agenda.adicionar_contato(nome, telefone)
        elif opcao == '2':
            nome = input("Digite o nome do contato a ser removido: ")
            agenda.remover_contato(nome)
        elif opcao == '3':
            agenda.listar_contatos()
        elif opcao == '4':
            print("Saindo da agenda... Até a próxima!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()

