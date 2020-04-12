#! usr/bin/env python3

"""
Controlling and copying mouse movements using python.
Sending virtual clicks and key-strokes using `pyautogui`
"""

import pyautogui

# return the screen size
print(pyautogui.size())

# return the current position of the mouse
print(pyautogui.position())

# change the position of the mouse using `moveTo`
pyautogui.moveTo(40, 40, duration = 1.5)

# moving the mouse relative of current position using `moveRel`
pyautogui.moveRel(xOffset=1000, yOffset=0, duration=1.5,)

"""
Clicking on stuff:
Example - Launch Firefox on Ubuntu
"""

# figure the position of the icon
firefox_pos = (22, 68)

# pass the position as moveTo
pyautogui.moveTo(firefox_pos, duration=1)
pyautogui.click()

"""
fail safe:
drag the mouse to the top left corner
"""






