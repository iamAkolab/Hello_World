import pyautogui

pyautogui.click(100,100)
pyautogui.typewrite('Hello world')

pyautogui.click(100,100)
pyautogui.typewrite('Hello world', interval=0.15)

#to insert to the left
pyautogui.click(100,100)
pyautogui.typewrite('a','b','left','left','X','Y', interval=0.15)

#complete keyboard keys
#print(pyautogui.KEYBOARD_KEYS())

#bring python help
pyautogui.press('f1')

pyautogui.hotkey('ctrl','s')