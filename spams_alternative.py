
from PyQt4 import QtCore, QtGui


class Dialog(QtGui.QDialog):
    NumGridRows = 6
    NumButtons = 4

    def __init__(self):
        super(Dialog, self).__init__()

        self.createHorizontalGroupBox()
        self.createGridGroupBox()
      

        buttonBox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QtGui.QVBoxLayout()
        
        mainLayout.addWidget(self.horizontalGroupBox)
        mainLayout.addWidget(self.gridGroupBox)
        mainLayout.addWidget(buttonBox)

        self.setLayout(mainLayout)
        self.setWindowTitle("SPAms alternative")


    def createHorizontalGroupBox(self):
        self.horizontalGroupBox = QtGui.QGroupBox("Population dynamics")
        layout = QtGui.QHBoxLayout()
        models = ("Stepping stone", "Island","model1", "model2")
        for m in models:
            button = QtGui.QPushButton(m)
            layout.addWidget(button)

        self.horizontalGroupBox.setLayout(layout)


    def createGridGroupBox(self):
        self.gridGroupBox = QtGui.QGroupBox("Options")
        layout = QtGui.QGridLayout()
        sections = ("Number of loci", "Sampling vector", "Initial deme sizes", "Initial migration matrix", "Time of change", "Deme sizes")
        for i in sections:
            label = QtGui.QLabel()
	    label.setText(i)
            lineEdit = QtGui.QLineEdit()
            layout.addWidget(label)
            layout.addWidget(lineEdit)

        
        self.gridGroupBox.setLayout(layout)



if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec_())
