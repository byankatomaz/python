import openai
from senha import API_KEY
import random

# Configurar a API Key da OpenAI
openai.api_key = f"{API_KEY}"

# Lista de personagens com suas características
personagens = [
    {
        "nome": "Mario",
        "altura": "1,55m",
        "idade": "26 anos",
        "personalidade": "amigável, corajoso e altruísta"
    },
    {
        "nome": "Luigi",
        "altura": "1,76m",
        "idade": "27 anos",
        "personalidade": "tímido, gentil e inteligente"
    },
    {
        "nome": "Princesa Peach",
        "altura": "1,73m",
        "idade": "24 anos",
        "personalidade": "bondosa, inteligente e leal"
    },
    # adicione mais personagens aqui
]

# Função para sortear um personagem aleatoriamente
def sortear_personagem():
    return random.choice(personagens)

def gerar_resposta(personagem, pergunta):
    # Consultar a API da OpenAI para gerar uma resposta com base nas características do personagem
    prompt = f"Vamos brincar de Cara A Cara(Quem sou eu?), lembre-se das regras. Esse é o meu personagem: {personagem['nome']}. Vou fazer perguntas sobre ele: {pergunta}, e você responde com sim ou não de acordo com as caracteristicas dele. Nunca fale o nome do personagem"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=50,
        n=1,
        stop=None,
        timeout=10,
    )
    resposta = response.choices[0].text.strip()

    # Verificar se a resposta contém apenas "yes" ou "no", e retornar "Sim" ou "Não"
    if resposta.lower() == "yes":
        return "Sim"
    elif resposta.lower() == "no":
        return "Não"
    else:
        return resposta


# Fluxo de jogo
while True:
    # Sortear um personagem aleatoriamente
    personagem_sorteado = sortear_personagem()

    # Iniciar o jogo
    print("Jogo Cara a Cara: Quem sou eu?")
    print(f"Eu sou um personagem {personagem_sorteado['nome']}.")

    # Controlar o número de perguntas feitas e o número de tentativas
    num_perguntas = 0
    num_tentativas = 0
    dicas = []

    # O usuário faz perguntas para tentar adivinhar quem é o personagem
    acertou = False
    while not acertou:
        pergunta = input("Qual sua pergunta? ")
        resposta = gerar_resposta(personagem_sorteado, pergunta)
        print(resposta)

        # Adicionar a pergunta às dicas após 3 perguntas
        num_perguntas += 1
        if num_perguntas == 3:
            dicas.append(pergunta)

        # Verificar se o usuário adivinhou corretamente
        if personagem_sorteado["nome"] in pergunta:
            acertou = True
        else:
            num_tentativas += 1

        # Informar ao usuário que ele perdeu após 5 tentativas
        if num_tentativas == 5:
            print(f"Você perdeu! O personagem era {personagem_sorteado['nome']}.")
            break

    # Se o usuário acertou, informar o número de tentativas e as dicas
    if acertou:
        print(f"Parabéns, você acertou em {num_tentativas} tentativas!")
        if dicas:
            print("Dicas:")
            for dica in dicas:
                print(f"- {dica}")

    # Perguntar se o usuário quer jogar novamente
    jogar_novamente = input("Deseja jogar novamente? (s/n) ")
    if jogar_novamente.lower() != "s":
        break
