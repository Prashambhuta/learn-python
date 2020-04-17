#! usr/bin/env python3
"""
Using screenshot feature to recognise the windows, and current content for
better automation controlling using `pyautogui`
"""

import pyautogui

# to take screenshot:, it will return a Pillow object
# pyautogui.screenshot('/home/prasham/Documents/sample_screenshot.png')

# to do image recognition, use `.locateOnScreen` with the cropped image of
# icon as a argument

# Example: lets try to click on the `Run` option of pycharm IDE.
run_option = pyautogui.locateOnScreen('/home/prasham/Pictures/pycharm_run.png')
print(run_option)

# use `.locateCenterOnScreen` for accuracy
run_option = pyautogui.locateCenterOnScreen(
    '/home/prasham/Pictures/pycharm_run.png')
print(run_option)

# moving the mouse and clicking the object `Run`
pyautogui.moveTo(run_option, duration=3)
pyautogui.click()

"""
This completes the automate the boring stuff using python by asweigart
"""

