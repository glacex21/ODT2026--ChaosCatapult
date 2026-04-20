from applink import AppInventorLink
from machine import Pin
import time

app = AppInventorLink()

# -------- NEMA STEPPER --------
IN1 = Pin(18, Pin.OUT)
IN2 = Pin(27, Pin.OUT)
IN3 = Pin(25, Pin.OUT)
IN4 = Pin(19, Pin.OUT)

# LEDs
green = Pin(13, Pin.OUT)
red = Pin(12, Pin.OUT)

# IR sensor
ir = Pin(15, Pin.IN)

# state
last_command_time = time.ticks_ms()
timeout = 200
current_action = "stop"

calibrated = False
drop_triggered = False
close_triggered = False
gate_open = False

rewind_active = False
unwind_active = False

#  step sequence (NEMA)
step_seq = [
    [1,1,0,0],
    [0,1,1,0],
    [0,0,1,1],
    [1,0,0,1],
]

step_index = 0
STEP_DELAY = 0.003

# STEPPER 
def step(direction):
    global step_index
    step_index = (step_index + direction) % 4
    s = step_seq[step_index]

    IN1.value(s[0])
    IN2.value(s[1])
    IN3.value(s[2])
    IN4.value(s[3])

def stepper_stop():
    IN1.value(0)
    IN2.value(0)
    IN3.value(0)
    IN4.value(0)

def move_angle(angle):
    steps = int(abs(angle) * 200 / 360)
    direction = 1 if angle > 0 else -1

    for _ in range(steps):
        step(direction)
        time.sleep(STEP_DELAY)

# APP 
def handle_app_request(params):
    global last_command_time, current_action
    global calibrated, drop_triggered, close_triggered
    global rewind_active, unwind_active

    action = params.get("action")
    print("App:", action)

    if action == "done":
        calibrated = True
        stepper_stop()
        green.value(1)
        return {"status": "locked"}

    if action == "drop":
        if calibrated:
            drop_triggered = True
        return {"status": "drop"}

    if action == "close":
        if calibrated:
            close_triggered = True
        return {"status": "close"}

    if action == "rewind":
        rewind_active = True
        unwind_active = False
        return {"status": "rewind"}

    if action == "unwind":
        unwind_active = True
        rewind_active = False
        return {"status": "unwind"}

    if action == "stop_motor":
        rewind_active = False
        unwind_active = False
        stepper_stop()
        return {"status": "stopped"}

    if calibrated:
        return {"status": "locked"}

    last_command_time = time.ticks_ms()
    current_action = action
    return {"status": action}

app.start_ap("CATAPULT", "12345678")
app.on_request(handle_app_request)

green.value(0)
red.value(0)
stepper_stop()

#  MAIN LOOP 
while True:
    app.process()
    now = time.ticks_ms()

    #  MANUAL GATE SETUP 
    if not calibrated:

        if current_action == "left":
            step(-1)
            red.value(1)
            green.value(0)
            time.sleep(STEP_DELAY)

        elif current_action == "right":
            step(1)
            green.value(1)
            red.value(0)
            time.sleep(STEP_DELAY)

        else:
            red.value(0)
            green.value(0)

        if time.ticks_diff(now, last_command_time) > timeout:
            current_action = "stop"
            stepper_stop()

    else:

        #  DROP (OPEN GATE) 
        if drop_triggered and not gate_open:
            move_angle(-90)
            stepper_stop()
            gate_open = True
            drop_triggered = False

        #  CLOSE 
        if close_triggered and gate_open:
            move_angle(90)
            stepper_stop()
            gate_open = False
            green.value(1)
            close_triggered = False

        #  REWIND (WITH IR STOP) 
        if rewind_active:
            if ir.value() == 1:
                step(-1)
                red.value(1)
                time.sleep(STEP_DELAY)
            else:
                stepper_stop()
                rewind_active = False
                red.value(0)

        # UNWIND 
        elif unwind_active:
            step(1)
            green.value(1)
            time.sleep(STEP_DELAY)

        else:
            stepper_stop()
            red.value(0)
            green.value(0)

    time.sleep(0.001)