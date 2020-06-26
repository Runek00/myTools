import pyautogui
from time import sleep
import configReader as cr
from typing import Optional
from tkinter import Event

def mainLogin(key: str) -> None:
    login, password = cr.getLogin(key)
    sleep(cr.delay)
    pyautogui.click()
    pyautogui.typewrite(login)
    sleep(cr.getWaitTime(key))
    pyautogui.press('tab')
    pyautogui.typewrite(password)
    pyautogui.press('enter')

def appLogin(e: Optional[Event] = None) -> None:
    pyautogui.moveTo(cr.position)
    pyautogui.moveTo(cr.position)#extra point if you know why it's doubled
    mainLogin(e.keysym)

def appLoginHere(e: Optional[Event] = None) -> None:
    mainLogin(e.keysym)
