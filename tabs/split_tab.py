import pypdf
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class SplitTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Tab-wide variables
        self.fileName = ""
        self.startPage = 0
        self.endPage = 0
        self.splitIntoIndividual = False
        self.setupUI()

    def setupUI(self):
        layout = QVBoxLayout()
        
        # Button to select which PDF to split
        self.btn = QPushButton("Select File")
        self.btn.clicked.connect(self.getFile)
        layout.addWidget(self.btn)

        # Field to hold file name
        self.fileField = QTextEdit()
        self.fileField.setReadOnly(True)
        layout.addWidget(self.fileField)

        # Fields to hold values for page numbers

        self.setLayout(layout)
    
    def getFile(self):
        # Open dialog and have the user select files
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setNameFilters(["PDF files (*.pdf)"])
        if dlg.exec_():
            self.fileName = dlg.selectedFiles()[0]
            self.fileField.setText(self.fileName)