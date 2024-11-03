import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

# Añade un label en la ventana

# Subclase QMainWindow para personalizar la ventana principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")
        
        # Código del botón
        boton = QPushButton('Haz clic aquí')
        # Señal de click y llamada al método
        boton.clicked.connect(self.boton_pulsado)
        self.setCentralWidget(boton)

    # Método que se lanza con el click
    def boton_pulsado(self):
        print("¡Señal recibida!")

app = QApplication(sys.argv)

ventana = MainWindow()
ventana.show()

app.exec()