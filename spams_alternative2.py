#To use this first you need to install and configure PyQt4
from PyQt4 import QtCore, QtGui
import sys


class Dialog(QtGui.QDialog):
    
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
  
        
    def new_window(self):
        self.wind.show()
  

    def createHorizontalGroupBox(self):
        self.horizontalGroupBox = QtGui.QGroupBox("Population dynamics")
        layout = QtGui.QHBoxLayout()
        models = ("Admixture model", "One population size change","Population structure")
        for m in models:
            button = QtGui.QPushButton(m)
            button.clicked.connect(self.new_window)
            self.wind = Second_W(self)
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
            for i in range(2,5):
                self.line2 = QtGui.QLineEdit()
                self.line3 = QtGui.QLineEdit()
                self.line4 = QtGui.QLineEdit()
                layout.addWidget(self.line2, 1, i )
                layout.addWidget(self.line3, 2, i )
                layout.addWidget(self.line4, 5, i )


            
            output_file.write("# "+sections[n]+"\n")
            output_file.write(self.line.text())
            output_file.write("\n")

           
        self.gridGroupBox.setLayout(layout)


class Second_W(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Second_W, self).__init__(parent)
        self.setGeometry(300, 300, 350, 300)
       
      	

def main():
    app = QtGui.QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(dialog.exec_())

if __name__ == '__main__':
    main()


