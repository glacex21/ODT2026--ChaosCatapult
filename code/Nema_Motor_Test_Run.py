from machine import Pin
import time

in1 = Pin(18, Pin.OUT)
in2 = Pin(27, Pin.OUT)
in3 = Pin(25, Pin.OUT)
in4 = Pin(19, Pin.OUT)

STEP_DELAY_US = 3000

sequence = [
    [1,1,0,0],
    [0,1,1,0],
    [0,0,1,1],
    [1,0,0,1],
]

while True:
    for s in sequence:
        in1.value(s[0])
        in2.value(s[1])
        in3.value(s[2])
        in4.value(s[3])
        time.sleep_us(STEP_DELAY_US)