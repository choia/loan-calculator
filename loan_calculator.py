import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)
        self.setLayout(grid)

        names = ['User Input Field', 'Static Information', 'Placeholder1', 'Placeholder2']
        positions = [(i,j) for i in range(2) for j in range(2)]

        for position, name in zip(positions, names):
            button = QPushButton(name)
            grid.addWidget(button, *position)

            self.move(300, 300)
            self.setWindowTitle('Calculator')
            self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())