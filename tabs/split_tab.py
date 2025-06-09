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
        self.pdfsCreated = []
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

        # A widget to hold the toggle button
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
        if (self.fileName == ""):
            self.errorDialog("No PDF Selected")
            return
        # Create the PDF object to read
        input = pypdf.PdfReader(self.fileName)
        self.numPages = len(input.pages)
        result = self.parseTextField()
        if result == -1:
            return
        
        self.pdfsCreated.clear()

        # For each set of ranges, create and write a PDF
        if (self.splitIntoIndividual):
            for (start, end) in result:
                writer = pypdf.PdfWriter()
                writer.append(fileobj=input, pages=(start-1,end))
                outputFileName = f"./extracted-pdf-{start}-{end}.pdf"
                with open(outputFileName, 'wb') as outputFile:
                    writer.write(outputFile)
                    self.pdfsCreated.append(outputFileName)
                writer.close()         
        else:
            writer = pypdf.PdfWriter()
            outputFileName = f"./extracted-pdf-{min(start for start,_ in result)},{max(end for _,end in result)}.pdf"
            for (start, end) in result:
                writer.append(fileobj=input, pages=(start-1,end))
                with open(outputFileName, 'wb') as outputFile:
                    writer.write(outputFile)
            self.pdfsCreated.append(outputFileName)
            writer.close()

        # Throw up success dialog
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        successString = ""
        for name in self.pdfsCreated:
            successString += f"{name}\n"
        msg.setText(f"Split PDFs created\n{successString}")
        msg.setWindowTitle("Success")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()


    # This function returns a list of tuples which represent all of the ranges
    # of pages to extract from the provded PDF
    def parseTextField(self):
        textFieldSplit = self.textbox.text().split(',')
        # If the user didn't put a valid string in the text field
        # Every character in the textFieldSplit should either be an integer or a hyphen
        for word in textFieldSplit:
            for char in word:
                if (ord(char) < 48 or ord(char) > 57) and (char != '-'):
                    self.errorDialog(f"Invalid page range\nPage Range: {textFieldSplit}")
                    return -1
    

        result = []

        for item in textFieldSplit:
            itemRange = item.split('-')
            # If the user put something with multiple hyphens like 1-2-8 instead of 1-2,8
            if len(itemRange) > 2:
                self.errorDialog(f"Invalid page range: {itemRange}")
                return -1
            elif len(itemRange) == 1:
                start = int(itemRange[0])
                end = start
            else:
                start = int(itemRange[0])
                end = int(itemRange[1])

            # If the start or end are greater than the number of pages in the PDF
            if (start > self.numPages) or (end > self.numPages):
                self.errorDialog(f"Start or end greater than number of pages\nStart: {start}\nEnd: {end}\nNumber of Pages: {self.numPages}")
                return -1
            if (start > end):
                self.errorDialog(f"Invalid page range\nStart: {start}\nEnd: {end}")
                return -1
            result.append((int(start),int(end)))

        return result
    
    def toggleBtn(self, checked):
        if checked:
            self.splitIntoIndividual = True
        else:
            self.splitIntoIndividual = False

    def errorDialog(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(message)
        msg.setWindowTitle("FAILURE")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()