import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLCDNumber
from PyQt6.QtCore import QTimer, QTime

class Reloj(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.lcd = QLCDNumber()
        self.lcd.setDigitCount(8)  # Establecer el número de dígitos
        layout.addWidget(self.lcd)
        self.setLayout(layout)

        timer = QTimer(self)
        timer.timeout.connect(self.mostrarTiempo)
        timer.start(1000)  # Actualizar cada segundo

        self.setWindowTitle("Reloj Digital")
        self.resize(300, 100)

    def mostrarTiempo(self):
        tiempo = QTime.currentTime()
        texto = tiempo.toString("hh:mm:ss")
        self.lcd.display(texto)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    reloj = Reloj()
    reloj.show()
    sys.exit(app.exec())