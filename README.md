# PDFMergeSplit
Desktop application for merging and splitting PDF documents with a graphical interface.

## Features

- **Merge Multiple PDFs**:
  - Combine several PDF files into a single document
  - Reorder files before merging

- **Split PDFs**:
  - Extract specific page ranges (e.g., 1-3,5,7-9)
  - Option to create individual PDFs for each page

- **User-Friendly Interface**:
  - Tab-based navigation
  - Drag-and-drop file selection
  - Visual feedback for operations

## Technologies Used

- **Core**:
  - Python 3.12.3
  - PyPDF (PDF manipulation library)
  
- **GUI Framework**:
  - PyQt5 (Qt5 bindings for Python)

## Installation

1. Ensure you have Python 3.12.3+ installed
2. Install dependencies:
   ```bash
   pip install pypdf PyQt5