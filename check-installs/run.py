import sys
import os

import cv2
import pdf2image
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


if __name__ == "__main__":


    # test opencv
    # -----------

    parent = os.path.dirname(__file__)
    img_path = parent + "/image.jpg"
    img = cv2.imread(img_path)
    cv2.imshow("OpenCV works", img)
    print("✅ OpenCV works!")


    # test some libs with system deps
    # -------------------------------

    import pytesseract
    print("✅ tesseract works!")

    import camelot
    print("✅ camelot works!")

    import PyPDF2
    print("✅ PyPDF2 works!")
    
    import pdf2image
    print("✅ pdf2image works!")


    # test qt
    # -------

    app = QApplication(sys.argv)

    # Build the window widget
    w = QWidget()
    w.setGeometry(300, 300, 250, 150)  # x, y, w, h
    w.setWindowTitle("QT works")

    # Add a label with tooltip
    label = QLabel("QT works! =)", w)
    label.resize(label.sizeHint())
    label.move(80, 50)

    # Show window and run
    w.show()
    print("✅ QT works!")
    app.exec_()
