import pyautogui

pyautogui.PAUSE = 2
pyautogui.FAILSAFE = True

print "Press Ctrl-C to quit."

try:
    while True:
        pyautogui.click(450,300)
        pyautogui.typewrite('Hello world this is a test. ')
        pyautogui.keyDown('command')
        pyautogui.keyDown('shiftleft')
        pyautogui.keyDown('T')
        pyautogui.keyUp('command')
        pyautogui.keyUp('shiftleft')
        pyautogui.keyUp('T') 
except KeyboardInterrupt:
    print "\nDone"
