from PyQt4 import QtCore, QtGui
import sys
import numpy as np
from teste import save_file
np.set_printoptions(suppress=True)

class Dialog(QtGui.QDialog):

    def __init__(self):
        super(Dialog, self).__init__()
        
        mainLayout = QtGui.QVBoxLayout()
        self.createGridGroupBox()        
       
        mainLayout.addWidget(self.gridGroupBox)

        buttonBox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok |QtGui.QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        

        self.create_docBtn = QtGui.QPushButton("Save input")
        self.create_docBtn.clicked.connect(self.store_input)
        mainLayout.addWidget(self.create_docBtn)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

    def createGridGroupBox(self):
        self.gridGroupBox = QtGui.QGroupBox("Options")
        layout = QtGui.QGridLayout()
            
        sections = ("Number of loci", "Sampling Vector", "Initial deme sizes","Initial migration matrix", "Time of change", "Deme sizes")       

        layout.addWidget(QtGui.QLabel(sections[0]),0,0)
        layout.addWidget(QtGui.QLabel(sections[1]),1,0)
        layout.addWidget(QtGui.QLabel(sections[2]),2,0) 
        layout.addWidget(QtGui.QLabel(sections[4]),5,0)
        layout.addWidget(QtGui.QLabel(sections[5]),6,0)

        self.line0 = QtGui.QLineEdit()   
        layout.addWidget(self.line0, 0,1)
        self.line1 = QtGui.QLineEdit()
        layout.addWidget(self.line1, 1,1)
        self.line2 = QtGui.QLineEdit()        
        layout.addWidget(self.line2, 2,1)
        self.line4 = QtGui.QLineEdit()        
        layout.addWidget(self.line4, 5,1)
        self.line5 = QtGui.QLineEdit()        
        layout.addWidget(self.line5, 6,1)
  
        self.gridGroupBox.setLayout(layout)

    def store_input(self):
        numinput0 = self.line0.text()
        numinput1 = self.line1.text()
        numinput2 = self.line2.text()
        numinput3 = self.line4.text()
        numinput4 = self.line5.text()

     
        m_array = np.zeros((5, 1),dtype=float)
        m_array2=np.zeros((5,1),dtype=float)
        
      
        m_array[0,0] = numinput0
        m_array[1,0] = numinput1
        m_array[2,0] = numinput2
        m_array[3,0] = numinput3
        m_array[4,0] = numinput4
        array = np.hstack((m_array2,m_array))
        print array

        
        


def main():
    app = QtGui.QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(dialog.exec_())

if __name__ == '__main__':
    main()
