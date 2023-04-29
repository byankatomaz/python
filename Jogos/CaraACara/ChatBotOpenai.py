from senha import API_KEY
import requests
import json

headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
link = "https://api.openai.com/v1/chat/completions"
id_modelo = "gpt-3.5-turbo"

while True:
    pergunta = input("User: ")

    body_message = {
      "model": id_modelo,
      "messages": [{"role": "user", "content": f"{pergunta}"}]
    }

    body_message = json.dumps(body_message)

    requisicao = requests.post(link, headers=headers, data=body_message)

    # print(requisicao)
    # print(requisicao.text)

    resposta = requisicao.json()
    mensagem = resposta["choices"][0]["message"]["content"]

    print(f"Chat: {mensagem}")
