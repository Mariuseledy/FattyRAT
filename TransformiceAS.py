import pyautogui
import sys
import time
from time import sleep
from functions import *
from tfmScripts import *
from main import *
from menu import *

print("****************************************** LOADING ***************************************************")
for i in range(101):
    sys.stdout.write('\r')
    sys.stdout.write("[%-10s] %d%%" % ('='*i, 1*i))
    sys.stdout.flush()
    sleep(0.02)
print("***************************************** >  DONE  < *************************************************")

while main():
    pass

