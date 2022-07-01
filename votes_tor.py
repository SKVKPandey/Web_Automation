from time import sleep
from pyautogui import press
from os import system
import webbrowser

mode = input("Do you want finite(f)/infinite(i) loop? ")

if mode=="f":
    times = int(input("Enter Number of Iterations: "))
    delay = int(input("Enter Delay: "))

    for i in range(times):
        url = 'https://india.enactus.org/contest9/entry/357'
        webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(r"C:\Users\shash\OneDrive\Desktop\Tor Browser\Browser\firefox.exe"))
        webbrowser.get('firefox').open(url)
        sleep(delay)
        for _ in range(9):
            press('tab')
        press('enter')
        sleep(2)
        system("taskkill /im firefox.exe /f")

else:
    delay = int(input("Enter Delay: "))

    while True:
        url = 'https://india.enactus.org/contest9/entry/357'
        webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(r"C:\Users\shash\OneDrive\Desktop\Tor Browser\Browser\firefox.exe"))
        webbrowser.get('firefox').open(url)
        sleep(delay)
        for _ in range(9):
            press('tab')
        press('enter')
        sleep(2)
        system("taskkill /im firefox.exe /f")