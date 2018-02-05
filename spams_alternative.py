
from PyQt4 import QtCore, QtGui


class Dialog(QtGui.QDialog):
    NumGridRows = 3
    NumButtons = 4

    def __init__(self):
        super(Dialog, self).__init__()

        self.createMenu()
        self.createHorizontalGroupBox()
      

        buttonBox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.setMenuBar(self.menuBar)
        mainLayout.addWidget(self.horizontalGroupBox)
   
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        self.setWindowTitle("SPAms alternative")

    def createMenu(self):
        self.menuBar = QtGui.QMenuBar()
        self.fileMenu = QtGui.QMenu("&File", self)
        self.exitAction = self.fileMenu.addAction("E&xit")
        self.menuBar.addMenu(self.fileMenu)
        self.exitAction.triggered.connect(self.accept)

    def createHorizontalGroupBox(self):
        self.horizontalGroupBox = QtGui.QGroupBox("Population dynamics")
        layout = QtGui.QHBoxLayout()
        models = ("Stepping stone", "Island","model1", "model2")
        for m in models:
            button = QtGui.QPushButton(m)
            layout.addWidget(button)

        self.horizontalGroupBox.setLayout(layout)

   


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec_())
