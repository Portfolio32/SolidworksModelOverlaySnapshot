import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt

path = 
app = QApplication(sys.argv)


image = QImage()
image.load(path)
image_label = QLabel()
image_label.setPixmap(QPixmap(image))
image_label.setWindowFlags(image_label.windowFlags() | Qt.WindowStaysOnTopHint)
image_label.show()

app.exec()