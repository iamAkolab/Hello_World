import pyautogui

pyautogui.click()  #Click to put drawing pen
distance = 200

while distance > 0:
    print(distance,0)

    #move right
    pyautogui.dragRel(distance, 0, duration = 0.1)
    distance = distance - 25
    print(0,distance)

    #move down
    pyautogui.dragRel(0, distance, duration = 0.1)
    print(-distance,0)

    #move left
    pyautogui.dragRel(-distance, 0, duration = 0.1)
    distance = distance - 25
    print(0,-distance)

    #move up
    pyautogui.dragRel(0, -distance, duration = 0.1)

'''
To get the screen coordinate you need.

C:\WINDOWS\system32>py -3.9

Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import pyautogui
>>> pyautogui.displayMousePosition()

Press Ctrl-C to quit.

X: 311 Y:274 RGB: (0. 0. 0.)
'''