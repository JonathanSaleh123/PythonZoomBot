import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime


def login(meetid, pwd):
    #Logins to the app
    subprocess.call(["/usr/bin/open", "/Applications/zoom.us.app"])
    
    time.sleep(10)
    
    join_btn = pyautogui.locateCenterOnScreen('zoomIcon.png')
    pyautogui.moveTo(join_btn) #Move Cursor to the coordinates
    pyautogui.click()
    
    
    #Type the meetind Id
    meet_id = pyautogui.locateCenterOnScreen('meetId.png')
    pyautogui.moveTo(meet_id)
    pyautogui.click()
    pyautogui.write(meetid)
    
    #Disables audio and video
    media_btn = pyautogui.locateAllOnScreen('media.png')
    for btn in media_btn:
        pyautogui.moveTo(btn)
        pyautogui.click()
        time.sleep(2)
        
    #Clicks Join
    join = pyautogui.locateCenterOnScreen('join.png')
    pyautogui.moveTo(join)
    pyautogui.click()
    time.sleep(8)
    
    #Type the pass Id
    meetpsd = pyautogui.locateAllOnScreen('pass.png')
    pyautogui.moveTo(meetpsd)
    pyautogui.click()
    pyautogui.write(pwd)
    pyautogui.press('enter')
    
    
