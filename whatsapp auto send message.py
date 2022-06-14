import time
import webbrowser as web
import pyautogui as pg
from pyautogui import size
from datetime import datetime

print("Program başlatıldı !")

tel=""# phone number
txt="Good Morning"
txt2="Goodnight"

def send():
    WIDTH, HEIGHT = size()
    web.open(f"https://web.whatsapp.com/send?phone={tel}&text={txt}")
    time.sleep(30)# How many seconds wait for the web page to open?
    pg.click(WIDTH / 2, HEIGHT / 2) #
    pg.press("enter")
    time.sleep(3)

def send2():
    WIDTH, HEIGHT = size()
    web.open(f"https://web.whatsapp.com/send?phone={tel}&text={txt2}")
    time.sleep(30)# How many seconds wait for the web page to open?
    pg.click(WIDTH / 2, HEIGHT / 2) #
    pg.press("enter")
    time.sleep(3)


while True:
    t = datetime.now()
    if t.hour == 6 and t.minute == 00: #time settings
        send()
        time.sleep(70)
        continue
    if t.hour == 23 and t.minute == 21:time settings
        send2()
        time.sleep(70)
        continue
