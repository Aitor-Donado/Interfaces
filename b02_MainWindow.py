# Configuración alternativa, creamos el botón fuera de la ventana

import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget


# Subclase QMainWindow para personalizar la ventana principal
class MainWindow(QMainWindow):
    def __init__(self, botonera):
        super().__init__()

        self.setWindowTitle("Mi aplicación")
        
        # Crear un widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Colocar el botón como "Widget central".
        layout = QVBoxLayout()
        for boton in botonera:
            layout.addWidget(boton)

        # Aplicar el layout al widget central
        central_widget.setLayout(layout)


app = QApplication(sys.argv)

boton1 = QPushButton('Haz clic aquí')
boton2 = QPushButton('Haz clic aquí')
boton3 = QPushButton('Haz clic aquí')

botonera = [boton1, boton2, boton3]

ventana = MainWindow(botonera)
ventana.show()

app.exec()