import random
import time
import inquirer as inquirer
import openai
from senha import API_KEY

class CaraCara:
    def __init__(self):

        openai.api_key = f"{API_KEY}"

        self.caracteristicas = None
        self.pessoaSecreta = None
        self.pessoaSelecionada = None
        self.dicaPessoa = []
        self.listaPessoas = []
        self.personagens = []
        self.caracteristicas = []

# ----------------------------------------------------------------------------------------------------------------------

    def inicio(self):
        print('-=-' * 20)
        print('O jogo da Cara a Cara!'.center(60, ' '))
        print('-=-' * 20)

        time.sleep(1)

        questions = [
            inquirer.List('comando',
                          message='Deseja iniciar?',
                          choices=['SIM', 'NÃO'],
                          ),
        ]
        answers = inquirer.prompt(questions)

        print('-=-' * 20)

        if answers['comando'] == 'SIM':
            print('VAMOS INICIAR!!'.center(60, ' '))
            print('-=-' * 20)
            print('\nO tema é desenho animado!'.center(60, ' '))
            print("Você tem que adivinhar qual personagem estou pensando. Faça perguntas que possam ser respondidas com 'sim' ou 'não'.")
            print("Para desistir, digite 'desisto'.")
            time.sleep(1)
            self.jogando()

        elif answers['comando'] == 'NÃO':
            print('Okay! Até a proxima!'.center(90, ' '))
            print('-=-' * 30)


# ----------------------------------------------------------------------------------------------------------------------

    def secreto(self):

        # Lista de personagens
        self.personagens = ["Mickey Mouse", "Bob Esponja", "Pica-Pau", "Scooby-Doo", "Pernalonga", "Lindinha", "Florzinha", "Docinho", "Garfield"]

        self.caracteristicas = [
            {"Mickey Mouse": ["Você é alguem que usa luvas brancas", "Você é alguem que tem orelhas grandes"]},
            {"Bob Esponja": ["Você é amerelo", "Você mora no fundo do mar", "Você gosta de aguas vivas"]},
            {"Pica-Pau": ["É famoso", "Tem bico grande", "É vermelho e azul", "É da infancia"]},
            {"Scooby-Doo": ["Você é o mascote e amigo de um grupo", "Você é um animal que fala", "Você tem o melhor amigo como dono"]},
            {"Pernalonga": ["Você é do Looney Tunes", "Você é o mais inteligente", "O mais saudavel"]},
            {"Lindinha": ["Sua cor favorita é azul", "Você participa de um trio", "Você é bem gentil", "Você é super forte"]},
            {"Florzinha": ["Sua cor favorita é vermelho", "Você é lider do trio", "Você é bem determinada", "Você é super forte"]},
            {"Docinho": ["Sua cor favorita é verde", "Você participa de um trio", "Você é bem estressada", "Você é super forte"]},
            {"Garfield": ["Você é um felino laranja", "Gosta muito de comida", "Você é preguiçoso", "Você falo tabom?"]}
        ]

        while True:

            self.pessoaSelecionada = random.choice(self.personagens)
            self.listaPessoas.append(self.pessoaSelecionada)

            if self.pessoaSelecionada in self.listaPessoas:
                self.pessoaSecreta = self.pessoaSelecionada

            for carac in self.caracteristicas:
                print(carac.get(__key=))
                print(self.pessoaSecreta)
                if carac.keys() == self.pessoaSecreta:
                    print(carac.values())
                    self.dicaPessoa.append(carac.values())
            print(self.dicaPessoa)

            break

        return self.personagens, self.caracteristicas
# ----------------------------------------------------------------------------------------------------------------------

    def ask_gpt(self, prompt):

        self.secreto()

        openai.api_key = f"{API_KEY}"
        model_engine = "ada"
        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].text.strip()


    def jogando(self):

        sum = 0

        while True:

            pergunta = input("\nFaça sua pergunta: ")
            sum += 1

            if pergunta.lower() == "desisto":
                print(f"O personagem era {self.pessoaSecreta}. Tente novamente da próxima vez!")
                break

            resposta = self.ask_gpt(f"Vamos jogar um jogo chamado Cara a Cara(Quem sou eu?)\n Eu sou o {self.pessoaSecreta}, mas não sei disso.\n Essa é minha pergunta sobre ele para eu tentar acertar quem sou eu: {pergunta}?\n Responda apenas com sim ou não baseado nas caracteristicas do meu personagem.")

            if sum >= 1:
                print(f'Sua dica é: \n{self.dicaPessoa}')

            if self.pessoaSecreta in pergunta.title():
                print("Parabens você acertou")
                break

            if "sim" in resposta.lower():
                print("Sim")
            elif "não" in resposta.lower():
                print("Não")
            else:
                print(f"Modelo respondeu: {resposta}. Tente fazer outra pergunta.")


jogoCara = CaraCara()
jogoCara.inicio()
