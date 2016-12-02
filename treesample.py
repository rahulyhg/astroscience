from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

styleSheet = """
QTreeView {
    alternate-background-color: #f6fafb;
    background: #e8f4fc;
}

QTreeView::item:open {
    /* background-color: #d9e2e6; */
    background-color: #c5ebfb;
    color: blue;
}

QTreeView::item:selected {
     background-color: #1d3dec;
     color: white;
}

QTreeView::branch {
    background-color: white;
}

QTreeView::branch:open {
    image: url(branch-open.png);
}

QTreeView::branch:closed:has-children {
    image: url(branch-closed.png);
}
"""


# ---------------------------------------------------------------------
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.resize(520, 300)
        self.setWindowTitle("Treeview Example")

        self.treeview = QTreeView(self)

        self.treeview.model = QFileSystemModel()
        self.treeview.model.setRootPath(QDir.currentPath())
        self.treeview.setModel(self.treeview.model)
        self.treeview.setColumnWidth(0, 150)

        self.setCentralWidget(self.treeview)

        self.treeview.clicked.connect(self.on_treeview_clicked)

        self.treeview.setAlternatingRowColors(True)
        self.setStyleSheet(styleSheet)

    # ---------------------------------------------------------------------

    @pyqtSlot(QModelIndex)
    def on_treeview_clicked(self, index):
        indexItem = self.treeview.model.index(index.row(), 0, index.parent())

        # path or filename selected
        fileName = self.treeview.model.fileName(indexItem)
        # full path/filename selected
        filePath = self.treeview.model.filePath(indexItem)

        print(fileName)
        print(filePath)


# ---------------------------------------------------------------------

if __name__ == '__main__':


    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
