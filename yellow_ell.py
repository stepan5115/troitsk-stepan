import sys

from PyQt5.QtCore import Qt, QPoint
import random
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.initUI()

    def initUI(self):
        self.width = 500
        self.height = 500
        self.setGeometry(300, 300, self.width, self.height)
        self.setWindowTitle('Координаты')
        self.pushButton.clicked.connect(self.print)
        self.do_paint = False

    def print(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
            self.do_paint = False

    def mouseMoveEvent(self, event):
        self.moment_y = event.y()
        self.moment_x = event.x()

    def draw_flag(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        for i in range(random.randint(5, 10)):
            r = random.randint(50, 100)
            x = random.randint(0, self.width - 100)
            y = random.randint(0, self.height - 100)
            qp.drawEllipse(x - r // 2, y - r // 2, r, r)
        self.do_paint = False


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
