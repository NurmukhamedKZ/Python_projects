import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel,QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QCheckBox, QRadioButton, QButtonGroup, QLineEdit 
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer, QTime, Qt



class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0,0,0,0)
        self.time_label = QLabel("00:00:00:00", self)

        self.start_buttom = QPushButton("Start",self)
        self.stop_buttom = QPushButton("Stop",self)
        self.reset_buttom = QPushButton("Reset",self)
        
        self.timer = QTimer(self)
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("stop watch")
        self.setGeometry(650,250,660,400)
        self.setWindowIcon(QIcon("stuff/images.png"))

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        vbox.addWidget(self.start_buttom)
        vbox.addWidget(self.stop_buttom)
        vbox.addWidget(self.reset_buttom)
        self.setLayout(vbox)
        
        self.time_label.setAlignment(Qt.AlignCenter)
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_buttom)
        hbox.addWidget(self.stop_buttom)
        hbox.addWidget(self.reset_buttom)
        vbox.addLayout(hbox)
        

        
        
        # self.time_label.setStyleSheet("font-family: Arial;font-size: 100px;color: black; margin-top: 50px; ")
        
        self.setStyleSheet(""" 
                * {
                    background-color: #FCF6F6;
                    padding: 20px;
                    font-family: calibri;
                    font-weight: bold;
                }
                QPushButton{
                    background-color: #980110;
                    font-size: 50px;
                    border-radius: 10px;
                }
                QLabel{
                    font-size: 30px;
                    background-color: #FCF6F6;
                    border-radius: 10px;
                    color: black;
                    font-size: 100px;
                    
                    margin-top: 50px;
                }
                """)
        
        self.start_buttom.clicked.connect(self.start_time)
        self.stop_buttom.clicked.connect(self.stop_time)
        self.reset_buttom.clicked.connect(self.reset_time)
        self.timer.timeout.connect(self.update_display)

        

    
    def start_time(self):
        self.timer.start(10)
        
    
    def stop_time(self):
        self.timer.stop()
    
    def reset_time(self):
        self.timer.stop()
        self.time = QTime(0,0,0,0)
        self.time_label.setText(self.format_time(self.time))
        
    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}:{milliseconds:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))
        
    
def main():
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()