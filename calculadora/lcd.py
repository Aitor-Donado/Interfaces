# -*- coding: utf-8 -*-

from PyQt6.QtWidgets import QLCDNumber
from PyQt6 import QtCore

def lcd(centralwidget):
    lcdNumber = QLCDNumber(parent = centralwidget)
    lcdNumber.setGeometry(QtCore.QRect(23, 12, 361, 71))
    lcdNumber.setDigitCount(9)
    lcdNumber.setObjectName("lcdNumber")
    return lcdNumber