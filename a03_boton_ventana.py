import sys
from PyQt6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

ventana = QPushButton('Haz clic aquí')
ventana.show()

app.exec()

print("Ventana cerrada")