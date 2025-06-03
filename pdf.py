#!/usr/bin/python3
import pypdf
from PyQt5.QtWidgets import QApplication, QLabel

'''
This is a GUI program that allows the user to merge and split pdfs.
'''


def main():
    app = QApplication([])

    label = QLabel('Hello world!')
    label.show()

    app.exec_()

if __name__ == "__main__":
    main()