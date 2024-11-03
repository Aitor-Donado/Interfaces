import sys
from PyQt6.QtCore import QSize, Qt, QTimer
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget
from PyQt6.QtCore import QDateTime


# Subclase QMainWindow para personalizar la ventana principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        # Creamos un objeto Label que sirve para MOSTRAR texto
        self.label = QLabel()

        # Creamos un objeto Label que sirve para INTRODUCIR texto
        self.input = QLineEdit()

        # El objeto input genera señal al cambiar su texto
        # Lo recibe el label y replica el texto introducido
        self.input.textChanged.connect(self.label.setText)
        
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        # Crear y configurar el QTimer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_label)  # Conectar la señal timeout al slot update_label
        self.timer.start(1000)  # Intervalo en milisegundos (1000 ms = 1 segundo)

    def update_label(self):
        # Actualizar el texto del label con el tiempo actual cada segundo
        current_time = QDateTime.currentDateTime().toString("hh:mm:ss")
        self.label.setText(current_time)

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
