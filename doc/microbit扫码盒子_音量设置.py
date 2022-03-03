'''
    ME66扫码盒子线序
    从左往右
    黄 Vcc
    白 GND
    红 tx
    黑 rx
'''


from microbit import *
uart.init(baudrate = 115200, tx = pin2, rx = pin1)
def Set_VOLUME(n):
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
    elif m == 1:
        uart.write("<STX><0015><SET><01><00><VOLUME=1><ETX><57>")
    sleep(1000)
    data = uart.read()
    return data

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
