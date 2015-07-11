import pyautogui

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

print "Press Ctrl-C to quit."

try:
    while True:
        pyautogui.click(450,300)
        pyautogui.click(220,14)
        pyautogui.click(217, 310)
        pyautogui.click(431,310)
except KeyboardInterrupt:
    print "\nDone"
