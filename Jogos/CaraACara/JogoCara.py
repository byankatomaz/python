import random


class CaraCara:
    def __init__(self):

        self.pessoas = None
        self.dicas = None

    def selecionado(self):
        # Lista de personagens
        personagens = [
            {"nome": "Mickey Mouse", "caracteristicas": ["Usa luvas brancas", "Tem orelhas grandes"]},
            {"nome": "Bob Esponja", "caracteristicas": ["Amerelo", "Mora no fundo do mar", "Gosta de aguas vivas"]},
            {"nome": "Pica-Pau",
             "caracteristicas": ["É famoso", "Tem bico grande", "É vermelho e azul", "É da infancia"]},
            {"nome": "Scooby-Doo",
             "caracteristicas": ["É o mascote do grupo", "Ele fala", "Tem o melhor amigo como dono"]},
            {"nome": "Pernalonga", "caracteristicas": ["Looney Tunes", "Inteligente", "O mais saudavel"]},
            {"nome": "Lindinha",
             "caracteristicas": ["Cor favorita é azul", "Participa de um trio", "Gentil", "Super forte"]},
            {"nome": "Florzinha",
             "caracteristicas": ["Cor favorita é vermelho", "Lider do trio", "Determinada", "Super forte"]},
            {"nome": "Docinho",
             "caracteristicas": ["Cor favorita é verde", "Participa de um trio", "Estressada", "Super forte"]},
            {"nome": "Garfield", "caracteristicas": ["Laranja", "Felino", "Preguiçoso", "Ama comida"]}

        ]

        # Perguntas e respostas
        perguntas = {
            "Sou uma garota?": {"Mickey Mouse": "sim", "Bob Esponja": "não", "Pica-pau": "não", "Scooby-Doo": "não",
                                "Pernalonga": "não",
                                "Lindinha": "sim", "Florzinha": "sim", "Docinho": "sim", "Garfield": "não"
                                },
            "Sou um garoto?": {"Mickey Mouse": "sim", "Pikachu": "sim", "Batman": "sim",
                               "Bob Esponja": "sim", "Pica-pau": "sim", "Scooby-Doo": "sim", "Pernalonga": "sim",
                               "Lindinha": "não", "não": "não", "Docinho": "não", "Garfield": "sim"
                               },
            "é um humano?": {"Mickey Mouse": "não", "Bob Esponja": "não", "Pica-pau": "não", "Scooby-Doo": "não",
                             "Pernalonga": "não",
                             "Lindinha": "sim", "Florzinha": "sim", "Docinho": "sim", "Garfield": "não"
                             },
            "Tenho cabelo?": {"Mickey Mouse": "não", "Bob Esponja": "não", "Pica-pau": "não", "Scooby-Doo": "não",
                              "Pernalonga": "não",
                              "Lindinha": "sim", "Florzinha": "sim", "Docinho": "sim", "Garfield": "não"
                              },
            "Tenho super poderes?": {"Mickey Mouse": "não", "Bob Esponja": "não", "Pica-pau": "não",
                                     "Scooby-Doo": "não",
                                     "Pernalonga": "não",
                                     "Lindinha": "sim", "Florzinha": "sim", "Docinho": "sim", "Garfield": "não"
                                     },
            "Tenho olhos verdes?": {"Mickey Mouse": "sim", "Pikachu": "não", "Batman": "não",
                                    "Bob Esponja": "não", "Pica-pau": "não", "Scooby-Doo": "não", "Pernalonga": "não",
                                    "Lindinha": "sim", "Florzinha": "sim", "Docinho": "sim", "Garfield": "não"
                                    },
            "Sou verde?": {"Mickey Mouse": "não", "Bob Esponja": "não", "Pica-pau": "não", "Scooby-Doo": "não",
                           "Pernalonga": "não",
                           "Lindinha": "não", "Florzinha": "não", "Docinho": "não", "Garfield": "não"
                           },
            "Sou amarelo?": {"Mickey Mouse": "não", "Bob Esponja": "sim", "Pica-pau": "não", "Scooby-Doo": "não",
                             "Pernalonga": "não",
                             "Lindinha": "não", "Florzinha": "não", "Docinho": "não", "Garfield": "não"
                             },
            "Sou um gato?": {"Mickey Mouse": "não", "Pikachu": "não", "Batman": "não",
                             "Bob Esponja": "não", "Pica-pau": "não", "Scooby-Doo": "não", "Pernalonga": "não",
                             "Lindinha": "não", "Florzinha": "não", "Docinho": "não", "Garfield": "sim"
                             },
            "Sou um cachorro?": {"Mickey Mouse": "não", "Pikachu": "não", "Batman": "não",
                                 "Bob Esponja": "não", "Pica-pau": "não", "Scooby-Doo": "não", "Pernalonga": "não",
                                 "Lindinha": "não", "Florzinha": "não", "Docinho": "não", "Garfield": "não"
                                 },
            "Sou da Disney?": {"Mickey Mouse": "sim",
                               "Bob Esponja": "não", "Pica-pau": "não", "Scooby-Doo": "não", "Pernalonga": "não",
                               "Lindinha": "não", "Florzinha": "não", "Docinho": "não", "Garfield": "não"
                               },
            "Caço aguas vivas?": {"Mickey Mouse": "não", "Bob Esponja": "sim", "Pica-pau": "não", "Scooby-Doo": "não",
                                  "Pernalonga": "não",
                                  "Lindinha": "não", "Florzinha": "não", "Docinho": "não", "Garfield": "não"
                                  },
            "Uso luvas?": {"Mickey Mouse": "sim", "Bob Esponja": "não", "Pica-pau": "não", "Scooby-Doo": "não",
                           "Pernalonga": "sim",
                           "Lindinha": "não", "Florzinha": "não", "Docinho": "não", "Garfield": "não"
                           },
            "Sou um desenho famoso?": {"Mickey Mouse": "sim", "Bob Esponja": "sim", "Pica-pau": "sim", "Scooby-Doo": "sim",
                                       "Pernalonga": "sim",
                                       "Lindinha": "sim", "Florzinha": "sim", "Docinho": "sim", "Garfield": "sim"
                                       },
            "Faço parte de um trio?": {"Mickey Mouse": "não", "Bob Esponja": "não", "Pica-pau": "não", "Scooby-Doo": "não",
                                       "Pernalonga": "não",
                                       "Lindinha": "sim", "Florzinha": "sim", "Docinho": "sim", "Garfield": "não"
                                       },
            "Sou estressada?": {"Mickey Mouse": "não", "Bob Esponja": "não", "Pica-pau": "não", "Scooby-Doo": "não",
                                "Pernalonga": "não",
                                "Lindinha": "não", "Florzinha": "não", "Docinho": "sim", "Garfield": "não"
                                },
            "Sou gentil?": {"Mickey Mouse": "não", "Bob Esponja": "não", "Pica-pau": "não", "Scooby-Doo": "não",
                            "Pernalonga": "não",
                            "Lindinha": "sim", "Florzinha": "não", "Docinho": "não", "Garfield": "não"
                            },
            "Sou a lider?": {"Mickey Mouse": "não", "Bob Esponja": "não", "Pica-pau": "não", "Scooby-Doo": "não",
                             "Pernalonga": "não",
                             "Lindinha": "não", "Florzinha": "sim", "Docinho": "não", "Garfield": "não"
                             },
            "Moro no mar?": {"Mickey Mouse": "não", "Bob Esponja": "sim", "Pica-pau": "não", "Scooby-Doo": "não",
                             "Pernalonga": "não",
                             "Lindinha": "não", "Florzinha": "não", "Docinho": "não", "Garfield": "não"
                             },
            "Faço hamburgues?": {"Mickey Mouse": "não", "Bob Esponja": "sim", "Pica-pau": "não", "Scooby-Doo": "não",
                                 "Pernalonga": "não",
                                 "Lindinha": "não", "Florzinha": "não", "Docinho": "não", "Garfield": "não"
                                 },
            "Uso capa?": {"Mickey Mouse": "não", "Pikachu": "não", "Batman": "sim",
                          "Bob Esponja": "não", "Pica-pau": "não", "Scooby-Doo": "não", "Pernalonga": "não",
                          "Lindinha": "sim", "Florzinha": "sim", "Docinho": "sim", "Garfield": "não"
                          }
        }

        # Escolhe um personagem aleatório
        personagem_secreto = random.choice(personagens)

        for i in range.randint(personagens["caracteristicas"])

        dica = personagem_secreto["caracteristicas"][0]

        # Início do jogo
        print("Vamos jogar Cara a Cara! PERSONAGENS DE DESENHO")

        dicas = 0

        while dicas < 10:

            # Pergunta ao usuário
            pergunta = input("Faça uma pergunta sobre o personagem: ")

            # Verifica se a pergunta está na lista de perguntas
            if pergunta in perguntas:
                # Obtém a resposta do chat bot baseado no personagem secreto
                resposta = perguntas[pergunta][personagem_secreto["nome"]]
                print(f"{resposta}, o personagem é {dica}")

                dicas += 1

            else:
                print("Desculpe, não entendi a sua pergunta. Tente novamente.")
                # Verifica se o usuário adivinhou o personagem

            if dicas == 3:
                palpite = input("Quem é o personagem? ")
                if palpite == personagem_secreto["nome"]:
                    print("Parabéns, você acertou!")
                    break
                else:
                    print("Ops, você errou! Tente novamente.")


jogoCara = CaraCara()
jogoCara.selecionado()
