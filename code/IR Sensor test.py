from machine import Pin
import time

ir = Pin(15, Pin.IN)

while True:
    state = ir.value()
    print("IR:", state)
    time.sleep(0.2)