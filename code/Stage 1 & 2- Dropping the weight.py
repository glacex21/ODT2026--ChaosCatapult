from applink import AppInventorLink
from machine import Pin
import time

app = AppInventorLink()

# GATE STEPPER
IN1 = Pin(21, Pin.OUT)
IN2 = Pin(19, Pin.OUT)
IN3 = Pin(18, Pin.OUT)
IN4 = Pin(5, Pin.OUT)

#  LEDs 
green = Pin(13, Pin.OUT)
red = Pin(12, Pin.OUT)

#  DC MOTORS 
m1a = Pin(26, Pin.OUT)
m1b = Pin(33, Pin.OUT)

m2a = Pin(32, Pin.OUT)
m2b = Pin(25, Pin.OUT)

#  STATE 
last_command_time = time.ticks_ms()
timeout = 200
current_action = "stop"

calibrated = False
drop_triggered = False
gate_open = False

#  STEPPER SEQUENCE 
step_seq = [
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]
]

step_index = 0

def step_forward():
    global step_index
    seq = step_seq[step_index]
    IN1.value(seq[0])
    IN2.value(seq[1])
    IN3.value(seq[2])
    IN4.value(seq[3])
    step_index = (step_index + 1) % 4

def step_backward():
    global step_index
    step_index = (step_index - 1) % 4
    seq = step_seq[step_index]
    IN1.value(seq[0])
    IN2.value(seq[1])
    IN3.value(seq[2])
    IN4.value(seq[3])

def stepper_stop():
    IN1.value(0)
    IN2.value(0)
    IN3.value(0)
    IN4.value(0)


def move_angle(angle, speed):
    global step_index

    steps = int(angle * 512 / 360 * 4)
    direction = 1 if steps > 0 else -1
    steps = abs(steps)

    led_toggle = False

    for _ in range(steps):
        step_index = (step_index + direction) % 4
        step = step_seq[step_index]

        IN1.value(step[0])
        IN2.value(step[1])
        IN3.value(step[2])
        IN4.value(step[3])

       
        if led_toggle:
            green.value(1)
            red.value(0)
        else:
            green.value(0)
            red.value(1)

        led_toggle = not led_toggle

        time.sleep(speed/1000)

    
    green.value(0)
    red.value(0)

#  MOTOR CONTROL 
def motors_forward():
    m1a.value(1); m1b.value(0)
    m2a.value(1); m2b.value(0)

def motors_stop():
    m1a.value(0); m1b.value(0)
    m2a.value(0); m2b.value(0)

#  APP HANDLER 
def handle_app_request(params):
    global last_command_time, current_action, calibrated, drop_triggered

    action = params.get("action")
    print("App:", action)

    if action == "done":
        calibrated = True
        current_action = "stop"
        stepper_stop()
        green.value(1)   # 🟢 stays ON
        red.value(0)
        print("Calibration locked")
        return {"status": "locked"}

    if action == "drop":
        if calibrated:
            drop_triggered = True
            print("Drop triggered")
        return {"status": "drop"}

    if calibrated:
        return {"status": "locked"}

    last_command_time = time.ticks_ms()
    current_action = action

    return {"status": action}

#  INIT 
app.start_ap("CATAPULT", "12345678")
app.on_request(handle_app_request)

print("System ready")

green.value(0)
red.value(0)
motors_stop()
stepper_stop()

#  MAIN LOOP 
while True:
    app.process()

    now = time.ticks_ms()

    #  STAGE 0 
    if not calibrated:

        if current_action == "left":
            step_backward()
            red.value(1)     #LEFT led
            green.value(0)
            time.sleep(0.003)

        elif current_action == "right":
            step_forward()
            green.value(1)   # RIGHT led
            red.value(0)
            time.sleep(0.003)

        else:
            # idle
            red.value(0)
            green.value(0)

        if time.ticks_diff(now, last_command_time) > timeout:
            current_action = "stop"
            stepper_stop()
            red.value(0)
            green.value(0)

    # -------- STAGE 1 & 2 --------
    else:

        if drop_triggered:

            if not gate_open:
                print("Stage 1 ready")
                time.sleep(1)

                print("Stage 2 opening gate")

                move_angle(-90, 2)   #blinking

                stepper_stop()
                print("Gate opened")

                gate_open = True

                # start motors after drop
                motors_forward()

            else:
                print("Gate already open")

            drop_triggered = False

    time.sleep(0.001)
