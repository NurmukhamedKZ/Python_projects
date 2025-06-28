import datetime
import time as t
import pygame

def set_alarm(alarm_time: str):
    isrunning = True
    sound_path = "stuff/Webdriver Torso.mp3"
    while isrunning:
        print(datetime.datetime.now().strftime("%H:%M:%S"))
        t.sleep(1)
        if datetime.datetime.now().strftime("%H:%M:%S") == alarm_time:
            isrunning = False
            print(f"Wake up!!!")
            
            pygame.mixer.init()
            pygame.mixer.music.load(sound_path)
            pygame.mixer.music.play()
            
            while pygame.mixer.music.get_busy():
                t.sleep(1)
        
        
def main():
    user_alarm_time = input(f"enter time(HH:MM:SS): ")
    set_alarm(user_alarm_time)
    


if __name__ == "__main__":
    main()