from PySide2.QtWidgets import QMainWindow, QStackedLayout


class Stack(QMainWindow):
    layout_widget = QStackedLayout()
    def __init__(self):
        super().__init__(self)

    def setup_ui(self):
        self.layout_widget.addWidget()
