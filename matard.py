import pyautogui as ptg
import time

def matar():

    tempo = 0
    limite = 3
    temposkill = 0
    lado = 'right'
    tp = 'shift'
    time.sleep(2)

    while (tempo < limite):
        ptg.keyDown(tp)
        time.sleep(.1)
        ptg.keyDown(lado)
        ptg.keyUp(tp)
        ptg.keyUp(lado)
        time.sleep(0.25)
        tempo += 1
        if tempo == limite:
            ptg.doubleClick(x=174, y=262)
            temposkill += 1
            time.sleep(1.75)
            break

if __name__ == '__main__':
    matar()







