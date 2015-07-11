import pyautogui

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

print "Press Ctrl-C to quit."

pyautogui.click(450,300)
try:
    while True:
        pyautogui.typewrite('Hello world this is a test. ')
except KeyboardInterrupt:
    print "\nDone"
