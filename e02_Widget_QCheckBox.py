import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox, QLineEdit, QVBoxLayout, QWidget


# Subclase QMainWindow para personalizar la ventana principal
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi Aplicación")
        widget = QCheckBox("Esto es un checkbox")
        # widget.setCheckState(Qt.CheckState.Checked)
        # Existe un tercer estado intermedio
        # Así: widget.setCheckState(Qt.PartiallyChecked)
        # O así: 
        widget.setTristate(True)
        widget.stateChanged.connect(self.show_state)
        self.setCentralWidget(widget)

    def show_state(self, estado):
        print(Qt.CheckState(estado) == Qt.CheckState.Checked)
        print(f"El estado es {estado}")


app = QApplication(sys.argv)

ventana = VentanaPrincipal()
ventana.show()

app.exec()