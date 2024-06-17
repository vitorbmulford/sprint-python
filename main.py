import os

def limpar_terminal():
    """
    Limpa o terminal de acordo com o sistema operacional.
    """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def criar_lista_de_carros():
    """
    Cria e retorna uma lista de carros de Fórmula E com suas características.
    """
    lista_carros = [
        {
            "Modelo": "Nissan IM01",
            "Velocidade Máxima": "280 km/h",
            "Autonomia": "45 min",
        },
        {
            "Modelo": "Audi e-tron FE07",
            "Velocidade Máxima": "270 km/h",
            "Autonomia": "40 min",
        },
        {
            "Modelo": "Jaguar I-TYPE 5",
            "Velocidade Máxima": "285 km/h",
            "Autonomia": "42 min",
        },
        {
            "Modelo": "BMW iFE.21",
            "Velocidade Máxima": "275 km/h",
            "Autonomia": "43 min",
        },
        {
            "Modelo": "Mahindra M7Electro",
            "Velocidade Máxima": "280 km/h",
            "Autonomia": "44 min",
        },
    ]
    return lista_carros


def criar_lista_de_pilotos():
    """
    Cria e retorna uma lista de pilotos de Fórmula E com seus detalhes.
    """
    lista_pilotos = [
        {
            "Nome": "Lucas di Grassi",
            "Equipe": "Rokit Venturi Racing",
            "Nacionalidade": "Brasileiro",
            "Idade": 38,
            "Peso": "75 kg",
            "Altura": "1.79 m",
            "Vitórias": 12,
            "Pódios": 33,
            "Títulos": 1,
        },
        {
            "Nome": "Jean-Éric Vergne",
            "Equipe": "DS Techeetah",
            "Nacionalidade": "Francês",
            "Idade": 33,
            "Peso": "70 kg",
            "Altura": "1.78 m",
            "Vitórias": 10,
            "Pódios": 26,
            "Títulos": 2,
        },
        {
            "Nome": "Stoffel Vandoorne",
            "Equipe": "Mercedes-EQ",
            "Nacionalidade": "Belga",
            "Idade": 31,
            "Peso": "68 kg",
            "Altura": "1.77 m",
            "Vitórias": 6,
            "Pódios": 15,
            "Títulos": 1,
        },
        {
            "Nome": "Antonio Felix da Costa",
            "Equipe": "DS Techeetah",
            "Nacionalidade": "Português",
            "Idade": 32,
            "Peso": "66 kg",
            "Altura": "1.75 m",
            "Vitórias": 7,
            "Pódios": 18,
            "Títulos": 1,
        },
        {
            "Nome": "Alex Lynn",
            "Equipe": "Mahindra Racing",
            "Nacionalidade": "Britânico",
            "Idade": 30,
            "Peso": "72 kg",
            "Altura": "1.80 m",
            "Vitórias": 2,
            "Pódios": 6,
            "Títulos": 0,
        },
        {
            "Nome": "Alexander Sims",
            "Equipe": "Mahindra Racing",
            "Nacionalidade": "Britânico",
            "Idade": 35,
            "Peso": "74 kg",
            "Altura": "1.82 m",
            "Vitórias": 1,
            "Pódios": 5,
            "Títulos": 0,
        },
    ]
    return lista_pilotos


def obter_estatisticas():
    """
    Retorna as estatísticas da temporada atual.
    """
    estatisticas = {
        "Corridas Realizadas": 12,
        "Corridas Restantes": 8,
        "Líder do Campeonato": "Stoffel Vandoorne",
        "Equipe Líder": "Mercedes-EQ",
        "Vitórias do Líder": 5,
        "Total de Equipes": 11,
        "Total de Pilotos": 22,
    }
    return estatisticas


def obter_noticias():
    """
    Retorna uma lista de notícias recentes da Fórmula E.
    """
    noticias = [
        "Stoffel Vandoorne vence a última corrida em Roma! A corrida foi emocionante do início ao fim, com Vandoorne da Mercedes-EQ mostrando habilidade e estratégia para vencer seus competidores. Ele agora lidera o campeonato com uma vantagem confortável.",
        "Mercedes-EQ lidera o campeonato de equipes com folga. A equipe tem mostrado consistência e desempenho excepcionais em todas as corridas da temporada. A equipe Mahindra Racing também tem se destacado com seus pilotos Alex Lynn e Alexander Sims, que estão constantemente entre os top 10.",
        "Lucas di Grassi sofre acidente, mas passa bem. Durante a corrida em Roma, di Grassi teve um acidente sério, mas felizmente saiu ileso. Ele agradeceu à equipe médica e prometeu voltar mais forte para as próximas corridas.",
        "Jean-Éric Vergne e Antonio Felix da Costa disputam acirradamente o segundo lugar. Os pilotos da DS Techeetah estão em uma disputa intensa, tornando cada corrida mais emocionante. A equipe Mahindra Racing também está em busca de melhores posições na tabela, com Alex Lynn e Alexander Sims mostrando grande potencial.",
        "Próxima corrida será em Berlim, expectativa alta! As equipes estão se preparando para a corrida em Berlim, onde a Mahindra Racing espera conquistar um pódio com seus talentosos pilotos. A expectativa é alta para uma corrida emocionante em uma das pistas mais desafiadoras do calendário.",
    ]
    return noticias


