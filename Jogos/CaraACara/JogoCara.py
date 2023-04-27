from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('Teste')

conversa = [
    "Coe",
    "E ai jovem, tranquilo?",
    "Tranquilo",
    "Qual a boa de hoje?",
    "Tem um sorvete novo na sorveteria",
    "Caraca que doidera",
    "Maneiro",
    "DOIDERA"
]

while True:

    mensagem = input("Mande uma mensagem: ")

    if mensagem == "parar":
        break
    response = chatbot.get_response(mensagem)
    print(response)