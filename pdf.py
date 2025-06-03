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
        masterLayout = QVBoxLayout() # Creates the layout
        self.btn = QPushButton("Select Files") # Creates the button
        self.btn.clicked.connect(self.getfile) # Assigns logic to button
        masterLayout.addWidget(self.btn) # Adds the button to the layout

        # Inner portion
        innerLayout = QHBoxLayout()
        self.list = QListView()
        innerLayout.addWidget(self.list)

        # Button layout
        buttonLayout = QVBoxLayout()
        self.upBtn = QPushButton("↑")
        # need button logic
        buttonLayout.addWidget(self.upBtn)
        self.downBtn = QPushButton("↓")
        # need button logic
        buttonLayout.addWidget(self.downBtn)
        innerLayout.addLayout(buttonLayout)
        
        
        
        masterLayout.addLayout(innerLayout)


        self.setLayout(masterLayout) # Sets layout
        self.setWindowTitle("PDFMergeSplit")


    def getfile(self):
        print("stupid")


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()

    app.exec_()

if __name__ == "__main__":
    main()