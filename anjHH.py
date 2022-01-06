import pyautogui as pg
import time
import keyboard

result = pg.position()
print(result)

def anjHH_login():
    pg.click(x=452,y=843)
    pg.click(x=482,y=685)
    pg.write('similan')
    pg.press('enter')
    pg.write('similan')
    pg.press('enter')
    # time.sleep(0.3)
def anjHH_login2():
    pg.click(x=104,y=897)
    pg.click(x=125,y=735)
    pg.write('similan')
    pg.press('enter')
    pg.write('similan')
    pg.press('enter')

def anjHH_login3():     
    pg.write('similan')
    pg.press('enter')
    pg.write('similan')
    pg.press('enter')

def operation():
    pg.click(x=470,y=167)
    time.sleep(0.5)
    pg.click(x=533,y=264)

def operation2():
    pg.click(x=122,y=174)
    time.sleep(0.5)
    pg.click(x=167,y=280)

def main():
    while 1:
        try:
            if keyboard.is_pressed('F1'):
                anjHH_login3()
                time.sleep(1)
                # operation2()                                
                # time.sleep(1)
            elif keyboard.is_pressed('F3'):
                # operation()                
                time.sleep(1)
                pg.write("warehousedbo")
            elif keyboard.is_pressed('F4'):
                anjHH_login3()
        except:
            break
        time.sleep(0.1)

main()