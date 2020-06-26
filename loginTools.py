import pyautogui
from time import sleep
import configReader as cr

def mainLogin(key: str):
    login, password = cr.getLogin(key)
    sleep(cr.delay)
    pyautogui.click()
    pyautogui.typewrite(login)
    sleep(cr.getWaitTime(key))
    pyautogui.press('tab')
    pyautogui.typewrite(password)
    pyautogui.press('enter')

def appLogin(e = None):
    pyautogui.moveTo(cr.position)
    pyautogui.moveTo(cr.position)#extra point if you know why it's doubled
    mainLogin(e.keysym)

def appLoginHere(e = None):
    mainLogin(e.keysym)
