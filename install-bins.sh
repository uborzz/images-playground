#!/bin/bash

# Install Python 3, PyQt5
sudo apt-get update
sudo apt-get install -y python3-pyqt5

# Install additional PyQt5 packages
sudo apt-get install -y python3-pyqt5.qtopengl 
sudo apt-get install -y python3-pyqt5.qtquick 
sudo apt-get install -y python3-pyqt5.qtmultimedia 

# Install Qm
sudo apt-get install -y qmlscene 
sudo apt-get install -y qml-module-qtqml* 
sudo apt-get install -y qml-module-qtquick* 
sudo apt-get install -y qml-module-qmltermwidget 
sudo apt-get install -y qml-module-qt-websockets 
sudo apt-get install -y qml-module-qt3d 
sudo apt-get install -y qml-module-qtaudioengine 
sudo apt-get install -y qml-module-qtav 
sudo apt-get install -y qml-module-qtbluetooth 
sudo apt-get install -y qml-module-qtcharts 
sudo apt-get install -y qml-module-qtdatavisualization 
sudo apt-get install -y qml-module-qtgraphicaleffects 
sudo apt-get install -y qml-module-qtgstreamer 
sudo apt-get install -y qml-module-qtlocation 
sudo apt-get install -y qml-module-qtmultimedia 
sudo apt-get install -y qml-module-qtpositioning 

# Libraries for multimedia
sudo apt-get install -y libqt5multimedia5-plugins 
sudo apt-get install -y gstreamer1.0-libav 
sudo apt-get install -y gstreamer1.0-alsa 
sudo apt-get install -y gstreamer1.0-plugins-bad 
sudo apt-get install -y gstreamer1.0-plugins-base 
sudo apt-get install -y gstreamer1.0-plugins-base-apps 
sudo apt-get install -y gstreamer1.0-plugins-good 
sudo apt-get install -y gstreamer1.0-plugins-ugly 
sudo apt-get install -y alsa-base 
sudo apt-get install -y alsa-utils

# pdfs and images
sudo apt-get install -y python3-tk ghostscript
sudo apt-get install -y poppler-utils

# tesseract
sudo apt-get install -y tesseract-ocr
