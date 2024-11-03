# Configuración alternativa, creamos el botón fuera de la ventana

import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# Subclase QMainWindow para personalizar la ventana principal
class MainWindow(QMainWindow):
    def __init__(self, boton):
        super().__init__()

        self.setWindowTitle("Mi aplicación")
        
        
        # Colocar el botón como "Widget central".
        self.setCentralWidget(boton)


app = QApplication(sys.argv)

boton = QPushButton('Haz clic aquí')
ventana = MainWindow(boton)
ventana.show()

app.exec()