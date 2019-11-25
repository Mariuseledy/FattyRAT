import pyautogui 

# 1920x1080 
def login1920x1080_nonsteam_fast():
    pyautogui.hotkey("winleft", "d")
    pyautogui.PAUSE = 1
    pyautogui.hotkey("winleft", "r")
    pyautogui.PAUSE = 1.5
    pyautogui.typewrite('C:\Program Files (x86)\Transformice\Transformice.exe')
    pyautogui.PAUSE = 1.5
    pyautogui.hotkey("enter")
    pyautogui.PAUSE = 2.5
    pyautogui.PAUSE = 1
    pyautogui.hotkey('winleft', 'up')
    pyautogui.PAUSE = 13
    pyautogui.click(787, 305)
    pyautogui.PAUSE = 0.3
    pyautogui.click(715, 402)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')
    pyautogui.moveTo(1095, 690, 2.5)
    pyautogui.click()
    pyautogui.moveTo(1205, 400, 1)
    pyautogui.click()
    pyautogui.moveTo(641, 335, 1)
    pyautogui.click()

def login1920x1080_steam_fast():
    pyautogui.hotkey("winleft", "d")
    pyautogui.PAUSE = 1
    pyautogui.hotkey("winleft", "r")
    pyautogui.PAUSE = 1.5
    pyautogui.typewrite('C:\Program Files (x86)\Steam\steamapps\common\Transformice\Transformice.exe')
    pyautogui.PAUSE = 1.5
    pyautogui.hotkey("enter")
    pyautogui.PAUSE = 2.5
    pyautogui.PAUSE = 1
    pyautogui.hotkey('winleft', 'up')
    pyautogui.PAUSE = 10
    pyautogui.click(787, 305)
    pyautogui.PAUSE = 0.3
    pyautogui.click(715, 402)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')
    pyautogui.moveTo(1095, 690, 2.5)
    pyautogui.click()
    pyautogui.moveTo(1205, 400, 1)
    pyautogui.click()
    pyautogui.moveTo(641, 335, 1)
    pyautogui.click()

def login1920x1080_nonsteam_slow():
    pyautogui.hotkey("winleft", "d")
    pyautogui.PAUSE = 1
    pyautogui.hotkey("winleft", "r")
    pyautogui.PAUSE = 2.0
    pyautogui.typewrite('C:\Program Files (x86)\Transformice\Transformice.exe')
    pyautogui.PAUSE = 2
    pyautogui.hotkey("enter")
    pyautogui.PAUSE = 0.5
    pyautogui.PAUSE = 4.5
    pyautogui.hotkey('winleft', 'up')
    pyautogui.PAUSE = 21
    pyautogui.click(787, 305)
    pyautogui.PAUSE = 0.3
    pyautogui.click(715, 402)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')
    pyautogui.moveTo(1095, 690, 3.5)
    pyautogui.click()
    pyautogui.moveTo(1205, 400, 1.5)
    pyautogui.click()
    pyautogui.moveTo(641, 335, 1.5)
    pyautogui.click()

def login1920x1080_steam_slow():
    pyautogui.hotkey("winleft", "d")
    pyautogui.PAUSE = 1
    pyautogui.hotkey("winleft", "r")
    pyautogui.PAUSE = 2
    pyautogui.typewrite('C:\Program Files (x86)\Steam\steamapps\common\Transformice\Transformice.exe')
    pyautogui.PAUSE = 3
    pyautogui.hotkey("enter")
    pyautogui.PAUSE = 0.5
    pyautogui.PAUSE = 4.5
    pyautogui.hotkey('winleft', 'up')
    pyautogui.PAUSE = 18
    pyautogui.click(926, 438)
    pyautogui.PAUSE = 0.3
    pyautogui.click(715, 402)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')
    pyautogui.moveTo(1095, 690, 3.5)
    pyautogui.click()
    pyautogui.moveTo(1205, 400, 1.5)
    pyautogui.click()
    pyautogui.moveTo(641, 335, 1.5)
    pyautogui.click()

