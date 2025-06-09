#!/usr/bin/python3
import pypdf
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from tabs.merge_tab import MergeTab
from tabs.split_tab import SplitTab

'''
This is a GUI program that allows the user to merge and split pdfs.
'''

class MainWindow(QWidget):
    def __init__(self, parent = None): # I don't entirely know what these two lines do
        super(MainWindow, self).__init__(parent)
        self.setupUI()

    def setupUI(self):
        mainLayout = QVBoxLayout(self)

        # Create tabs for splitting and merging
        self.tabs = QTabWidget()
        self.mergeTab = MergeTab()
        self.splitTab = SplitTab()

        # Add tabs to the main layout
        self.tabs.addTab(self.mergeTab, "Merge PDFs")
        self.tabs.addTab(self.splitTab, "Split PDF")

        mainLayout.addWidget(self.tabs)

        # self.setLayout(mainLayout) # Sets layout of entire window
        self.setWindowTitle("PDFMergeSplit")

def main():
    app = QApplication([])
    window = MainWindow()
    window.show()

    app.exec_()

if __name__ == "__main__":
    main()