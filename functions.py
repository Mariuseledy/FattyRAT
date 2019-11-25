import os
import pyautogui, sys
import pyperclip
import subprocess
import webbrowser
import sys

def wipe():
    clear = lambda: os.system('cls') 
    clear()

def cursorLocation():
    print('Press Ctrl-C to quit.')
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')

def resolution():
    pyautogui.size()
    print("Here is your resolution:")
    print("")
    print(pyautogui.size())

    print("Press enter to leave")

def writeFile():
    passw = input("> ")
    with open('password.txt', 'w') as f:
        f.write(passw)

def copyPaste():
    filepath = 'password.txt'
    line = ""
    with open(filepath) as f:
        line = f.readline()
    pyperclip.copy(line)
    pyperclip.paste()

def writeMessageFile():
    msg = input("> ")
    with open('message.txt', 'w') as f:
        f.write(msg)

def copyPasteMessage():
    filepath = 'message.txt'
    line = ""
    with open(filepath) as f:
        line = f.readline()
    pyperclip.copy(line)
    pyperclip.paste()

def browser():
    url = 'https://youtu.be/eHXAxDk2qRo'
    if sys.platform == '':
        subprocess.Popen(['open', url])
    else:
        webbrowser.open_new_tab(url)

def downloadLinks():
    url = 'https://github.com/Mariuseledy/FattyRAT'
    if sys.platform == '':
        subprocess.Popen(['open', url])
    else:
        webbrowser.open_new_tab(url)

def tfmMessage():
    pyautogui.hotkey('enter')
    pyautogui.PAUSE = 1
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.PAUSE = 2

def secret():
    url = 'https://youtu.be/dkxYiI2W2tY'
    if sys.platform == '':
        subprocess.Popen(['open', url])
    else:
        webbrowser.open_new_tab(url)
