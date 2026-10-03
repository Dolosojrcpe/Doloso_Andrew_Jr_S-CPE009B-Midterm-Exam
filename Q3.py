import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit 
from PyQt6.QtGui import QIcon

def displayName():
    name = inputName.text()
    outputName.setText(name)

script_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(script_dir, "py_icon.png")

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Midterm in OOP")
window.setGeometry(400, 500, 750, 400)
window.setWindowIcon(QIcon(icon_path))

label = QLabel("Enter your fullname", window)
label.setGeometry(100, 120, 200, 30)

inputName = QLineEdit(window)
inputName.setGeometry(400, 115, 300, 40)

button = QPushButton("Click to display your fullname", window)
button.setGeometry(100, 180, 250, 40)

outputName = QLabel("", window)
outputName.setGeometry(400, 180, 300, 40)

button.clicked.connect(displayName)

window.show()
sys.exit(app.exec())