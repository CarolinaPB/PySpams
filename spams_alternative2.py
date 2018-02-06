#To use this first you need to install and configure PyQt4
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
   
	self.setGeometry(300, 300, 350, 300)

        self.setLayout(mainLayout)
        self.setWindowTitle("SPAms alternative")
        
        
    def handleButton(self):
        print("hello world")

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
        sections = ("Number of loci", "Sampling Vector", "Initial deme sizes", "Initial migration matrix", "Time of change", "Deme sizes")
	
        output_file = open("alternative2_result.txt","w")
    
   
        for n in range(len(sections)): 
            layout.addWidget(QtGui.QLabel(sections[n]),n,0)
            self.line = QtGui.QLineEdit()
           
            layout.addWidget(self.line, n,1)
            output_file.write("# "+sections[n]+"\n")
            output_file.write(self.line.text())
            output_file.write("\n")

           

        self.gridGroupBox.setLayout(layout)
	
	

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    dialog = Dialog()
  
    
sys.exit(dialog.exec_())