def obter_eventos_disponiveis():
    """
    Retorna uma lista de eventos disponíveis para agendamento.
    """
    eventos = [
        {"Nome": "E-Prix de Berlim", "Data": "15/06/2024", "Local": "Berlim, Alemanha"},
        {
            "Nome": "E-Prix de Nova Iorque",
            "Data": "29/06/2024",
            "Local": "Nova Iorque, EUA",
        },
        {
            "Nome": "E-Prix de Londres",
            "Data": "13/07/2024",
            "Local": "Londres, Reino Unido",
        },
        {
            "Nome": "E-Prix de Seul",
            "Data": "27/07/2024",
            "Local": "Seul, Coreia do Sul",
        },
    ]
    return eventos


def menu():
    """
    Exibe o menu principal e solicita a opção do usuário.
    """
    limpar_terminal()
    print("MENU PRINCIPAL")
    print("=" * 50)
    print("1 - Ver lista de carros disponíveis")
    print("2 - Ver detalhes dos pilotos")
    print("3 - Ver estatísticas da temporada")
    print("4 - Ver últimas notícias")
    print("5 - Agendar evento de corrida")
    print("6 - Experiência Interativa")
    print("7 - Sair")
    print("=" * 50)
    opcao = int(input("Escolha uma opção: "))
    return opcao


def exibir_lista_de_carros(lista_carros):
    """
    Exibe a lista de carros disponíveis.
    """
    limpar_terminal()
    print("CARROS DISPONÍVEIS")
    print("=" * 50)
    for i, carro in enumerate(lista_carros, 1):
        print(f"{i}. Modelo: {carro['Modelo']}")
        print(f"   Velocidade Máxima: {carro['Velocidade Máxima']}")
        print(f"   Autonomia: {carro['Autonomia']}")
        print("-" * 50)
    input("Pressione Enter para continuar...")


def exibir_lista_de_pilotos(lista_pilotos):
    """
    Exibe a lista de pilotos e seus detalhes.
    """
    limpar_terminal()
    print("PILOTOS")
    print("=" * 50)
    for i, piloto in enumerate(lista_pilotos, 1):
        print(f"{i}. Nome: {piloto['Nome']}")
        print(f"   Equipe: {piloto['Equipe']}")
        print(f"   Nacionalidade: {piloto['Nacionalidade']}")
        print(f"   Idade: {piloto['Idade']} anos")
        print(f"   Peso: {piloto['Peso']}")
        print(f"   Altura: {piloto['Altura']}")
        print(f"   Vitórias: {piloto['Vitórias']}")
        print(f"   Pódios: {piloto['Pódios']}")
        print(f"   Títulos: {piloto['Títulos']}")
        print("-" * 50)
    input("Pressione Enter para continuar...")


def exibir_estatisticas(estatisticas):
    """
    Exibe as estatísticas da temporada atual.
    """
    limpar_terminal()
    print("ESTATÍSTICAS DA TEMPORADA")
    print("=" * 50)
    for chave, valor in estatisticas.items():
        print(f"{chave}: {valor}")
    print("=" * 50)
    input("Pressione Enter para continuar...")


def exibir_noticias(noticias):
    """
    Exibe as últimas notícias da Fórmula E.
    """
    limpar_terminal()
    print("ÚLTIMAS NOTÍCIAS")
    print("=" * 50)
    for noticia in noticias:
        print(f"- {noticia}")
        print("-" * 50)
    input("Pressione Enter para continuar...")


