import sys
from PyQt4 import QtGui, QtCore

lista = ['aa', 'ab', 'ac']
listb = ['ba', 'bb', 'bc']
listc = ['ca', 'cb', 'cc']
mystruct = {'A':lista, 'B':listb, 'C':listc}


class MyTable(QtGui.QTableWidget):
    def __init__(self, thestruct, *args):
        QtGui.QTableWidget.__init__(self, *args)
        self.data = thestruct
        self.setmydata()

    def setmydata(self):
        n = 0
        for key in self.data:
            m = 0
            for item in self.data[key]:
                newitem = QtGui.QTableWidgetItem(item)
                if key == 'A':
                    newitem.setBackground(QtGui.QColor(100,100,150))
                elif key == 'B':
                    newitem.setBackground(QtGui.QColor(100,150,100))
                else:
                    newitem.setBackground(QtGui.QColor(150,100,100))
                self.setItem(m, n, newitem)
                m += 1
            n += 1


def main(args):
    app = QtGui.QApplication(args)
    table = MyTable(mystruct, 5, 3)
    table.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main(sys.argv)