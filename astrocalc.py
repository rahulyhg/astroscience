#!/usr/bin/env python3
from GUI.AstroCalc import mainwindow
import astromodule as dvg
import math
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox, qApp, QTableView
from PyQt5.QtCore import QSettings, QPoint, QSize, QObject
# import dvgscience.GUI.AstroCalc.astroressources_rc

class AstrocalcGui(QMainWindow):

    def __init__(self):
        # Create our main window
        super(AstrocalcGui,self  ).__init__()
        self.gui = mainwindow.Ui_MainWindow()
        self.gui.setupUi(self)
        # Use QSettings to store the position and size of our form
        self.settings = QSettings('astron', 'AstrocalcGui')
        # Before the form is shown, set the position and size, if it is
        # the first time, default settings are used (QSize...)
        self.resize(self.settings.value("size", QSize(640, 480)))
        self.move(self.settings.value("pos", QPoint(50, 50)))

        # --- Connect the events to the buttons
        self.gui.btnConvertGSTLST.clicked.connect(self.gstToLst)
        self.gui.btnCalcEaster.clicked.connect(self.calcEaster)
        self.gui.btnConvertGCDJD.clicked.connect(self.calcJulianDate)

        # --- Connect actions (toolbar button clicks)
        self.gui.actionExit.triggered.connect(qApp.quit)

    def calcEaster(self):
        # Calculate the date of easter

        # Validate user input
        c3 = self.gui.txtEasterYear.text()
        if len(c3) == 0 or int(c3) < 1582:
            msg = QMessageBox()

            msg.setIcon(QMessageBox.Critical)
            msg.setText("Invalid input for the year!")
            msg.setInformativeText("Year value should be at least 1583!")
            msg.setWindowTitle("Error")
            msg.setDetailedText("Enter year as from 1583. \nFrom there, there is no limit on the year entered.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return
        # Year seems ok, calculate the date
        c3 = int(c3)
        easterdy = dvg.calceaster(c3)
        self.gui.txtEasterDay.setText(str(math.trunc(easterdy[0])))
        eastermonth = 'March' if easterdy[1] == 3 else 'April'
        self.gui.txtEasterMonth.setText(eastermonth)

    def calcJulianDate(self):
        # Convert Greenwich Calendar Date to Julian Date
        result = dvg.cdjd(float(self.gui.txtGDJD.text().replace(',', '.')),
                          int(self.gui.txtGMJD.text()),
                          int(self.gui.txtGDJY.text()))
        self.gui.txtJulianDate.setText(str(result))


    def gstToLst(self):
        # Conversion of Greenwich Siderial time to Local Siderial Time.
        #
        c3 = int(self.gui.spinGTLHours.text())
        c4 = int(self.gui.spinGTLMinutes.text())
        c5a = self.gui.spinGTLSeconds.text()
        # Needed to do this to avoid an error with the ',' decimal
        # sign in the doublespinbox widget
        c5correction = c5a.replace(',', '.')
        c5 = float(c5correction)
        c6 = int(self.gui.spinGTLGeoL.text())
        # Convert
        result = dvg.gstlst(c3, c4, c5, c6)
        self.gui.txtLSTHour.setText(str(result[0]))
        self.gui.txtLSTMinutes.setText(str(result[1]))
        self.gui.txtLSTSeconds.setText(str(result[2]))

    def closeEvent(self, e):
        # When the QMainWindow is closed, the closeEvent is triggered automatically
        # Write window size and position to config file
        self.settings.setValue("size", self.size())
        self.settings.setValue("pos", self.pos())
        e.accept()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    frame = AstrocalcGui()
    frame.show()
    app.exec()
    sys.exit()