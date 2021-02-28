import pyautogui

# Get the image
pyautogui.screenshot('C:\\Users\\john\\Pictures\\screenshot3.png')

# crop the image 

#pass the image and returns the coordinates of where the image is on screen
pyautogui.locateOnScreen('c:\\calc7key.png')
#(907, 316, 50, 41)

#get the center of the image and will return a tuple(x,y)
pyautogui.locateCenterOnScreen('c:\\calc7key.png')
#(932, 336)

#move to that center
pyautogui.moveTo((932, 336), duration=1)

#then click
pyautogui.click()

#fail safe is to slam the mouse button to the top left corner
#susi go round bot
#https://github.com/asweigart/susigoroundbot