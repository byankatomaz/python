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
    
    
    def showEvent(self, event):
        self.paginas.setCurrentWidget(self.page_1)

if __name__ == '__main__':
    app = QApplication()
    janela = MainWindow()
    janela.show()
    app.exec()
