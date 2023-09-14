import pyautogui
from time import sleep
pyautogui.PAUSE = 1.5
pyautogui.FAILSAFE = True
pyautogui.position()
pyautogui.press('f4')

width, height = pyautogui.size()
print(width, height)
##
#перемещение
pyautogui.moveTo(2560/2,1440/2, duration=1)
pyautogui.move(-200,-200, duration = 2)
##
#нажатие
pyautogui.click(clicks = 1 , interval = 0.05)
pyautogui.doubleClick()
pyautogui.tripleClick()
pyautogui.rightClick()
pyautogui.middleClick()
pyautogui.vscroll(200)
# %%
#перемещение с зажатием
pyautogui.position()
pyautogui.moveTo(1682,857,duration = 1)
pyautogui.dragTo(1510,857,duration = 1)
pyautogui.move(100,-1,duration = 1)
pyautogui.dragTo(1551,637,duration = 1)
##
#ввод с клавиатуры
pyautogui.click(clicks = 1 , interval = 0.05)
pyautogui.PAUSE = 1.5
pyautogui.typewrite('Hello,World!', interval=0.2)
##
#Нажатие клавиш: press, hotkey
pyautogui.click(clicks = 1 , interval = 0.05)
pyautogui.PAUSE = 1.5
pyautogui.press('Enter')
pyautogui.hotkey('ctrl','a')
##
#Скриншоты и нахождение отдельных элементов???????????
pyautogui.PAUSE = 2
pyautogui.screenshot(r"C:\Users\test 2\Pictures\Example.png")
pyautogui.PAUSE = 2
pyautogui.locateCenterOnScreen(r"C:\Users\/test 2\Pictures\/text.png")
pyautogui.click()
##
#Всплывающие окна
sleep(2)
print(pyautogui.alert(text='Надпись', title='inteceptor', button='OK'))
print(pyautogui.confirm(text='Надпись', title='опрос', buttons=['OK', 'Cancel']))

##
#Список открытых приложений
programm_list = pyautogui.getAllTitles() #список отрытых приложений
print(programm_list)
