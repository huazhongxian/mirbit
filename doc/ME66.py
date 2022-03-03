'''
    ME66扫码盒子线序
    从左往右
    黄 Vcc
    白 GND
    红 tx
    黑 rx
'''


from microbit import *

def Set_Volume(n):
    '''
    # 设置串口音量
    0: <STX><0015><SET><01><00><VOLUME=0><ETX><56>
    1: <STX><0015><SET><01><00><VOLUME=1><ETX><57>
    2: <STX><0015><SET><01><00><VOLUME=2><ETX><54>
    3: <STX><0015><SET><01><00><VOLUME=3><ETX><55>
    4: <STX><0015><SET><01><00><VOLUME=4><ETX><52>
    5: <STX><0015><SET><01><00><VOLUME=5><ETX><53>
    '''
    if n == 0:
        uart.write("<STX><0015><SET><01><00><VOLUME=0><ETX><56>")
    elif n == 1:
        uart.write("<STX><0015><SET><01><00><VOLUME=1><ETX><57>")
    elif n == 2:
        uart.write("<STX><0015><SET><01><00><VOLUME=2><ETX><54>")
    elif n == 3:
        uart.write("<STX><0015><SET><01><00><VOLUME=3><ETX><55>")
    elif n == 4:
        uart.write("<STX><0015><SET><01><00><VOLUME=4><ETX><52>")
    elif n == 5:
        uart.write("<STX><0015><SET><01><00><VOLUME=4><ETX><52>")
    while True:
        if uart.any():
            data = uart.read()
            # display.scroll(data)
    return data


def Reset():
    '''
    重置ME66
    ON: <STX><0015><SET><01><00><RESET=ON><ETX><3A>
    OFF: <STX><0016><SET><01><00><RESET=OFF><ETX><77>
    '''
    uart.write("<STX><0015><SET><01><00><RESET=ON><ETX><3A>")
    while True:
        if uart.any():
            data = uart.read()
            # display.scroll(data)
    return data

def Prompt(switch):
    '''
    提示音
    ON：<STX><0020><SET><01><00><PROMPT=0002ON><ETX><6F>
    OFF：<STX><0021><SET><01><00><PROMPT=0003OFF><ETX><21>
    '''
    if switch == 0 :
        uart.write("<STX><0021><SET><01><00><PROMPT=0003OFF><ETX><21>")
    elif switch == 1 :
        uart.write("<STX><0020><SET><01><00><PROMPT=0002ON><ETX><6F>")
    while True:
        if uart.any():
            data = uart.read()
            # display.scroll(data)
    return data

if __name__ == "__main__":
    sleep(1000)
    uart.init(baudrate = 115200, tx = pin16, rx = pin15)
    while True:
        '''
        data = eval('{"SKU":1001,"Name_CN":"可乐","Name_EN":"cola","Price":3.00}')
        display.scroll(data["Price"])
        '''
        if uart.any():
            data = str(uart.read(),'utf-8')
            try:
                data = eval(data)
                display.scroll(data["Price"])
            except:
                pass
