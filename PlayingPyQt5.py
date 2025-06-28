import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel,QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QCheckBox, QRadioButton, QButtonGroup, QLineEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Alarm clock")
        self.setGeometry(650,250,600,500)
        self.setWindowIcon(QIcon("stuff/images.png"))

        # self.button = QPushButton("Click me pupsik", self)     
        # self.checkbox = QCheckBox("are you cool?", self)  
        
        # self.pixmap = QPixmap("stuff/Волонтеры ОМК.jpg")
        
        self.text1 = QLabel(self) 
        # label1.setFont(QFont("Arial", 40))
        self.label1 = QLabel(self)
        
        
        self.radio1 = QRadioButton("Info", self)
        self.radio2 = QRadioButton("Phys", self)
        self.radio3 = QRadioButton("Geo", self)
        self.radio4 = QRadioButton("Math", self)
        self.radio5 = QRadioButton("English", self)

        
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)
        
        self.button1 = QPushButton("confirm",self)
        
        self.line_edit = QLineEdit(self)
        self.initUI()
        
    def initUI(self):
        
        # self.radio1.setGeometry(0,0,100,30)
        # self.radio2.setGeometry(0,30,100,30)
        # self.radio3.setGeometry(0,60,100,30)
        # self.radio4.setGeometry(60,0,100,30)
        # self.radio5.setGeometry(60,30,100,30)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        gbox = QGridLayout()
        gbox.addWidget(self.radio1,0,0)
        gbox.addWidget(self.radio2,1,0)
        gbox.addWidget(self.radio3,2,0)
        gbox.addWidget(self.radio4,0,1)
        gbox.addWidget(self.radio5,1,1)
        
        central_widget.setLayout(gbox)
        
        
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)
        
        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)
        
        
        
        self.cnt = 0
        self.user_choice1 = False
        self.user_choice2 = False
        
        self.button1.setGeometry(30,95, 60,35)
        self.button1.clicked.connect(self.on_click)
        
        self.line_edit.setGeometry(130,0,300,50)
        self.line_edit.setStyleSheet("font-size:20px; font-family: Arial; background-color: #F0F0F0; border: 1px solid black")
        self.line_edit.editingFinished.connect(self.text_edited)
        
        self.setStyleSheet("""
            QRadioButton{
                font-size: 30px;
                color: blue;
                
                background-color: white;
                
            }    
        
        
        """)
    
    
    def radio_button_changed(self):
        radio_button = self.sender()
        
        if not radio_button.isChecked():
            return  
        

        if radio_button.text() in {"Info","Phys", "Geo"}:
            self.user_choice1 = radio_button.text()
            self.cnt += 1
        elif radio_button.text() in {"Math", "English"}:
            self.user_choice2 = radio_button.text()
            self.cnt += 1
          
        print(self.cnt)  
        if self.user_choice1 or self.user_choice2:
            print(self.user_choice1, self.user_choice2)   


    def on_click(self):
        if self.user_choice1 and self.user_choice2:
            self.label1.setGeometry(0,0,120,90)
            self.label1.setStyleSheet("background-color: white;")
            self.text1.setText(f"you chose {self.user_choice1} and {self.user_choice2}")
            self.text1.setGeometry(20,130, 200,35)
        else:
            self.text1.setText("choose the couple!")
            self.text1.setGeometry(20,130, 200,35)
        
    def text_edited(self):
        text = self.line_edit.text()
        print(f'your text "{text}"')

    
    # def on_check(self, state):
    #     if state == Qt.Checked:
    #         print("you are cool")
    #     else:
    #         print("you are not cool(")
        
        
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()