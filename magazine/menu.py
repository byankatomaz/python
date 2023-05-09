from time import sleep
from adicionando import inserir_xiaomi, inserir_apple, inserir_motorola, inserir_lg, inserir_samsung
from selenium import webdriver
from selenium.webdriver.common.by import By


class Web:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.xiaomi()
        # self.apple()
        # self.motorola()
        # self.lg()
        # self.samsung()

    def xiaomi(self):

        self.driver.get('https://www.magazineluiza.com.br/xiaomi/celulares-e-smartphones/s/te/xiao/')
        sleep(5)

        print('\nXiaomi')
        for k in range(15):

            if k == 2 or k == 8 or k == 11 or k == 12 or k == 13:
                continue

            lista_modelo_valor = [self.driver.find_element(By.XPATH, f'/html/body/div[1]/div/main/section[4]/div[2]/div/ul/li[{k + 1}]/a/div[3]/h2').text]
            valor = self.driver.find_element(By.XPATH, f'/html/body/div[1]/div/main/section[4]/div[2]/div/ul/li[{k + 1}]/a/div[3]/div[2]/div/p[2]').text
            lista_modelo_valor.append(valor)

            Model, valor = lista_modelo_valor

            inserir_xiaomi(Model, valor)

            print(lista_modelo_valor)

    def apple(self):

        self.driver.get('https://www.magazineluiza.com.br/iphone/celulares-e-smartphones/s/te/teip/')
        sleep(5)

        print('\nApple')
        for k in range(10):

            lista_modelo_valor = [self.driver.find_element(By.XPATH, f'/html/body/div[1]/div/main/section[4]/div[2]/div/ul/li[{k + 1}]/a/div[3]/h2').text]
            valor = self.driver.find_element(By.XPATH, f'/html/body/div[1]/div/main/section[4]/div[2]/div/ul/li[{k + 1}]/a/div[3]/div[2]/div/p[2]').text

            lista_modelo_valor.append(valor)

            Model, valor = lista_modelo_valor
            inserir_apple(Model, valor)

            print(lista_modelo_valor)

    def motorola(self):

        self.driver.get('https://www.magazineluiza.com.br/motorola/celulares-e-smartphones/s/te/srmt/')
        sleep(5)

        print('\nMotorola')
        for k in range(10):

            lista_modelo_valor = [self.driver.find_element(By.XPATH, f'/html/body/div[1]/div/main/section[4]/div[2]/div/ul/li[{k + 1}]/a/div[3]/h2').text]
            valor = self.driver.find_element(By.XPATH, f'/html/body/div[1]/div/main/section[4]/div[2]/div/ul/li[{k + 1}]/a/div[3]/div[2]/div/p[2]').text

            lista_modelo_valor.append(valor)

            Model, valor = lista_modelo_valor
            inserir_motorola(Model, valor)

            print(lista_modelo_valor)

    def lg(self):

        self.driver.get('https://www.magazineluiza.com.br/celular-lg/celulares-e-smartphones/s/te/telg/')
        sleep(5)

        print('\nLG')
        for k in range(10):

            lista_modelo_valor = [self.driver.find_element(By.XPATH, f'/html/body/div[1]/div/main/section[4]/div[2]/div/ul/li[{k + 1}]/a/div[3]/h2').text]
            valor = self.driver.find_element(By.XPATH, f'/html/body/div[1]/div/main/section[4]/div[2]/div/ul/li[{k + 1}]/a/div[3]/div[2]/div/p[2]').text

            lista_modelo_valor.append(valor)

            Model, valor = lista_modelo_valor
            inserir_lg(Model, valor)

            print(lista_modelo_valor)

    def samsung(self):

        self.driver.get('https://www.magazineluiza.com.br/samsung-galaxy/celulares-e-smartphones/s/te/galx/')
        sleep(5)

        print('\nSamsung')
        for k in range(10):

            lista_modelo_valor = [self.driver.find_element(By.XPATH, f'/html/body/div[1]/div/main/section[4]/div[2]/div/ul/li[{k + 1}]/a/div[3]/h2').text]
            valor = self.driver.find_element(By.XPATH, f'/html/body/div[1]/div/main/section[4]/div[2]/div/ul/li[{k + 1}]/a/div[3]/div[2]/div/p[2]').text

            lista_modelo_valor.append(valor)

            Model, valor = lista_modelo_valor
            inserir_samsung(Model, valor)

            print(lista_modelo_valor)


maga = Web()

