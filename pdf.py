#!/usr/bin/python3
import pypdf
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

'''
This is a GUI program that allows the user to merge and split pdfs.
'''

def swap(index1, index2, listLike):
    listLike[index1], listLike[index2] = listLike[index2], listLike[index1]

class MainWindow(QWidget):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        # Program-wide variables
        self.fileNames = []

        masterLayout = QVBoxLayout() # Creates the layout
        self.btn = QPushButton("Select Files") # Creates the button
        self.btn.clicked.connect(self.getFile) # Assigns logic to button
        masterLayout.addWidget(self.btn) # Adds the button to the layout

        # Inner layout
        innerLayout = QHBoxLayout()
        self.listWidget = QListWidget()
        innerLayout.addWidget(self.listWidget)

        # Button layout
        buttonLayout = QVBoxLayout()
        self.upBtn = QPushButton("↑")
        self.upBtn.clicked.connect(self.moveUp)
        buttonLayout.addWidget(self.upBtn)

        self.deleteBtn = QPushButton("X")
        self.deleteBtn.clicked.connect(self.deleteEntry)
        buttonLayout.addWidget(self.deleteBtn)
        
        self.downBtn = QPushButton("↓")
        self.downBtn.clicked.connect(self.moveDown)
        buttonLayout.addWidget(self.downBtn)
        innerLayout.addLayout(buttonLayout)
        
        masterLayout.addLayout(innerLayout)

        self.mergeBtn = QPushButton("Merge PDFs")
        self.mergeBtn.clicked.connect(self.merge)
        masterLayout.addWidget(self.mergeBtn)

        self.setLayout(masterLayout) # Sets layout of entire window
        self.setWindowTitle("PDFMergeSplit")

    def getFile(self):
        # Open dialog and have the user select files
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setNameFilters(["PDF files (*.pdf)"])
        if dlg.exec_():
            for name in dlg.selectedFiles():
                self.fileNames.append(name)

        # This removes duplicates from the list
        self.fileNames = list(set(self.fileNames))

        # Go through the selected files
        self.listWidget.clear() # Clear the list widget
        for name in self.fileNames:
            self.listWidget.addItem(name)

    def moveUp(self):
        row = self.listWidget.row(self.listWidget.selectedItems()[0])
        if row > 0:
            swap(row,row-1,self.fileNames)
            item = self.listWidget.takeItem(row)
            self.listWidget.insertItem(row - 1, item)
            self.listWidget.setCurrentRow(row - 1)

    def moveDown(self):
        row = self.listWidget.row(self.listWidget.selectedItems()[0])
        if row < self.listWidget.count()-1:
            swap(row,row+1,self.fileNames)
            item = self.listWidget.takeItem(row)
            self.listWidget.insertItem(row + 1, item)
            self.listWidget.setCurrentRow(row + 1)

    def merge(self):
        merger = pypdf.PdfWriter()

        for pdf in self.fileNames:
            merger.append(pdf)

        merger.write("merged-pdf.pdf")
        merger.close()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Merged PDF created merged-pdf.pdf")
        msg.setWindowTitle("Success")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def deleteEntry(self):
        selectedItems = self.listWidget.selectedItems()
        for item in selectedItems:
            self.listWidget.takeItem(self.listWidget.row(item))

def main():
    app = QApplication([])
    window = MainWindow()
    window.show()

    app.exec_()

if __name__ == "__main__":
    main()