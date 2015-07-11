import pyautogui

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

print "Press Ctrl-C to quit."

try:
    while True:
        # TODO: Get and print the mouse coordinates
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print positionStr
        #print "\b" * len(positionStr), 
except KeyboardInterrupt:
    print "\nDone"
