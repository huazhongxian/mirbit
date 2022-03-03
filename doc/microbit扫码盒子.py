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
