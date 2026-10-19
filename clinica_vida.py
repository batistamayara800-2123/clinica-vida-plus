# Clínica Vida+ — programa acadêmico demonstrativo
# Execute com: python clinica_vida.py
# Os dados são mantidos apenas na memória enquanto o programa está aberto.

def ler_nome(mensagem="Nome: "):
    while True:
        nome = input(mensagem).strip()
        if nome:
            return nome
        print("O nome não pode ficar vazio. Tente novamente.")


def ler_idade():
    while True:
        entrada = input("Idade: ").strip()
        try:
            idade = int(entrada)
            if 0 <= idade <= 120:
                return idade
            print("Informe uma idade entre 0 e 120.")
        except ValueError:
            print("Idade inválida. Digite um número inteiro.")


def ler_telefone():
    while True:
        telefone = input("Telefone: ").strip()
        if telefone:
            return telefone
        print("O telefone não pode ficar vazio. Tente novamente.")


def cadastrar_paciente(pacientes):
    print("\n--- Cadastro de paciente ---")
    paciente = {
        "nome": ler_nome("Nome: "),
        "idade": ler_idade(),
        "telefone": ler_telefone(),
    }
    pacientes.append(paciente)
    print(f"Paciente {paciente['nome']} cadastrado com sucesso.")


def ver_estatisticas(pacientes):
    print("\n--- Estatísticas ---")
    if not pacientes:
        print("Ainda não há pacientes cadastrados.")
        return
    total = len(pacientes)
    media = sum(p["idade"] for p in pacientes) / total
    mais_novo = min(pacientes, key=lambda p: p["idade"])
    mais_velho = max(pacientes, key=lambda p: p["idade"])
    print(f"Total cadastrado: {total}")
    print(f"Idade média: {media:.1f} anos")
    print(f"Paciente mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")
    print(f"Paciente mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)")


def buscar_paciente(pacientes):
    print("\n--- Buscar paciente ---")
    if not pacientes:
        print("Ainda não há pacientes cadastrados.")
        return
    termo = input("Digite o nome (ou parte do nome): ").strip().casefold()
    if not termo:
        print("A busca não pode ficar vazia.")
        return
    encontrados = [p for p in pacientes if termo in p["nome"].casefold()]
    if not encontrados:
        print("Nenhum paciente encontrado com esse nome.")
        return
    for paciente in encontrados:
        mostrar_paciente(paciente)


def mostrar_paciente(paciente):
    print(f"Nome: {paciente['nome']} | Idade: {paciente['idade']} | Telefone: {paciente['telefone']}")


def listar_pacientes(pacientes):
    print("\n--- Lista de pacientes ---")
    if not pacientes:
        print("Ainda não há pacientes cadastrados.")
        return
    for numero, paciente in enumerate(pacientes, start=1):
        print(f"{numero}. ", end="")
        mostrar_paciente(paciente)


def main():
    pacientes = []
    while True:
        print("\n" + "=" * 28)
        print("       CLÍNICA VIDA+")
        print("=" * 28)
        print("1. Cadastrar paciente")
        print("2. Ver estatísticas")
        print("3. Buscar paciente pelo nome")
        print("4. Listar todos os pacientes")
        print("5. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_paciente(pacientes)
        elif opcao == "2":
            ver_estatisticas(pacientes)
        elif opcao == "3":
            buscar_paciente(pacientes)
        elif opcao == "4":
            listar_pacientes(pacientes)
        elif opcao == "5":
            print("Programa encerrado. Obrigado por utilizar o Clínica Vida+!")
            break
        else:
            print("Opção inválida. Digite um número de 1 a 5.")


if __name__ == "__main__":
    main()
