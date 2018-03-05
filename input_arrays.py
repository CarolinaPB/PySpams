from PyQt4 import QtCore, QtGui
import sys
import numpy as np



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
    def run_once(func):
        def decorated(*args, **kwargs):
            try:
                return decorated._once_result
            except AttributeError:
                decorated._once_result = func(*args, **kwargs)
                return decorated._once_result
        return decorated

    @run_once
    def create_arrays(self):
        init_array = np.zeros((6,10),dtype=object)
        sect_array = np.array([["Number of loci"],["Sampling vector"],["Initial deme sizes"],["Initial migration matrix"],["Time of change"],["Deme sizes"]])
        sect_array = np.vstack(sect_array)
        total_array = np.hstack((sect_array,init_array))
        #print total_array
        return total_array
    

    def store_input(self):
        numinput0 = self.line0.text()
        numinput1 = self.line1.text()
        numinput2 = self.line2.text()
        numinput3 = self.line4.text()
        numinput4 = self.line5.text()
  
        
        m = open("matrix.txt","r")
        m2 = m.read()
        m3 = m2.replace(","," ")
        matrix = np.asarray(m3)
        global nonzeros
        nonzeros = np.count_nonzero(self.create_arrays()[:,1])
        print nonzeros

        if nonzeros == 0:
            global ncols
            ncols = 0
            self.create_arrays()[0,ncols+1] = numinput0
            self.create_arrays()[1,ncols+1] = numinput1  
            self.create_arrays()[2,ncols+1] = numinput2
            self.create_arrays()[3,ncols+1] = matrix
            self.create_arrays()[4,ncols+1] = numinput3
            self.create_arrays()[5,ncols+1] = numinput4
                
            print "working"
            ncols = ncols +1
            global final_array
            final_array = self.create_arrays()
            #print final_array
            return final_array
 
        else:
            print "ok"
        
            final_array[0,ncols+1] = numinput0
            final_array[1,ncols+1] = numinput1  
            final_array[2,ncols+1] = numinput2
            final_array[3,ncols+1] = matrix
            final_array[4,ncols+1] = numinput3
            final_array[5,ncols+1] = numinput4
            ncols = ncols +1
            
            #print final_array
            return final_array 
        
    def save_files(self):

        files_names=[]
        for i in range(0, ncols):
            files_names.append("input"+str(i)+".txt")

            with open(files_names[i], "w") as f:
                #for cols in range(1,ncols+1):
                for row in range(0,6):
                    f.write("# " + final_array[row,0])
                    f.write("\n")
                    f.write(final_array[row,i+1])
                    f.write("\n\n")
                               
        

        
        


def main():
    app = QtGui.QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(dialog.exec_())

if __name__ == '__main__':
    main()
