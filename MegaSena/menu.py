from update import inserir_jogos
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Web:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.numeros_mega_sena = []  # Lista para armazenar os números da Mega Sena
        self.abrir_site()

    def abrir_site(self):

        for i in range(2016, 2023):
            site = f'https://asloterias.com.br/resultados-da-mega-sena-{i}'
            map = {
                "sorteio": {
                    'xpath': '/html/body/main/div[2]/div/div/div[1]/strong[%numSorteio%]'
                },
                "numero":{
                    'xpath': '/html/body/main/div[2]/div/div/div[1]/span[@numeros@]'
                }
            }

            self.driver.get(site)
            sleep(5)
            k = 1

            while True:
                try:
                    sum = 0
                    for j in range(150):
                        numero_sorteio = self.driver.find_element(By.XPATH, map['sorteio']['xpath'].replace('%numSorteio%', f'{j+4}')).text
                        sum+=1

                except:
                    break

            print(sum)

            for j in range(sum):

                numero_sorteio = self.driver.find_element(By.XPATH, map['sorteio']['xpath'].replace('%numSorteio%', f'{j+4}')).text
                numeros_sorteados = []

                for n in range(6):
                    numero_sortado = self.driver.find_element(By.XPATH, map['numero']['xpath'].replace('@numeros@', f'{k}')).text
                    numeros_sorteados.append(numero_sortado)
                    k += 1

                self.numeros_mega_sena.append(numeros_sorteados)
                num1, num2, num3, num4, num5, num6 = numeros_sorteados
                print(numero_sorteio, i, num1, num2, num3, num4, num5, num6)
                inserir_jogos(numero_sorteio, i, num1, num2, num3, num4, num5, num6)  # Chama a função para inserir no BD

Web()