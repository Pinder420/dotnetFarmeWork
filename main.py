import pyautogui
import time
from random import randint

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

pyautogui.FAILSAFE = False
while True:
    time.sleep(random_with_N_digits(1))
    for i in range(0, 10):
        pyautogui.moveTo(random_with_N_digits(3),  random_with_N_digits(3) * 5)
    for i in range(0, random_with_N_digits(1)):
        pyautogui.press('shift')