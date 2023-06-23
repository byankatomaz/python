from PySide6.QtWidgets import *
from PySide6.QtGui import QMovie
from PySide6.QtCore import QTimer
from escape import  Ui_MainWindow


# noinspection PyUnresolvedReferences,PyArgumentList
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("ESCAPAPE THE PYRAMID")

        # pagina 1
        self.btn_jogar.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_2))
        # pagina 2
        self.btn_jogar_2.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_3))
        # pagina 3
        self.btn_gigante_1.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_2))
        # pagina 4
        #self.btn_porta.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_4))
        # pagina 5
        self.btn_portaLua.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_5))
        # pagina 6
        self.btn_gigante_2.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_4))
        
        #caso o usuario enviar o input e estiver certo: # página 7
        self.btn_enviar.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_6))
        # página 8
        self.btn_macaquinho.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_7))
        # página 9
        self.btn_macaquinho_3.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_8))
        # pagina 10
        self.btn_gigante_3.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_7))
        # pagina 11
        self.btn_macaquinho_resposta.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_9))
        #caso o usuario enviar o input e estiver certo: # página 12
        self.btn_enviar_2.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_10))
        # página 13
        self.btn_caminho2.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_11))
        # página 14 (caso tenha errado)
        self.btn_caminho1_errado.clicked.connect(lambda: self.paginas.setCurrentWidget(self.prank))
        # página 15
        self.btn_dica_3.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_12))
        # página 16
        self.btn_gigante_5.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_11))
        # pagina 17
        self.btn_altar.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_13))
        # página 18
        self.btn_gigante_6.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_11))
        #caso o usuario enviar o input e estiver certo: # página 18
        self.btn_enviar_3.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_14))
        
        # página 19
        self.btn_portaSaida.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_15))
        # página 20 (caso tenha errado)
        self.btn_gigante_7.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_14))
        # página 21
        self.btn_lobo.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_16))
        # página 22
        self.btn_saida.clicked.connect(lambda: self.paginas.setCurrentWidget(self.page_17))
    
    
    def showEvent(self, event):
        self.paginas.setCurrentWidget(self.page_1)

if __name__ == '__main__':
    app = QApplication()
    janela = MainWindow()
    janela.show()
    app.exec()
