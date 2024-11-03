from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Configuración de la ventana
        self.setWindowTitle('Mi Aplicación PyQt')
        self.setGeometry(300, 300, 300, 200)  # x, y, ancho, alto

        # Crear un layout vertical
        layout = QVBoxLayout()

        # Añadir widgets al layout
        boton = QPushButton('Haz clic aquí')
        layout.addWidget(boton)

        # Establecer el layout de la ventana
        self.setLayout(layout)

def main():
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()

if __name__ == '__main__':
    main()