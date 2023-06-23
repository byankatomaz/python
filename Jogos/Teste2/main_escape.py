from PySide6.QtWidgets import *
from PySide6.QtGui import QMovie
from PySide6.QtCore import QTimer
from escape import  Ui_MainWindow


# noinspection PyUnresolvedReferences,PyArgumentList
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.cont = 0
        self.setupUi(self)
        self.setWindowTitle("ESCAPAPE THE PYRAMID")

        # pagina 1
        self.btn_jogar.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_2))
        
        # pagina 2
        self.btn_jogar_2.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_3))
        self.btn_porta.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_4))
        
        # pagina 3
        self.btn_gigante_1.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_2))
        
        # pagina 4
        self.btn_portaLua.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_5))
        self.btn_portaLua_errado.clicked.connect(self.chances)
        self.btn_voltar_p2.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_2))
        
        # pagina 5
        self.btn_gigante_2.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_4))
        self.btn_enviar.clicked.connect(self.vericandoPrimeira)
        
        # página 6
        self.btn_macaquinho.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_7))
        self.btn_macaquinho_errado1.clicked.connect(self.chances)
        self.btn_macaquinho_errado2.clicked.connect(self.chances)
        
        # página 7
        self.btn_macaquinho_3.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_8))
        self.btn_macaquinho_resposta.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_9))
        self.btn_voltar_p6.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_6))
        
        # pagina 8
        self.btn_gigante_3.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_7))
        
        # pagina 9
        self.btn_gigante_4.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_7))
        self.btn_enviar_2.clicked.connect(self.vericandoSegunda)
        
        # página 10
        self.btn_caminho2.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_11))
        self.btn_caminho1_errado.clicked.connect(self.chances)
        
        # página 11
        self.btn_dica_3.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_12))
        self.btn_altar.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_13))
        
        # página 12
        self.btn_gigante_5.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_11))
        
        # página 13
        self.btn_gigante_6.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_11))
        self.btn_enviar_3.clicked.connect(self.vericandoTerceira)
        
        # página 14
        self.btn_portaSaida.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_15))
        self.btn_lobo_certo.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_16))
        self.btn_lobo_errado1.clicked.connect(self.chances)
        self.btn_lobo_errado2.clicked.connect(self.chances)
        self.btn_lobo_errado3.clicked.connect(self.chances)
        self.btn_lobo_errado4.clicked.connect(self.chances)
        self.btn_lobo_errado5.clicked.connect(self.chances)
        
        # página 15
        self.btn_gigante_7.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_14))
        
        # página 16
        self.btn_saida.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_17))
    
    def vericandoPrimeira(self):
        self.conteudo = self.inputUsuario.text()
        
        if self.conteudo.title() == "Lua Nova":
            self.paginas.setCurrentWidget(self.page_6)
        else:
            self.paginas.setCurrentWidget(self.page_4)
    
    def vericandoSegunda(self):
        self.conteudo = self.inputUsuario_2.text()
        
        if self.conteudo.title() == "Lá":
            self.paginas.setCurrentWidget(self.page_10)
        else:
            self.paginas.setCurrentWidget(self.page_7)
            
    def vericandoTerceira(self):
        self.conteudo = self.inputUsuario_3.text()
        
        if self.conteudo.title() == "Nova Crescente Cheia Minguante":
            self.paginas.setCurrentWidget(self.page_14)
        else:
            self.paginas.setCurrentWidget(self.page_11)
    
    def chances(self):
        self.cont += 1
        
        if self.cont == 1:
            self.paginas.setCurrentWidget(self.chance5)
    
    
    
    def showEvent(self, event):
        self.paginas.setCurrentWidget(self.page_1)

if __name__ == '__main__':
    app = QApplication()
    janela = MainWindow()
    janela.show()
    app.exec()
