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

        # Button for toggling splitIntoIndividualPDFs
        toggleBtn = QToolButton()
        toggleBtn.setCheckable(True)
        toggleBtn.toggled.connect(self.toggleBtn)

        toggleWidget = QWidget()
        toggleLayout = QHBoxLayout(toggleWidget)
        toggleLayout.addWidget(toggleBtn)
        toggleLayout.addWidget(QLabel("Split into individual PDFs"))
        toggleLayout.setContentsMargins(0, 0, 0, 0) # Remove extra margins
        layout.addWidget(toggleWidget)

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
        # EDIT: Come back and create proper error message dialog box
        if (self.fileName == ""):
            print("no file selected")
        result = self.parseTextField()
        print(result)

        # Create the PDF object to read
        input = pypdf.PdfReader(self.fileName)

        # For each set of ranges, create and write a PDF
        if (self.splitIntoIndividual):
            for (start, end) in result:
                writer = pypdf.PdfWriter()
                with open(f"./extracted-pdf-{start}-{end}", 'w') as outputFile:
                    writer.append(fileobj=input, pages=(start,end))
                    writer.write(outputFile)
                writer.close()         
        else:
            writer = pypdf.PdfWriter()
            for (start, end) in result:
                with open(f"./extracted-pdf-{start}-{end}", 'w') as outputFile:
                    with pypdf.PdfWriter() as writer:
                        writer.append(fileobj=input, pages=(start,end))
            writer.write(outputFile)
            writer.close()


    # This function returns a list of tuples which represent all of the ranges
    # of pages to extract from the provded PDF
    def parseTextField(self):
        textFieldSplit = self.textbox.text().split(',')
        # EDIT: Come back and create proper error message dialog box
        if textFieldSplit[0] == '':
            print("womp womp")

        result = []

        for item in textFieldSplit:
            itemRange = item.split('-')
            # EDIT: Come back and create proper error message dialog box
            if len(itemRange) > 2:
                print("womp womp")
            elif len(itemRange) == 1:
                start = itemRange[0]
                end = start
            else:
                start = itemRange[0]
                end = itemRange[1]

            # EDIT: Come back and create proper error message dialog box
            if (start > end):
                print(f"invalid page range\nstart: {start}\nend: {end}")
            result.append((start,end))

        return result
    
    def toggleBtn(self, checked):
        if checked:
            self.splitIntoIndividual = True
        else:
            self.splitIntoIndividual = False