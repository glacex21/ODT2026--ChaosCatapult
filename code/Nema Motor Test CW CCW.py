from machine import Pin
import time

in1 = Pin(18, Pin.OUT)
in2 = Pin(25, Pin.OUT)
in3 = Pin(27, Pin.OUT)
in4 = Pin(19, Pin.OUT)

STEP_DELAY_US = 2500

sequence = [
    [1,1,0,0],
    [0,1,1,0],
    [0,0,1,1],
    [1,0,0,1],
]

index = 0

while True:

    # ---- CLOCKWISE ----
    for _ in range(200):
        s = sequence[index]
        
        in1.value(s[0])
        in2.value(s[1])
        in3.value(s[2])
        in4.value(s[3])
        
        index = (index + 1) % 4
        time.sleep_us(STEP_DELAY_US)

    # 🔥 reset magnetic field
    in1.value(0); in2.value(0); in3.value(0); in4.value(0)
    time.sleep_ms(100)

    # ---- ANTICLOCKWISE ----
    for _ in range(200):
        s = sequence[index]
        
        in1.value(s[0])
        in2.value(s[1])
        in3.value(s[2])
        in4.value(s[3])
        
        index = (index - 1) % 4
        time.sleep_us(STEP_DELAY_US)

    # 🔥 reset again
    in1.value(0); in2.value(0); in3.value(0); in4.value(0)
    time.sleep_ms(100)