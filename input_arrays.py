from PyQt4 import QtCore, QtGui
import sys
import numpy as np
#from teste import save_file
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
        

        self.input_btn = QtGui.QPushButton("Save input")
        self.input_btn.clicked.connect(self.store_input)
        self.file_input = QtGui.QPushButton("Save doc")
        self.file_input.clicked.connect(self.save_files)
        mainLayout.addWidget(self.input_btn)
        mainLayout.addWidget(self.file_input)
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
        
        #m_array = np.zeros((6, 1),dtype=object)
        #narray0 = np.zeros((6,1),dtype=object)
        

        init_array = np.zeros((6,10),dtype=object)
        sect_array = np.array([["Number of loci"],["Sampling vector"],["Initial deme sizes"],["Initial migration matrix"],["Time of change"],["Deme sizes"]])
        sect_array = np.vstack(sect_array)
        total_array = np.hstack((sect_array,init_array))
        #print total_array

        numinput0 = self.line0.text()
        numinput1 = self.line1.text()
        numinput2 = self.line2.text()
        numinput3 = self.line4.text()
        numinput4 = self.line5.text()
  

        m = open("matrix.txt","r")
        m2 = m.read()
        m3 = m2.replace(","," ")
        matrix = np.asarray(m3)
        
        ncols = 0
        ncols = ncols +1
        #while loop
        total_array[0,ncols+1] = numinput0
        total_array[1,ncols+1] = numinput1  
        total_array[2,ncols+1] = numinput2
        total_array[3,ncols+1] = matrix
        total_array[4,ncols+1] = numinput3
        total_array[5,ncols+1] = numinput4
        print total_array     
        return total_array
            

        m_array2 = np.array([[numinput0],[numinput1],[numinput2],[matrix],[numinput3],[numinput4]])
      
        #num_rows, num_cols = m_array2.shape
        ## wrong because num_cols of m_array2 is always = 1
        #print num_cols
        
        #if num_cols == 1:
         #   narray = np.hstack((narray0,m_array2))
          #  narray=np.hstack((narray,m_array2))
           # narray = narray[:,1:]
            #print "empty"
       # else:
        #    narray=np.hstack((narray,m_array2)) 
         #   print "working"
        	
        #return narray
       
        
        
    def save_files(self):
        #num_rows, num_cols = self.store_input().shape

        files_names=[]
        for i in range(0,10):
            files_names.append("input"+str(i)+".txt")
            
            with open(files_names[0],"w") as f:
                for n in range(0,6):
                    f.write("# " + self.store_input()[n,0])
                    f.write("\n")
                    f.write(self.store_input()[n,1])
                    f.write("\n\n")
        

        
        


def main():
    app = QtGui.QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(dialog.exec_())

if __name__ == '__main__':
    main()
