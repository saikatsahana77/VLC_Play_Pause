import sys
from PyQt5.QtWidgets import QApplication
import pyautogui as pyauto
import win32api
import win32gui
import time

app = QApplication(sys.argv)
dw = app.desktop()  
taskbar_height = dw.screenGeometry().height() - dw.availableGeometry().height()

print(taskbar_height)

state_left = win32api.GetKeyState(0x01)
while True:
    try:
        k = pyauto.position()
        if k[1]>=45 and k[1]<=dw.availableGeometry().height()-53:
            window = win32gui.GetForegroundWindow()
            active_window_name = win32gui.GetWindowText(window)
            if active_window_name.endswith(' - VLC media player'):
                print(active_window_name)
                a = win32api.GetKeyState(0x01)
                if a != state_left:   
                    state_left = a
                    print(a) 
                    if a >= 0: 
                        print('Left Button Pressed')   
                        pyauto.press('space')

        time.sleep(0.01)
    except:
        break
