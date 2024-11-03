import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget


# Subclase QMainWindow para personalizar la ventana principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi Aplicación")
        widget = QLabel("Hola")
        # Tomamos el objeto "fuente" del widget para poder modificarlo y devolverlo al widget
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)
        # Alineación horizontal y vertical del texto
        widget.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.setCentralWidget(widget)



app = QApplication(sys.argv)

ventana = MainWindow()
ventana.show()

app.exec()