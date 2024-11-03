import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# Subclase QMainWindow para personalizar la ventana principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")
        
        # Código del botón
        boton = QPushButton('Haz clic aquí')
        # Convertimos el botón en un interruptor que podemos dejar pulsado
        boton.setCheckable(True)
        # Señal de click y llamada al método
        boton.clicked.connect(self.boton_pulsado)
        boton.clicked.connect(self.interruptor_activado)
        self.setCentralWidget(boton)

    # Método que se lanza con el click
    def boton_pulsado(self):
        print("¡Señal recibida!")

    def interruptor_activado(self, checked):
        print("¿Activado?", checked)

app = QApplication(sys.argv)

ventana = MainWindow()
ventana.show()

app.exec()