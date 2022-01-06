from re import X
import pyautogui as pg
import time
import keyboard

result = pg.position()
print(result)
# print(pg.size())
# pg.moveRel(0, 100, duration=0.25)
# pg.moveRel(0,0, duration=2)
# icon_location = pg.locateOnScreen('C:\Users\USER-PC\Desktop\Learn\python bot\assetsbotNo1\IMG\Screenshot 2021-11-02 085323.png')
# print(icon_location)

# loc = pg.locateOnScreen('C:\Users\USER-PC\Desktop\Learn\python bot\assetsbotNo1\IMG\Capture.PNG', grayscale=True, confidence=.5)
# print(loc)


def login_POS_anon():
    pg.click(x=1075,y=478)
    pg.write("anon")
    pg.press('enter')
    pg.write("anon")
    pg.press('enter')
    time.sleep(1)
    
# login_POS_anon()

def login_EKP():
    pg.click(x=1051,y=598)
    time.sleep(1)
    pg.click(x=908,y=534)
    time.sleep(1)
    pg.write("anon")

    pg.press('enter')
    pg.write("anon")
    pg.press('enter')
    pg.press('enter')
    time.sleep(2)



# login_EKP()

def start_ANJ():
    pg.click(x=1050,y=599)
    time.sleep(1.5)
    pg.doubleClick(x=848,y=326)
    time.sleep(1)

def ANJ_Report_report():
    pg.click(x=31,y=971)
    time.sleep(1)
    pg.doubleClick(x=52,y=195)
    # time.sleep(1)

# start_ANJ()
# ANJ_Report_report()


def login_GBF():
    pg.click(x=1051,y=598)
    time.sleep(1)
    pg.click(x=908,y=534)
    time.sleep(1)
    pg.write("similan")
    pg.press('enter')
    pg.write("software")
    pg.press('enter')
    pg.press('enter')
    time.sleep(2)

def INQUIRY_Inbound_POQ(): #OP = Open
    pg.click(x=135,y=122)
    time.sleep(0.5)
    pg.doubleClick(x=66,y=146)
    time.sleep(0.5)
    pg.click(x=126,y=166)
    time.sleep(0.5)

def INQUIRY_Inbound_ROQ(): #OP = Open
    pg.click(x=135,y=122)
    time.sleep(0.5)
    pg.doubleClick(x=66,y=146)
    time.sleep(0.5)
    pg.click(x=141,y=189)
    time.sleep(0.5)

def INQUIRY_Outbound_DOQ(): #OP = Open
    pg.click(x=135,y=122)
    time.sleep(0.5)
    pg.doubleClick(x=63,y=166)
    time.sleep(0.5)
    pg.click(x=111,y=186)
    time.sleep(0.5)

def INQUIRY_Outbound_SOQ():
    pg.click(x=135,y=122)
    time.sleep(0.5)
    pg.doubleClick(x=63,y=166)
    time.sleep(0.5)
    pg.click(x=96,y=208)
    time.sleep(0.5)

def INQUIRY_Stock_status_IIQ(): 
    pg.click(x=135,y=122)
    time.sleep(0.5)
    pg.doubleClick(x=131,y=205)
    time.sleep(0.5)
    pg.click(x=125,y=209)
    time.sleep(0.5)

def INQUIRY_Stock_status_LHQ(): 
    pg.click(x=135,y=122)
    time.sleep(0.5)
    pg.doubleClick(x=131,y=205)
    time.sleep(0.5)
    pg.click(x=136,y=203)
    time.sleep(0.5)

def INQUIRY_Stock_status_PHQ(): 
    pg.click(x=135,y=122)
    time.sleep(0.5)
    pg.doubleClick(x=67,y=189)
    time.sleep(0.5)
    pg.click(x=103,y=246)
    time.sleep(0.5)

def INQUIRY_Warehouse_WOSQ(): 
    pg.click(x=135,y=122)
    time.sleep(0.5)
    pg.doubleClick(x=66,y=205)
    time.sleep(0.5)
    pg.click(x=162,y=224)
    time.sleep(0.5)

