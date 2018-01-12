import utime
import machine
pin15 = machine.Pin(15, machine.Pin.OUT)
while True:
        pin15.value(1)
        utime.sleep_ms(500)
        pin15.value(0)
        utime.sleep_ms(500)