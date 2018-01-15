import is31fl3731
import machine 
#import I2C, Pin
i2c = machine.I2C(sda=machine.Pin(21), scl=machine.Pin(22))
display = is31fl3731.Matrix(i2c)

display.blink(500)
display.fill(255, blink=True)
display.fill(0)

display.pixel(0,0,127)
display.pixel(1,1,127)