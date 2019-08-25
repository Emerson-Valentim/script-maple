import pyautogui as ptg
import time

def buff():

    tempo = 0
    limite = 1
    buff = 'shift'

    if tempo != 1:
        ptg.click(x=473, y=95)
        ptg.click(x=673, y=504)
        ptg.click(x=722, y=349)

        while tempo < limite:

            ptg.keyDown(buff)
            ptg.press('left')
            ptg.keyUp(buff)
            time.sleep(2)
            tempo += 1
            ptg.click(x=472, y=144)
            ptg.click(x=673, y=504)
            ptg.click(x=722, y=349)
            ptg.keyDown(buff)
            ptg.press('left')
            ptg.keyUp(buff)
            time.sleep(2.5)
            ptg.click(x=234, y=60)
            ptg.click(x=175, y=182)
            ptg.click(x=673, y=504)
            ptg.click(x=722, y=349)
            ptg.click(x=304, y=58)


if __name__ == '__main__':
    buff()