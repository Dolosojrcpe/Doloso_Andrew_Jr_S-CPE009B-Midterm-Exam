import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtGui import QIcon

def change_color():
	button.setStyleSheet("background-color: yellow;")


app = QApplication(sys.argv)
script_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(script_dir, "py_icon.png")

window = QWidget()
window.setWindowTitle("Special Midterm Exam in OOP2")
window.setGeometry(400, 200, 500, 400)
window.setWindowIcon(QIcon(icon_path))

button = QPushButton("Click to Change the Color", window)
button.setGeometry(160, 180, 180, 40)
button.clicked.connect(change_color)

window.show()

sys.exit(app.exec())