#1366x768 
def login1366x768_nonsteam_fast():
    pyautogui.hotkey("winleft", "d")
    pyautogui.PAUSE = 1
    pyautogui.hotkey("winleft", "r")
    pyautogui.PAUSE = 1.5
    pyautogui.typewrite('C:\Program Files (x86)\Transformice\Transformice.exe')
    pyautogui.PAUSE = 1.5
    pyautogui.hotkey("enter")
    pyautogui.PAUSE = 2.5
    pyautogui.PAUSE = 1.0
    pyautogui.hotkey('winleft', 'up')
    pyautogui.PAUSE = 13
    pyautogui.click(568, 229)
    pyautogui.PAUSE = 0.3
    pyautogui.click(436, 245)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')
    pyautogui.moveTo(817, 535, 2.5)
    pyautogui.click()
    pyautogui.moveTo(930, 243, 1.0)
    pyautogui.click()
    pyautogui.moveTo(358, 178, 1.0)
    pyautogui.click()

def login1366x768_nonsteam_slow():
    pyautogui.hotkey("winleft", "d")
    pyautogui.PAUSE = 1
    pyautogui.hotkey("winleft", "r")
    pyautogui.PAUSE = 2.0
    pyautogui.typewrite('C:\Program Files (x86)\Transformice\Transformice.exe')
    pyautogui.PAUSE = 2
    pyautogui.hotkey("enter")
    pyautogui.PAUSE = 0.5
    pyautogui.PAUSE = 4.5
    pyautogui.hotkey('winleft', 'up')
    pyautogui.PAUSE = 21
    pyautogui.click(568, 229)
    pyautogui.PAUSE = 0.3
    pyautogui.click(438, 246)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')
    pyautogui.moveTo(817, 535, 3.5)
    pyautogui.click()
    pyautogui.moveTo(930, 243, 1.5)
    pyautogui.click()
    pyautogui.moveTo(358, 178, 1.5)
    pyautogui.click()

def login1366x768_steam_fast():
    pyautogui.hotkey("winleft", "d")
    pyautogui.PAUSE = 1
    pyautogui.hotkey("winleft", "r")
    pyautogui.PAUSE = 1.5
    pyautogui.typewrite('C:\Program Files (x86)\Steam\steamapps\common\Transformice\Transformice.exe')
    pyautogui.PAUSE = 1.5
    pyautogui.hotkey("enter")
    pyautogui.PAUSE = 2.5
    pyautogui.PAUSE = 1.0
    pyautogui.hotkey('winleft', 'up')
    pyautogui.PAUSE = 10
    pyautogui.click(568, 229)
    pyautogui.PAUSE = 0.3
    pyautogui.click(438, 246)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')
    pyautogui.moveTo(817, 535, 2.5)
    pyautogui.click()
    pyautogui.moveTo(930, 243, 1.0)
    pyautogui.click()
    pyautogui.moveTo(358, 178, 1.0)
    pyautogui.click()

def login1366x768_steam_slow():
    pyautogui.hotkey("winleft", "d")
    pyautogui.PAUSE = 1
    pyautogui.hotkey("winleft", "r")
    pyautogui.PAUSE = 2.0
    pyautogui.typewrite('C:\Program Files (x86)\Steam\steamapps\common\Transformice\Transformice.exe')
    pyautogui.PAUSE = 3
    pyautogui.hotkey("enter")
    pyautogui.PAUSE = 0.5
    pyautogui.PAUSE = 4.5
    pyautogui.hotkey('winleft', 'up')
    pyautogui.PAUSE = 18
    pyautogui.click(568, 229)
    pyautogui.PAUSE = 0.3
    pyautogui.click(438, 246)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')
    pyautogui.moveTo(817, 535, 3.5)
    pyautogui.click()
    pyautogui.moveTo(930, 243, 1.5)
    pyautogui.click()
    pyautogui.moveTo(358, 178, 1.5)
    pyautogui.click()

