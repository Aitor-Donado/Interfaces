from PyQt6.QtWidgets import QPushButton, QSizePolicy
from PyQt6.QtGui import QFont

def crea_boton(gridLayoutWidget, nombre_boton):
    btn = QPushButton(parent = gridLayoutWidget)
    sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
    #sizePolicy.setHorizontalStretch(0)
    #sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(btn.sizePolicy().hasHeightForWidth())
    btn.setSizePolicy(sizePolicy)
    font = QFont()
    font.setPointSize(25)
    btn.setFont(font)
    btn.setObjectName(nombre_boton)
    return btn
