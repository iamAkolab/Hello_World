import pyautogui

# get the size
width, height = pyautogui.size()
print(width)
print(height)

# Get the current postion of the mouse
print(pyautogui.position())

#move to an x,y coordinate
pyautogui.moveTo(200,200)

# specify speed
pyautogui.moveTo(400,400, duration= 1.5)

# move relative to the current position
pyautogui.moveRel(400,200)

# specify speed
pyautogui.moveRel(400,200, duration =1)

# click somewhere on the screan
# print(pyautogui.position(10,10))
pyautogui.click(10,40)
pyautogui.doubleClick(10,40)


# To click where the mouse is currently
pyautogui.click()