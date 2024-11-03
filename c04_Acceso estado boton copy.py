import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# Subclase QMainWindow para personalizar la ventana principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.interruptor_activado = False
        self.setWindowTitle("Mi aplicación")

        # Código del botón
        button = QPushButton('Haz clic aquí')
        # Convertimos el botón en un interruptor que podemos dejar pulsado
        button.setCheckable(True)
        # Inicializamos el estado del botón. Podría estar activado por defecto
        button.setChecked(self.interruptor_activado)
        # Señal de click y llamada al método
        button.clicked.connect(self.boton_pulsado)
        button.clicked.connect(self.activa_interruptor)
        self.setCentralWidget(button)
        self.button = button

    # Método que se lanza con el click
    def boton_pulsado(self):
        print("¡Señal recibida!")

    def activa_interruptor(self, checked):
        self.interruptor_activado = checked
        print("¿Activado?", self.interruptor_activado)
        # Imprimo accediendo al estado del interruptor desde self
        print("¿Activado (self)?", self.button.isChecked())

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()