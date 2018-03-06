#First you need to install and configure PyQt4

from PyQt4 import QtCore, QtGui
import sys, csv
import numpy as np


class Dialog(QtGui.QDialog):

    def __init__(self):
        super(Dialog, self).__init__()
        
        mainLayout = QtGui.QVBoxLayout()

        self.createHorizontalGroupBox()
        self.createGridGroupBox()
        mainLayout.addWidget(self.horizontalGroupBox)
        mainLayout.addWidget(self.gridGroupBox)
      

        buttonBox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        
        self.input_btn = QtGui.QPushButton("Save input")
        self.input_btn.clicked.connect(self.store_input)

        self.file_input = QtGui.QPushButton("Save doc")
        self.file_input.clicked.connect(self.save_files)
        
        
        mainLayout.addWidget(self.input_btn)
        mainLayout.addWidget(self.file_input)
        mainLayout.addWidget(buttonBox)
       
   
	self.setGeometry(300, 300, 350, 300)

        self.setLayout(mainLayout)
        self.setWindowTitle("SPAms alternative")

    
    def new_matrix2(checked):
        global path_open3
        if checked:
            path = QtGui.QFileDialog.getOpenFileName(None, 'Upload File', '', '*.txt')
            path_open = open(path)
            path_open2 = path_open.read()
            path_open3 = path_open2.replace(","," ")
      
            print "working"
        
    def new_window(self):
        self.wind.show()
    def new_gwindow(self):
        self.gwindow.show()

        
#creates the buttons for the models and opens a window when you click them
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

#creates grid layout with several fields to fill | creates a file with the fields' headers 
    def createGridGroupBox(self):
        self.gridGroupBox = QtGui.QGroupBox("Options")
        layout = QtGui.QGridLayout()
            
        sections = ("Number of loci", "Sampling Vector", "Initial deme sizes","Initial migration matrix", "Time of change", "Deme sizes")       

        layout.addWidget(QtGui.QLabel(sections[0]),0,0)
        layout.addWidget(QtGui.QLabel(sections[1]),1,0)
        layout.addWidget(QtGui.QLabel(sections[2]),2,0)
        layout.addWidget(QtGui.QLabel(sections[3]),3,0) 
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
        


        self.button_matr = QtGui.QPushButton("Create matrix")
        self.button_matr.clicked.connect(self.new_gwindow)
        self.gwindow = grid_window(self)
        layout.addWidget(self.button_matr,3,1)
 

        matr_checkbox = QtGui.QCheckBox("Add matrix", self)
        matr_checkbox.stateChanged.connect(self.new_matrix2)
        layout.addWidget(matr_checkbox, 4,0)
                
        
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
  
        global nonzeros
        nonzeros = np.count_nonzero(self.create_arrays()[:,1])
        print nonzeros

        if nonzeros == 0:
            global ncols
            ncols = 0
            self.create_arrays()[0,ncols+1] = numinput0
            self.create_arrays()[1,ncols+1] = numinput1  
            self.create_arrays()[2,ncols+1] = numinput2
            self.create_arrays()[3,ncols+1] = path_open3
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
            final_array[3,ncols+1] = path_open3
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

      
class Second_W(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Second_W, self).__init__(parent)
        self.setGeometry(300, 300, 350, 300)

        

class grid_window(QtGui.QMainWindow):
    def __init__(self, parent):
        super(grid_window, self).__init__(parent)
        self.setGeometry(600, 300, 600, 630)
        
        glayout=QtGui.QGridLayout()
        self.setWindowTitle("Matrix input")
      

#table inside the new window created with the button_matr
        self.matrix = QtGui.QTableWidget(self)
        self.matrix.resize(600,600)
        self.matrix.setRowCount(25)
        self.matrix.setColumnCount(25)
        
        self.matrix.resizeColumnsToContents()
        self.matrix.resizeRowsToContents()
        glayout.addWidget(self.matrix, 0,0)
        for i in range (0,25):
            for j in range( 0, 25):
                self.matrix.setItem(i,j,QtGui.QTableWidgetItem("0."))
            
        self.buttonSave = QtGui.QPushButton('Save', self)
        self.buttonSave.clicked.connect(self.matrix_save)
        self.buttonSave.move(500,600)
        glayout.addWidget(self.buttonSave)

        

#function to save matrix as new txt file
    def matrix_save(self):
        path = QtGui.QFileDialog.getSaveFileName(
                self, 'Save File', '', '*.txt')
        if not path.isEmpty():
            with open(unicode(path), 'wb') as stream:
                writer = csv.writer(stream)
                for row in range(self.matrix.rowCount()):
                    rowdata = []
                    for column in range(self.matrix.columnCount()):
                        item = self.matrix.item(row, column)
                        if item is not None:
                            rowdata.append(
                                unicode(item.text()).encode('utf8'))
                        else:
                            rowdata.append('')
                    writer.writerow(rowdata)
    
          	

def main():
    app = QtGui.QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(dialog.exec_())

if __name__ == '__main__':
    main()
