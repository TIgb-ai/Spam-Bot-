import pyautogui
import time
time.sleep(5)
f = open("spam.txt",'r')
for spam in f:
    pyautogui.typewrite(spam)
    pyautogui.press('enter')
    print("Hehe boi trolled")