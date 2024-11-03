from PyQt6.QtWidgets import QApplication, QWidget

# Sólo es necesario para acceder a los argumentos de la línea de comando
import sys

# Necesita una (¡y solo una!) instancia de QApplication por aplicación.
# Pase sys.argv para permitir argumentos de línea de comando para su aplicación.
# Si sabe que no utilizará argumentos de línea de comando, sustituyalo por una lista vacía 
# de esta manera: QApplication([])
app = QApplication(sys.argv)

# Crea un widget Qt, que será nuestra ventana.
ventana = QWidget()
ventana.show()  #¡¡¡IMPORTANTE!!!!! Las ventanas están ocultas de forma predeterminada.

# Iniciar el ciclo de eventos.
app.exec()

# Su aplicación no llegará aquí hasta que salga y el evento
# bucle se ha detenido.
print("Has cerrado la ventana")