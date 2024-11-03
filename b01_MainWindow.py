import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# Subclase QMainWindow para personalizar la ventana principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi aplicación")
        boton = QPushButton('Haz clic aquí')
        
        # Colocar el botón como "Widget central".
        self.setCentralWidget(boton)


app = QApplication(sys.argv)


ventana = MainWindow()
ventana.show()

app.exec()