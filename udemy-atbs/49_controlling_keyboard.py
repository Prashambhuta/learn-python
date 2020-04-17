#! usr/bin/env python3
"""
Controlling the keyboard using pyautogui
"""

import pyautogui

# to type text use `typewrite()` method
pyautogui.typewrite("Hello world!", interval=1)

# to press special keys
pyautogui.typewrite(['d', 'backspace', 'p'], interval=0.1)

# to see all keyboard keys option use `KEYBOARD_KEYS` method
# print(pyautogui.KEYBOARD_KEYS)

# to press the single key
# pyautogui.press('f1')

# to press shortcuts or multiple key together
# pyautogui.hotkey('shift', 'f10')
pyautogui.hotkey('ctrl', 'n')
