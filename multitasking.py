import threading
import datetime as dt
import time as t

def time_now():
    while True:
        now = dt.datetime.now().strftime("%H:%M:%S")
        print(now)
        t.sleep(1)
        
        if now == "18:10:40":
            break

def get_mail():
    t.sleep(2)
    print(f"you get the mail")
    
chore1 = threading.Thread(target=time_now)
chore1.start()

chore2 = threading.Thread(target=get_mail)
chore2.start()