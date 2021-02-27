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