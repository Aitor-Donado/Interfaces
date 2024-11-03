import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox, QLineEdit, QVBoxLayout, QWidget


# Subclase QMainWindow para personalizar la ventana principal
class MainWindow(QMainWindow):
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

    def show_state(self, s):
        print(Qt.CheckState(s) == Qt.CheckState.Checked)
        print(s)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()