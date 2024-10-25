from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import subprocess   
import threading

class Ui_Form(object):
    def setupUi(self, Form):
        Form.resize(696, 481)
        self.horizontalLayoutWidget = QWidget(Form)

        self.horizontalLayoutWidget.setGeometry(QRect(9, 9, 681, 461))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)

        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout = QVBoxLayout()

        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.label_2 = QLabel(self.horizontalLayoutWidget)

        self.label_2.setScaledContents(False)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.horizontalLayoutWidget)

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout_2 = QHBoxLayout()

        self.horizontalLayout_2.setContentsMargins(12, 12, 12, 12)
        self.button_amplitude_time = QPushButton(self.horizontalLayoutWidget)


        self.horizontalLayout_2.addWidget(self.button_amplitude_time)

        self.horizontalLayout_5 = QHBoxLayout()


        self.horizontalLayout_2.addLayout(self.horizontalLayout_5)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.label_4 = QLabel(self.horizontalLayoutWidget)


        self.verticalLayout.addWidget(self.label_4)

        self.horizontalLayout_4 = QHBoxLayout()

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)

        self.verticalLayout_2.setContentsMargins(12, 12, 12, 12)
        self.button_basic = QPushButton(self.horizontalLayoutWidget)


        self.verticalLayout_2.addWidget(self.button_basic)

        self.button_logarithmic = QPushButton(self.horizontalLayoutWidget)


        self.verticalLayout_2.addWidget(self.button_logarithmic)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()

        self.verticalLayout_3.setContentsMargins(12, 12, 12, 12)
        self.button_sigmoid = QPushButton(self.horizontalLayoutWidget)


        self.verticalLayout_3.addWidget(self.button_sigmoid)

        self.button_bar_graph = QPushButton(self.horizontalLayoutWidget)


        self.verticalLayout_3.addWidget(self.button_bar_graph)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        self.button_amplitude_time.clicked.connect(self.amplitude_time)
        self.button_basic.clicked.connect(self.basic)
        self.button_logarithmic.clicked.connect(self.logarithmic)
        self.button_sigmoid.clicked.connect(self.sigmoid)
        self.button_bar_graph.clicked.connect(self.bar_graph)


    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; text-decoration: underline;\">Audio Visualisers<br/></span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">1- Amplitude Time</span></p></body></html>", None))

        self.button_amplitude_time.setText(QCoreApplication.translate("Form", u"  Amplitude Time ", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">    2 - Amplitude - Frequency</span></p></body></html>", None))
        self.button_basic.setText(QCoreApplication.translate("Form", u"Basic Normalisation", None))
        self.button_logarithmic.setText(QCoreApplication.translate("Form", u"Logarithmic Normalisation", None))
        self.button_sigmoid.setText(QCoreApplication.translate("Form", u"Logarithmic Sigmoid Normalisation", None))
        self.button_bar_graph.setText(QCoreApplication.translate("Form", u"Bar Graph Visualiser", None))
    # retranslateUi

    def run(self,command):
        def target():
            try:
                subprocess.run(command.split(), capture_output=True, text=True)
            except subprocess.CalledProcessError as e:
                print(f"Error: {e}")
        thread = threading.Thread(target=target)
        thread.start()

    def amplitude_time(self):
        self.run("python.exe final-amplitude-time.py")

    def basic(self):
        self.run("python.exe final-basic.py")
        
    def logarithmic(self):
        self.run("python.exe final-logarithmic.py")
    
    def sigmoid(self):
        self.run("python.exe final-sigmoid.py")

    def bar_graph(self):
        self.run("python.exe final-bar-graph.py")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)    
        self.setWindowTitle("Menu")
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