def agendar_evento(eventos):
    """
    Permite ao usuário agendar um evento de corrida, selecionando um evento disponível.
    """
    limpar_terminal()
    print("AGENDAR EVENTO DE CORRIDA")
    print("=" * 50)
    print("Eventos disponíveis:")
    for i, evento in enumerate(eventos, 1):
        print(
            f"{i}. {evento['Nome']} - Data: {evento['Data']} - Local: {evento['Local']}"
        )
    print("=" * 50)
    opcao = int(input("Escolha um evento para agendar: "))

    if 1 <= opcao <= len(eventos):
        evento_escolhido = eventos[opcao - 1]
        print("\nEvento agendado com sucesso!")
        print("=" * 50)
        print(f"Evento: {evento_escolhido['Nome']}")
        print(f"Data: {evento_escolhido['Data']}")
        print(f"Local: {evento_escolhido['Local']}")
        print("=" * 50)
    else:
        print("Opção inválida. Nenhum evento foi agendado.")
    input("Pressione Enter para continuar...")


def experiencia_interativa():
    """
    Exibe a seção de Experiência Interativa com um quiz de conhecimento sobre Fórmula E.
    """
    limpar_terminal()
    print("EXPERIÊNCIA INTERATIVA")
    print("=" * 50)
    print("Bem-vindo ao quiz de conhecimento sobre Fórmula E!")
    print("Responda às perguntas abaixo e teste seus conhecimentos.")
    print("=" * 50)

    perguntas = [
        {
            "pergunta": "Qual é a equipe que lidera o campeonato de equipes em 2024?",
            "opcoes": [
                "Mercedes-EQ",
                "DS Techeetah",
                "Mahindra Racing",
                "Rokit Venturi Racing",
            ],
            "resposta": "Mercedes-EQ",
        },
        {
            "pergunta": "Quem é o líder do campeonato de pilotos em 2024?",
            "opcoes": [
                "Lucas di Grassi",
                "Jean-Éric Vergne",
                "Stoffel Vandoorne",
                "Antonio Felix da Costa",
            ],
            "resposta": "Stoffel Vandoorne",
        },
        {
            "pergunta": "Qual a velocidade máxima do carro Nissan IM01?",
            "opcoes": ["270 km/h", "280 km/h", "275 km/h", "285 km/h"],
            "resposta": "280 km/h",
        },
        {
            "pergunta": "Qual equipe tem os pilotos Alex Lynn e Alexander Sims?",
            "opcoes": [
                "Mahindra Racing",
                "Mercedes-EQ",
                "Jaguar Racing",
                "Audi Sport ABT",
            ],
            "resposta": "Mahindra Racing",
        },
        {
            "pergunta": "Em qual cidade será a próxima corrida da Fórmula E?",
            "opcoes": ["Berlim", "Nova Iorque", "Londres", "Seul"],
            "resposta": "Berlim",
        },
    ]

    pontuacao = 0
    for i, questao in enumerate(perguntas, 1):
        print(f"{i}. {questao['pergunta']}")
        for j, opcao in enumerate(questao["opcoes"], 1):
            print(f"   {j}. {opcao}")
        resposta = input("Escolha a opção correta: ")
        if (
            not resposta.isdigit()
            or int(resposta) < 1
            or int(resposta) > len(questao["opcoes"])
        ):
            print("Opção inexistente. Tente novamente.\n")
            continue
        resposta = int(resposta)
        if questao["opcoes"][resposta - 1] == questao["resposta"]:
            print("Resposta correta!\n")
            pontuacao += 1
        else:
            print(f"Resposta errada. A resposta correta é: {questao['resposta']}\n")
        print("-" * 50)

    print(f"Você acertou {pontuacao} de {len(perguntas)} perguntas.")
    if pontuacao == len(perguntas):
        print("Parabéns! Você é um verdadeiro especialista em Fórmula E!")
    else:
        print("Continue aprendendo mais sobre Fórmula E e tente novamente!")
    input("Pressione Enter para continuar...")


def main():
    """
    Função principal que gerencia o fluxo do programa.
    """
    carros = criar_lista_de_carros()
    pilotos = criar_lista_de_pilotos()
    estatisticas = obter_estatisticas()
    noticias = obter_noticias()
    eventos = obter_eventos_disponiveis()

    while True:
        opcao = menu()

        if opcao == 1:
            exibir_lista_de_carros(carros)
        elif opcao == 2:
            exibir_lista_de_pilotos(pilotos)
        elif opcao == 3:
            exibir_estatisticas(estatisticas)
        elif opcao == 4:
            exibir_noticias(noticias)
        elif opcao == 5:
            agendar_evento(eventos)
        elif opcao == 6:
            experiencia_interativa()
        elif opcao == 7:
            print("\nPrograma finalizado.")
            break
        else:
            print("\nOpção inválida. Por favor, escolha uma opção válida.")
            input("Pressione Enter para continuar...")


if __name__ == "__main__":
    main()
