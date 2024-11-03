import sys
import time
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# Subclase QMainWindow para personalizar la ventana principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.interruptor_activado = False
        self.setWindowTitle("Mi aplicación")

        # Código del botón
        self.button = QPushButton('Haz clic aquí')

        # Señal de click y llamada al método
        self.button.clicked.connect(self.boton_pulsado)
        
        self.setCentralWidget(self.button)

    # Método que se lanza con el click
    def boton_pulsado(self):
        # Cambiamos el texto del botón
        self.button.setText("Ya me has pulsado.")
        # Inhabilitamos el botón. Ya no se puede volver a usar.
        self.button.setEnabled(False)
        # También cambiamos el nombre de la ventana.
        self.setWindowTitle("Aplicación con botón desactivado")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()