#First you need to install and configure PyQt4

from PyQt4 import QtCore, QtGui
import sys, csv
import numpy as np
from teste import save_file

class Dialog(QtGui.QDialog):

    def __init__(self):
        super(Dialog, self).__init__()

        self.createHorizontalGroupBox()
        self.createGridGroupBox()
      

        buttonBox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        create_docBtn = QtGui.QPushButton("Create .txt")
        create_docBtn.clicked.connect(self.create_txt2)
        create_docBtn.clicked.connect(self.save_file2)
        
      
     
        mainLayout = QtGui.QVBoxLayout()
        
        mainLayout.addWidget(self.horizontalGroupBox)
        mainLayout.addWidget(self.gridGroupBox)
        mainLayout.addWidget(create_docBtn)       
        mainLayout.addWidget(buttonBox)
       
   
	self.setGeometry(300, 300, 350, 300)

        self.setLayout(mainLayout)
        self.setWindowTitle("SPAms alternative")


       

    def save_file2(self):

        numinput0 = self.line0.text()
        numinput1 = self.line1.text()
        numinput2 = self.line2.text()
        numinput3 = self.line4.text()
        numinput4 = self.line5.text()
        m_array = np.zeros((3,3))
        m_array[0,0] = numinput0
        m_array[1,0] = numinput1
        m_array[2,0] = numinput2
        matr_array = np.genfromtxt("matrix.txt",delimiter = ",")
        m_array2 = np.zeros((2,3))
        m_array2[0,0] = numinput3
        m_array2[1,0] = numinput4
        #final_array = np.vstack((m_array, matr_array, m_array2))
        final_array = np.vstack((m_array, m_array2))
        save_file(final_array)
  
        

    
    def new_matrix2(checked):
        global path_open3
        if checked:
            path = QtGui.QFileDialog.getOpenFileName(None, 'Upload File', '', '*.txt')
            path_open = open(path)
            path_open2 = path_open.read()
            path_open3 = path_open2.replace(","," ")

            print "working"


    def create_txt2(self):
        sections = ("Number of loci", "Sampling Vector", "Initial deme sizes", "Initial migration matrix")
        sections2 =( "Time of change", "Deme sizes")
        ninput = ("numinput0", "numinput1", "numinput2", "numinput3", "numinput4")

        numinput0 = self.line0.text()
        numinput1 = self.line1.text()
        numinput2 = self.line2.text()
        numinput3 = self.line4.text()
        numinput4 = self.line5.text()

        
        
        
        filepath = QtGui.QFileDialog.getSaveFileName(self, 'Save file',"", '*.txt')
        fileHandle = open(filepath, "w")
        
        fileHandle.write("# "+sections[0]+"\n")
        fileHandle.write(numinput0+"\n\n")
        fileHandle.write("# "+sections[1]+"\n")
        fileHandle.write(numinput1+"\n\n")
        fileHandle.write("# "+sections[2]+"\n")
        fileHandle.write(numinput2+"\n\n")
        fileHandle.write("# "+sections[3]+"\n")
        for line in path_open3:
            fileHandle.write(line)
        fileHandle.write("\n")
        fileHandle.write("# "+sections2[0]+"\n")
        fileHandle.write(numinput3+"\n\n")
        fileHandle.write("# "+sections2[1]+"\n")
        fileHandle.write(numinput4+"\n\n")
        
        
        fileHandle.close()
       

        
    def new_window(self):
        self.wind.show()
    def new_gwindow(self):
        self.gwindow.show()

    def add_file(self):
        path = QtGui.QFileDialog.getOpenFileName(
                self, 'Upload File', '', '*.txt')
    
        
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