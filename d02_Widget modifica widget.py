import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget


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
        self.input.textChanged.connect(self.update_label)
        
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def update_label(self, text):
        self.label.setText(text.upper())


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()