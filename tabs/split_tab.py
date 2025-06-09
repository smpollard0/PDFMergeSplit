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
        self.numPages = 0
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
        
        instructions = QLabel(
            "Specify page ranges to extract\n"
            "Example: 1-3,5,7-9"
        )
        instructions.setWordWrap(True)
        layout.addWidget(instructions)

        # Textbox for page ranges
        self.textbox = QLineEdit()
        self.textbox.setPlaceholderText("Enter page range...")
        self.textbox.setMaximumWidth(200)
        self.textbox.setReadOnly(False)

        layout.addWidget(self.textbox)


        # Split PDF button
        self.splitBtn = QPushButton("Split PDF")
        self.splitBtn.clicked.connect(self.splitPDF)
        layout.addWidget(self.splitBtn)
        self.setLayout(layout)
    
    def getFile(self):
        # Open dialog and have the user select files
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setNameFilters(["PDF files (*.pdf)"])
        if dlg.exec_():
            self.fileName = dlg.selectedFiles()[0]
            self.fileField.setText(self.fileName)

    def splitPDF(self):
        result = self.parseTextField()

        print("split")

    def parseTextField(self):

        print("parsed")