def INQUIRY_Warehouse_WUQ(): 
    pg.click(x=135,y=122)
    time.sleep(0.5)
    pg.doubleClick(x=66,y=205)
    time.sleep(0.5)
    pg.click(x=141,y=245)
    time.sleep(0.5)

def login_tsc():
    # pg.click(x=1051,y=598)
    # time.sleep(1)
    # pg.click(x=908,y=534)
    # time.sleep(1)
    pg.write("ANON")
    pg.press('enter')
    pg.write("ANON")
    pg.press('enter')
    pg.press('enter')
    time.sleep(2)

def tsc_Reports_reports():
    pg.click(x=109,y=193)
    time.sleep(0.5)
    pg.click(x=70,y=227)
    time.sleep(0.5)

def login_ANJ():
    pg.click(x=1035,y=606)
    time.sleep(1)
    pg.press('enter')

def ANJ_Peration_outbound_fair_shear_wo():
    pg.click(x=49,y=192)
    time.sleep(0.5)
    pg.click(x=78,y=250)
    time.sleep(0.5)
    pg.click(x=1364,y=274)

def POS_ANJ_purchase():
    pg.click(x=273,y=66)
    time.sleep(0.5)
    pg.click(x=959,y=757)
    time.sleep(0.5)
    pg.click(x=772,y=121)
    time.sleep(0.5)
    pg.click(x=772,y=121)
    time.sleep(0.5)
    pg.write("023-01-202958")
    pg.click(x=1730,y=739)
    time.sleep(0.5)
    pg.click(x=1587,y=993)
    time.sleep(0.5)
    pg.click(x=959,y=757)
    time.sleep(0.5)
    pg.click(x=813,y=688)
    time.sleep(0.5)
    pg.write("10")
    pg.click(x=518,y=944)
    time.sleep(0.5)
    pg.click(x=847,y=880)

def login_JRFB():    
    # pg.click(x=1052,y=596)
    pg.press("enter")
    time.sleep(1)
    pg.press("enter")
    # pg.click(x=1115,y=601)
    time.sleep(2)
    pg.click(x=907,y=527)
    time.sleep(1)
    pg.write("SIMILAN")
    pg.press("enter")
    pg.write("SOFTWARE")
    pg.press('enter')
    time.sleep(2)
    pg.press('enter')
    time.sleep(1)

def JRFB_Operation_QA():
    pg.doubleClick(x=75,y=260)
    time.sleep(0.5)
    pg.click(x=104,y=277)
    time.sleep(1)

def JRFB_QA_Select():
    pg.click(x=835,y=548)
    time.sleep(1)
    pg.doubleClick(x=771,y=487)
    time.sleep(1)
    pg.doubleClick(x=866,y=591)
    time.sleep(1)
    pg.write("2015")
    time.sleep(1)
    pg.doubleClick(x=948,y=647)
    time.sleep(1)

def main():
    while 1:
        try:
            if keyboard.is_pressed('F1'):
                # login_POS_anon()
                # login_tsc()
                # tsc_Reports_reports()
                # login_GBF()
                # login_ANJ()
                login_JRFB()
                time.sleep(1)
            elif keyboard.is_pressed('F3'):
                # ANJ_Peration_outbound_fair_shear_wo()
                # POS_ANJ_purchase()
                # pg.write("warehousedbo")
                # ANJ_Report_report()
                JRFB_Operation_QA()
                JRFB_QA_Select()
                time.sleep(1)
            elif keyboard.is_pressed('F4'):
                pg.write("warehousedbo")
        except:
            break
        time.sleep(0.1)

main()


# login_software()
# INQUIRY_Outbound_DOQ()
# INQUIRY_Stock_status_IIQ()
# INQUIRY_Stock_status_PHQ()
# INQUIRY_Warehouse_WOSQ()
# INQUIRY_Warehouse_WUQ()


# pg.click(x=913,y=529)

# # pg.doubleClick(position) #double click
# # time.sleep(2) #delay 2000

# pg.write("similan")
# pg.hotkey('enter')
# pg.write("software")
# pg.hotkey('enter')
# pg.hotkey('enter')
# print("writed")


# position = pg.locateOnScreen("assetsbotNo1\IMG\btnOK.png")
# print(position)
# pg.click(position)