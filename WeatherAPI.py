import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel,QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QCheckBox, QRadioButton, QButtonGroup, QLineEdit 
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt



class WeatherAPP(QWidget):
    def __init__(self):
        super().__init__()
        
        self.city_label = QLabel("Enter city name:", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get weather", self)
        self.temp = QLabel("",self)
        self.emoji_label = QLabel("", self)
        self.description_label = QLabel("", self)
        
        self.initUI()
        
    
    def initUI(self):
        self.setWindowTitle("Weather APP")
        self.setGeometry(750,150,450,600)
        self.setWindowIcon(QIcon("stuff/images.png"))
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temp)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        self.setLayout(vbox)
        
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temp.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        
        self.city_label.setObjectName("city_label")
        self.temp.setObjectName("temp")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        
        self.setStyleSheet("""
            * {
                font-size: 30px;
                font-family: calibri;
                font-weight: bold;
            }                           
            QPushButton{
                color: #50a7bf;
            }            
            QLabel#city_label{
                font-style: italic;
            }
            QLabel#temp{
                font-size: 60px;
            }     
            QLabel#emoji_label{
                font-size: 80px;
                font-family: Segoe UI emoji;
            }        
            QLabel#description_label{
                font-size:50px;
            }
            """)
        
        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = "e3803a006cc1312498da05884bd41764"
        city_name = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
        try:
            response = requests.get(url)
            data = response.json()
            if data["cod"] == 200:
                self.display_weather(data)
            else:
                self.display_error(data["cod"])
        except requests.exceptions.ConnectionError:
            self.display_error("Connection error")
        except requests.exceptions.Timeout:
            self.display_error("Timeout error")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request error {req_error}")
            
    def display_error(self, error):
        if error == "404":
            self.temp.setText(f"enter a correct name")
            self.temp.setStyleSheet("font-size: 40px")
            self.emoji_label.setText("")
            self.description_label.setText("")
        else:
            self.temp.setText(f"{error}")   
            self.temp.setStyleSheet("font-size: 40px")  
             
    def display_weather(self, data):
        celsius = int(data["main"]["temp"]-273)
        self.temp.setText(f"{celsius}°C")
        self.description_label.setText(data["weather"][0]["description"])
        
        if celsius > 35:
            self.emoji_label.setText("🥵")
        elif celsius > 20:
            self.emoji_label.setText("😌")
        elif celsius > 0:
            self.emoji_label.setText("🤧")
        elif celsius <= 0:
            self.emoji_label.setText("🥶")
        
        self.temp.setStyleSheet("font-size: 60px")
        
    
def main():
    app = QApplication(sys.argv)
    weatherAPP = WeatherAPP()
    weatherAPP.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()