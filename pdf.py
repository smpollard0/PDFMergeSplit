#!/usr/bin/python3
import pypdf
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

'''
This is a GUI program that allows the user to merge and split pdfs.
'''

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
        self.listView = QListView()
        innerLayout.addWidget(self.listView)

        # Button layout
        buttonLayout = QVBoxLayout()
        self.upBtn = QPushButton("↑")
        self.upBtn.clicked.connect(self.moveUp)
        buttonLayout.addWidget(self.upBtn)
        
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
        model = QStandardItemModel()

        # Open dialog and have the user select files
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setNameFilters(["PDF files (*.pdf)"])
        if dlg.exec_():
            for name in dlg.selectedFiles():
                self.fileNames.append(name)

        # This removes duplicates from the list
        self.fileNames = list(set(self.fileNames))

        print(self.fileNames)

        # Go through the selected files 

        for name in self.fileNames:
            item = QStandardItem(str(name))
            model.appendRow(item)

        self.listView.setModel(model)
        print("stupid")

    def moveUp(self):
        print("up")

    def moveDown(self):
        print("down")

    def merge(self):
        print("merge")


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()

    app.exec_()

if __name__ == "__main__":
    main()