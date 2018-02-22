import sys, csv
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MainW (QDialog):
    def __init__(self, parent=None):
        super(MainW,self).__init__(parent)

        mainlayout = QVBoxLayout()
        #self.setLayout(mainlayout)
        self.setWindowTitle("Spams Alternative")
        self.setGeometry(600, 300, 500, 300)

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        

        self.tabs = QTabWidget()
        self.tabs.tab1 = QWidget()
        self.tabs.tab2 = QWidget()
        self.tabs.tab3 = QWidget()

        self.tabs.addTab(self.tabs.tab1,"Admixture model")
        self.tabs.addTab(self.tabs.tab2,"One pop. size change")
        self.tabs.addTab(self.tabs.tab3,"Population structure")

        self.tab1_w()
        
        
        mainlayout.addWidget(self.tabs)
        mainlayout.addWidget(buttonBox)
        self.setLayout(mainlayout)

    def g_window(self):
        self.gwindow.show()

    def tab1_w (self):
        layout = QGridLayout()

        def funct_chbox (state):
            if state == Qt.Checked:
                matr_path = QFileDialog.getOpenFileName(None, 'Upload File', '', '*.txt')
                layout.addWidget(QLabel(matr_path), 4,1)
                layout.addWidget(QLabel(sections[4]),5,0)
                self.line4 = QLineEdit()   
                layout.addWidget(self.line4, 5,1)
                layout.addWidget(QLabel(sections[5]),6,0)       
                self.line5 = QLineEdit()
                layout.addWidget(self.line5,6,1)
        def new_chbox(state):
            if state ==Qt.Checked:
                matr_chbox2 = QCheckBox(" Choose matrix")
                layout.addWidget(matr_chbox2,7,0)
                matr_chbox2.stateChanged.connect(funct_chbox)
        

        sections = ("Number of loci", "Sampling Vector", "Initial deme sizes","Initial migration matrix", "Time of change", "Deme sizes")   
        layout.addWidget(QLabel(sections[0]),0,0)
        layout.addWidget(QLabel(sections[1]),1,0)
        layout.addWidget(QLabel(sections[2]),2,0)
        layout.addWidget(QLabel(sections[3]),3,0) 
        #layout.addWidget(QLabel(sections[4]),5,0)
        #layout.addWidget(QLabel(sections[5]),6,0)

        self.line0 = QLineEdit()   
        layout.addWidget(self.line0, 0,1)
        self.line1 = QLineEdit()
        layout.addWidget(self.line1, 1,1)
        self.line2 = QLineEdit()        
        layout.addWidget(self.line2, 2,1)
        #self.line4 = QLineEdit()        
        #layout.addWidget(self.line4, 5,1)
        #self.line5 = QLineEdit()        
        #layout.addWidget(self.line5, 6,1)


        self.button_matr = QPushButton("Create matrix")
        self.button_matr.clicked.connect(self.g_window)
        self.gwindow = grid_window(self)
        layout.addWidget(self.button_matr,3,1)
        self.button_doc = QPushButton("Save .txt")
        
        layout.addWidget(self.button_doc,15,1)

        

        matr_checkbox = QCheckBox(" Choose matrix")
        matr_checkbox.stateChanged.connect(funct_chbox)
        matr_checkbox.stateChanged.connect(new_chbox)
        layout.addWidget(matr_checkbox, 4,0)
        

        
        self.tabs.tab1.setLayout(layout)
       
        
        
class grid_window(QMainWindow):
    def __init__(self, parent):
        super(grid_window, self).__init__(parent)
        self.setGeometry(600, 300, 600, 630)
        
        glayout=QGridLayout()
        self.setWindowTitle("Matrix input")
      

#table inside the new window created with the button_matr
        self.matrix = QTableWidget(self)
        self.matrix.resize(600,600)
        self.matrix.setRowCount(25)
        self.matrix.setColumnCount(25)
        
        self.matrix.resizeColumnsToContents()
        self.matrix.resizeRowsToContents()
        glayout.addWidget(self.matrix, 0,0)
        for i in range (0,25):
            for j in range( 0, 25):
                self.matrix.setItem(i,j,QTableWidgetItem("0."))
            
        self.buttonSave = QPushButton('Save', self)
        self.buttonSave.clicked.connect(self.matrix_save)
        self.buttonSave.move(500,600)
        glayout.addWidget(self.buttonSave)

        
    def matrix_save(self):
        path = QFileDialog.getSaveFileName(
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

        



app = QApplication(sys.argv)
mainw = MainW()
mainw.show()
app.exec_()
