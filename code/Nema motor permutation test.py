from machine import Pin
import time

# available pins
pins = [18, 25, 27, 19]

# all 24 permutations manually listed
permutations = [
    [18,25,27,19],[18,25,19,27],[18,27,25,19],[18,27,19,25],[18,19,25,27],[18,19,27,25],
    [25,18,27,19],[25,18,19,27],[25,27,18,19],[25,27,19,18],[25,19,18,27],[25,19,27,18],
    [27,18,25,19],[27,18,19,25],[27,25,18,19],[27,25,19,18],[27,19,18,25],[27,19,25,18],
    [19,18,25,27],[19,18,27,25],[19,25,18,27],[19,25,27,18],[19,27,18,25],[19,27,25,18]
]

STEP_DELAY_US = 2000

sequence = [
    [1,1,0,0],
    [0,1,1,0],
    [0,0,1,1],
    [1,0,0,1],
]

while True:
    for p in permutations:
        print("\nTESTING PINS:", p)

        in1 = Pin(p[0], Pin.OUT)
        in2 = Pin(p[1], Pin.OUT)
        in3 = Pin(p[2], Pin.OUT)
        in4 = Pin(p[3], Pin.OUT)

        # run each combo for some steps
        for _ in range(200):
            for s in sequence:
                in1.value(s[0])
                in2.value(s[1])
                in3.value(s[2])
                in4.value(s[3])
                time.sleep_us(STEP_DELAY_US)

        # small pause before next combo
        time.sleep(1)