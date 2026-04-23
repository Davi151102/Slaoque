import datetime

# --- BANCO DE DADOS SIMULADO ---
barbearias = {
    1: {"nome": "Barbearia do Dev", "ativa": True},
    2: {"nome": "Corte & Código", "ativa": True}
}

barbeiros = {
    101: {"nome": "Lucas", "id_barbearia": 1},
    102: {"nome": "Mateus", "id_barbearia": 1},
    201: {"nome": "Tiago", "id_barbearia": 2}
}

agendamentos = []

# --- FUNÇÕES DO SISTEMA ---

def listar_barbeiros(id_barbearia):
    return [f"ID: {id} - Nome: {dados['nome']}" for id, dados in barbeiros.items() if dados['id_barbearia'] == id_barbearia]

def criar_agendamento(id_barbearia, nome_cliente, id_barbeiro, data_hora):
    # Valida se a barbearia existe
    if id_barbearia not in barbearias:
        return "❌ Erro: Barbearia não encontrada."

    # Valida se o barbeiro pertence à barbearia selecionada
    if id_barbeiro not in barbeiros or barbeiros[id_barbeiro]['id_barbearia'] != id_barbearia:
        return "❌ Erro: Este barbeiro não trabalha nesta unidade."

    # Verificar conflito de horário
    for ag in agendamentos:
        if ag['id_barbeiro'] == id_barbeiro and ag['data_hora'] == data_hora:
            return f"❌ Erro: O barbeiro {barbeiros[id_barbeiro]['nome']} já está ocupado às {data_hora}."

    # Registrar agendamento
    novo_corte = {
        "barbearia": barbearias[id_barbearia]['nome'],
        "cliente": nome_cliente,
        "id_barbeiro": id_barbeiro,
        "barbeiro_nome": barbeiros[id_barbeiro]['nome'],
        "data_hora": data_hora
    }
    agendamentos.append(novo_corte)
    return f"✅ Sucesso: Horário marcado para {nome_cliente} com {barbeiros[id_barbeiro]['nome']}!"

# --- MENU INTERATIVO PARA TESTE ---

def executar_app():
    while True:
        print(f"\n{'='*30}")
        print("SISTEMA BARBER SaaS v1.0")
        print(f"{'='*30}")
        print("1. Ver Barbeiros Disponíveis")
        print("2. Marcar Novo Horário")
        print("3. Ver Agenda Completa")
        print("0. Sair")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            print("\nBarbeiros na unidade 1:")
            for b in listar_barbeiros(1): print(b)
        
        elif opcao == "2":
            nome = input("Nome do Cliente: ")
            id_b = int(input("ID do Barbeiro (ex: 101): "))
            hora = input("Hora (ex: 14:00): ")
            resultado = criar_agendamento(1, nome, id_b, hora)
            print(resultado)

        elif opcao == "3":
            print("\n--- AGENDA DO DIA ---")
            if not agendamentos: print("Nenhum horário marcado.")
            for ag in agendamentos:
                print(f"{ag['data_hora']} | {ag['barbeiro_nome']} -> Cliente: {ag['cliente']}")
        
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    executar_app()
      