# 1280x800 
def login1280x800_nonsteam_fast():
    pyautogui.hotkey("winleft", "d")
    pyautogui.PAUSE = 1
    pyautogui.hotkey("winleft", "r")
    pyautogui.PAUSE = 1.5
    pyautogui.typewrite('C:\Program Files (x86)\Transformice\Transformice.exe')
    pyautogui.PAUSE = 1.5
    pyautogui.hotkey("enter")
    pyautogui.PAUSE = 2.5
    pyautogui.PAUSE = 1.0
    pyautogui.hotkey('winleft', 'up')
    pyautogui.PAUSE = 10
    pyautogui.click(581, 264)
    pyautogui.PAUSE = 0.3
    pyautogui.click(397, 262)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')
    pyautogui.moveTo(774, 550, 2.5)
    pyautogui.click()
    pyautogui.moveTo(886, 260, 1.0)
    pyautogui.click()
    pyautogui.moveTo(314, 193, 1.0)
    pyautogui.click()

def login1280x800_nonsteam_slow():
    pyautogui.hotkey("winleft", "d")
    pyautogui.PAUSE = 1
    pyautogui.hotkey("winleft", "r")
    pyautogui.PAUSE = 2.0
    pyautogui.typewrite('C:\Program Files (x86)\Transformice\Transformice.exe')
    pyautogui.PAUSE = 2
    pyautogui.hotkey("enter")
    pyautogui.PAUSE = 0.5
    pyautogui.PAUSE = 4.5
    pyautogui.hotkey('winleft', 'up')
    pyautogui.PAUSE = 21
    pyautogui.click(581, 264)
    pyautogui.PAUSE = 0.3
    pyautogui.click(397, 262)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')
    pyautogui.moveTo(774, 550, 3.5)
    pyautogui.click()
    pyautogui.moveTo(886, 260, 1.5)
    pyautogui.click()
    pyautogui.moveTo(314, 193, 1.5)
    pyautogui.click()

def login1280x800_steam_fast():
    pyautogui.hotkey("winleft", "d")
    pyautogui.PAUSE = 1
    pyautogui.hotkey("winleft", "r")
    pyautogui.PAUSE = 1.5
    pyautogui.typewrite('C:\Program Files (x86)\Steam\steamapps\common\Transformice\Transformice.exe')
    pyautogui.PAUSE = 1.5
    pyautogui.hotkey("enter")
    pyautogui.PAUSE = 2.5
    pyautogui.PAUSE = 1.0
    pyautogui.hotkey('winleft', 'up')
    pyautogui.PAUSE = 10
    pyautogui.click(581, 264)
    pyautogui.PAUSE = 0.3
    pyautogui.click(397, 262)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')
    pyautogui.moveTo(774, 550, 3.5)
    pyautogui.click()
    pyautogui.moveTo(886, 260, 1.5)
    pyautogui.click()
    pyautogui.moveTo(314, 193, 1)
    pyautogui.click()

def login1280x800_steam_slow():
    pyautogui.hotkey("winleft", "d")
    pyautogui.PAUSE = 1
    pyautogui.hotkey("winleft", "r")
    pyautogui.PAUSE = 2.0
    pyautogui.typewrite('C:\Program Files (x86)\Steam\steamapps\common\Transformice\Transformice.exe')
    pyautogui.PAUSE = 3
    pyautogui.hotkey("enter")
    pyautogui.PAUSE = 0.5
    pyautogui.PAUSE = 4.5
    pyautogui.hotkey('winleft', 'up')
    pyautogui.PAUSE = 18
    pyautogui.click(581, 264)
    pyautogui.PAUSE = 0.3
    pyautogui.click(397, 262)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')
    pyautogui.moveTo(774, 550, 3.5)
    pyautogui.click()
    pyautogui.moveTo(886, 260, 1.5)
    pyautogui.click()
    pyautogui.moveTo(314, 193, 1.5)
    pyautogui.click()
# maybe will add in the future more