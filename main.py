import pyautogui
from menu import *
from functions import *
from tfmScripts import *
import sys
import time
from time import sleep

# Main option select
def message():
        pyautogui.hotkey('enter')
        pyautogui.PAUSE = 0.5
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.PAUSE = 0.5
        pyautogui.hotkey('enter')

def main():
    for y in range(999):
        wipe()
        first()
        userinput = input("**** >>> ")
        if userinput == str(1):
                wipe()
                fast_nonsteam()
                userAutoLogininput = input("**** >>> ")
                if userAutoLogininput == str(1):
                        wipe()
                        copyPaste()
                        login1920x1080_nonsteam_fast()
                        copyPasteMessage()
                        message()
                        wipe()
                        break
                if userAutoLogininput == str(2):
                        wipe()
                        copyPaste()
                        login1366x768_nonsteam_fast()
                        copyPasteMessage()
                        message()
                        wipe()
                        break
                if userAutoLogininput == str(3):
                        wipe()
                        copyPaste()
                        login1280x800_nonsteam_fast()
                        copyPasteMessage()
                        message()
                        wipe()
                        break
                else:
                    break
        
        if userinput == str(2):
                wipe()
                fast_steam()
                userAutoLogininput = input("**** >>> ")
                if userAutoLogininput == str(1):
                        wipe()
                        copyPaste()
                        login1920x1080_steam_fast()
                        copyPasteMessage()
                        message()
                        wipe()
                        break
                if userAutoLogininput == str(2):
                        wipe()
                        copyPaste()
                        login1366x768_steam_fast()
                        copyPasteMessage()
                        message()
                        wipe()
                        break
                if userAutoLogininput == str(3):
                        wipe()
                        copyPaste()
                        login1280x800_steam_fast()
                        copyPasteMessage()
                        message()
                        wipe()
                        break
                else:
                    raise SystemExit

        if userinput == str(3):
                wipe()
                slow_nonsteam()
                userAutoLogininput = input("**** >>> ")
                if userAutoLogininput == str(1):
                        wipe()
                        copyPaste()
                        login1920x1080_nonsteam_slow()
                        copyPasteMessage()
                        message()
                        wipe()
                        break
                if userAutoLogininput == str(2):
                        wipe()
                        copyPaste()
                        login1366x768_nonsteam_slow()
                        copyPasteMessage()
                        message()
                        wipe()
                        break
                if userAutoLogininput == str(3):
                        wipe()
                        copyPaste()
                        login1280x800_nonsteam_slow()
                        copyPasteMessage()
                        message()
                        wipe()
                        break
                else:
                    raise SystemExit
                
        if userinput == str(4):
                wipe()
                slow_steam()
                userAutoLogininput = input("**** >>> ")
                if userAutoLogininput == str(1):
                        wipe()
                        copyPaste()
                        login1920x1080_steam_slow()
                        copyPasteMessage()
                        message()
                        wipe()
                        break
                if userAutoLogininput == str(2):
                        wipe()
                        copyPaste()
                        login1366x768_steam_slow()
                        copyPasteMessage()
                        message()
                        wipe()
                        break
                if userAutoLogininput == str(3):
                        wipe()
                        copyPaste()
                        login1280x800_steam_slow()
                        copyPasteMessage()
                        message()
                        wipe()
                        break
        elif userinput == str(5):
            wipe()
            print("Enter your password:")
            writeFile()
            wipe()
        elif userinput == str(6):
            wipe()
            resolution()
            input()
            wipe()
        elif userinput == str(7):
            wipe()
            print("Enter your message: ")
            writeMessageFile()
            wipe()
        elif userinput == str(8):
            wipe()
            contact()
        elif userinput == str(9):
            wipe()
            browser()
            helpScript()
            ehha = input(">>> ")
            if ehha == 'req':
                url = 'https://github.com/Mariuseledy/FattyRAT'
                if sys.platform == '':   
                        subprocess.Popen(['open', url])
                else:
                        webbrowser.open_new_tab(url)
        elif userinput == "secret":
                secret()
                
        else:
                main()
        return True

