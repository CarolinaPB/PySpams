#First you need to install and configure PyQt4

from PyQt4 import QtCore, QtGui
import sys, csv

class Dialog(QtGui.QDialog):

    def __init__(self):
        super(Dialog, self).__init__()

        self.createHorizontalGroupBox()
        self.createGridGroupBox()
      

        buttonBox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        create_docBtn = QtGui.QPushButton("Create .txt")
        #create_docBtn.clicked.connect(self.create_txt)
        create_docBtn.clicked.connect(self.create_txt2)
        
      
     
        mainLayout = QtGui.QVBoxLayout()
        
        mainLayout.addWidget(self.horizontalGroupBox)
        mainLayout.addWidget(self.gridGroupBox)
        mainLayout.addWidget(create_docBtn)       
        mainLayout.addWidget(buttonBox)
       
   
	self.setGeometry(300, 300, 350, 300)

        self.setLayout(mainLayout)
        self.setWindowTitle("SPAms alternative")

    def create_txt2(self):
        sections = ("Number of loci", "Sampling Vector", "Initial deme sizes", "Initial migration matrix")
        sections2 =( "Time of change", "Deme sizes")
        ninput = ("numinput0", "numinput1", "numinput2", "numinput3", "numinput4")
        numinput0 = self.line0.text()
        numinput1 = self.line1.text()
        numinput2 = self.line2.text()
        numinput3 = self.line3.text()
        numinput4 = self.line4.text()
        
        filepath = QtGui.QFileDialog.getSaveFileName(self, 'Save file',"", '*.txt')
        fileHandle = open(filepath, "w")
        
        fileHandle.write(" #"+sections[0]+"\n")
        fileHandle.write(numinput0+"\n\n")
        fileHandle.write(" #"+sections[1]+"\n")
        fileHandle.write(numinput1+"\n\n")
        fileHandle.write(" #"+sections[2]+"\n")
        fileHandle.write(numinput2+"\n\n")
        fileHandle.write(" #"+sections[3]+"\n\n")
        #fileHandle.write( --> save matrix)
        fileHandle.write(" #"+sections2[0]+"\n")
        fileHandle.write(numinput3+"\n\n")
        fileHandle.write(" #"+sections2[1]+"\n")
        fileHandle.write(numinput4+"\n\n")
        
        
        fileHandle.close()



    #def create_txt (self):
     #   numinput = self.line0.text()
      #  outfile = open("sample.txt", "w")
       # outfile.write(numinput)
        #outfile.close()
        
    def new_window(self):
        self.wind.show()
    def new_gwindow(self):
        self.gwindow.show()

    def add_file(self):
        path = QtGui.QFileDialog.getOpenFileName(
                self, 'Upload File', '', 'CSV(*.csv)')

    
   
        
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
        for n in range(len(sections)): 
            layout.addWidget(QtGui.QLabel(sections[n]),n,0)
        
        self.line0 = QtGui.QLineEdit()   
        layout.addWidget(self.line0, 0,1)
        self.line1 = QtGui.QLineEdit()
        layout.addWidget(self.line1, 1,1)
        self.line2 = QtGui.QLineEdit()        
        layout.addWidget(self.line2, 2,1)
        self.line3 = QtGui.QLineEdit()        
        layout.addWidget(self.line3, 4,1)
        self.line4 = QtGui.QLineEdit()        
        layout.addWidget(self.line4, 5,1)

        

            #for i in range(2,5):
            #    self.line2 = QtGui.QLineEdit()
             #   self.line3 = QtGui.QLineEdit()
               # self.line4 = QtGui.QLineEdit()
              #  layout.addWidget(self.line2, 1, i )
                #layout.addWidget(self.line3, 2, i )
                #layout.addWidget(self.line4, 5, i )
        

        self.button_matr = QtGui.QPushButton("Matrix input")
        self.button_matr.clicked.connect(self.new_gwindow)
        self.gwindow = grid_window(self)
        layout.addWidget(self.button_matr,3,1)
        self.add_matr_btn = QtGui.QPushButton("Upload matrix")
        self.add_matr_btn.clicked.connect(self.add_file)
        layout.addWidget(self.add_matr_btn,3,2)
        
        
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
        self.matrix.setRowCount(100)
        self.matrix.setColumnCount(100)
        
        self.matrix.resizeColumnsToContents()
        self.matrix.resizeRowsToContents()
        glayout.addWidget(self.matrix, 0,0)
        for i in range (0,100):
            for j in range( 0, 100):
                self.matrix.setItem(i,j,QtGui.QTableWidgetItem("0."))
            
        self.buttonSave = QtGui.QPushButton('Save', self)
        self.buttonSave.clicked.connect(self.matrix_save)
        self.buttonSave.move(500,600)
        glayout.addWidget(self.buttonSave)

        self.buttonOpen = QtGui.QPushButton('Open', self)
        self.buttonOpen.clicked.connect(self.matrix_open)
        self.buttonOpen.move(400,600)
        glayout.addWidget(self.buttonOpen)

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
    def matrix_open(self):
        path = QtGui.QFileDialog.getOpenFileNames(
                self, 'Open File', '', '*.txt')
        if not path.isEmpty():
            with open(unicode(path), 'rb') as infile:
                self.matrix.setRowCount(0)
                self.matrix.setColumnCount(0)
                for rowdata in csv.reader(infile):
                    row = self.matrix.rowCount()
                    self.matrix.insertRow(row)
                    self.matrix.setColumnCount(len(rowdata))
                    for column, data in enumerate(rowdata):
                        item = QtGui.QTableWidgetItem(data.decode('utf8'))
                        self.matrix.setItem(row, column, item)
          	

def main():
    app = QtGui.QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(dialog.exec_())

if __name__ == '__main__':
    main()
