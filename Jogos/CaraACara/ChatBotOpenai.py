import openai
import random
from senha import API_KEY

# Defina a sua chave de API do OpenAI
openai.api_key = f"{API_KEY}"

# Defina o modelo que você deseja usar
model_engine = "ada"

# Defina a lista de personagens disponíveis
personagens = ["Goku", "Harry Potter", "Homem-Aranha", "Darth Vader", "Superman", "Batman"]

# Escolha um personagem aleatório para o jogo
personagem_secreto = random.choice(personagens)


# Defina a função para enviar a solicitação API e obter a resposta
def ask_gpt(prompt):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()


# Inicie o jogo de adivinhação
print("Bem-vindo ao jogo 'Quem sou eu?'")
print("Você tem que adivinhar qual personagem estou pensando. Faça perguntas que possam ser respondidas com 'sim' ou 'não'.")
print("Para desistir, digite 'desisto'.")

sum = 0

while True:
    pergunta = input("Sua pergunta: ")
    sum += 1

    if pergunta.lower() == "desisto":
        print(f"O personagem era {personagem_secreto}. Tente novamente da próxima vez!")
        break

    resposta = ask_gpt(f"Vamos jogar um jogo chamado Cara a Cara(Quem sou eu?)\n Eu sou o {personagem_secreto}, mas não sei disso.\n Essa é minha pergunta sobre ele para eu tentar acertar quem sou eu: {pergunta}?\n Responda apenas com sim ou não baseado nas caracteristicas do meu personagem.")

    if sum == 3:
        resposta = ask_gpt(f"Chat, me de UMA dica sobre a caracteristica do personagem, apenas UMA, por exemplo: 'Você tem um desenho sobre você'.")
        print(resposta)

    if personagem_secreto in pergunta.title():
        print("Parabens você acertou")
        break

    if "sim" in resposta.lower():
        print("Sim")
    elif "não" in resposta.lower():
        print("Não")
    else:
        print(f"Modelo respondeu: {resposta}. Tente fazer outra pergunta.")

