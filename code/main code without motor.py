from applink import AppInventorLink
from machine import Pin
import time

app = AppInventorLink()

# gate stepper
IN1 = Pin(21, Pin.OUT)
IN2 = Pin(19, Pin.OUT)
IN3 = Pin(18, Pin.OUT)
IN4 = Pin(5, Pin.OUT)

# leds
green = Pin(13, Pin.OUT)
red = Pin(12, Pin.OUT)

# dc motors
m1a = Pin(26, Pin.OUT)
m1b = Pin(33, Pin.OUT)

m2a = Pin(32, Pin.OUT)
m2b = Pin(25, Pin.OUT)

# state
last_command_time = time.ticks_ms()
timeout = 200
current_action = "stop"

calibrated = False
drop_triggered = False
close_triggered = False
gate_open = False

# stepper sequence
step_seq = [
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]
]

step_index = 0

def step_forward():
    global step_index
    s = step_seq[step_index]
    IN1.value(s[0])
    IN2.value(s[1])
    IN3.value(s[2])
    IN4.value(s[3])
    step_index = (step_index + 1) % 4

def step_backward():
    global step_index
    step_index = (step_index - 1) % 4
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

def move_angle(angle, speed):
    global step_index

    steps = int(angle * 512 / 360 * 4)
    direction = 1 if steps > 0 else -1
    steps = abs(steps)

    led_toggle = False

    for _ in range(steps):
        step_index = (step_index + direction) % 4
        s = step_seq[step_index]

        IN1.value(s[0])
        IN2.value(s[1])
        IN3.value(s[2])
        IN4.value(s[3])

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

def move_angle_close(angle, speed):
    global step_index

    steps = int(angle * 512 / 360 * 4)
    direction = 1 if steps > 0 else -1
    steps = abs(steps)

    for _ in range(steps):
        step_index = (step_index + direction) % 4
        s = step_seq[step_index]

        IN1.value(s[0])
        IN2.value(s[1])
        IN3.value(s[2])
        IN4.value(s[3])

        red.value(1)
        time.sleep(0.001)
        red.value(0)

        time.sleep(speed/1000)

    red.value(0)

def motors_forward():
    m1a.value(1)
    m1b.value(0)
    m2a.value(1)
    m2b.value(0)

def motors_stop():
    m1a.value(0)
    m1b.value(0)
    m2a.value(0)
    m2b.value(0)

def handle_app_request(params):
    global last_command_time, current_action
    global calibrated, drop_triggered, close_triggered

    action = params.get("action")
    print("App:", action)

    if action == "done":
        calibrated = True
        stepper_stop()
        green.value(1)
        red.value(0)
        return {"status": "locked"}

    if action == "drop":
        if calibrated:
            drop_triggered = True
        return {"status": "drop"}

    if action == "close":
        if calibrated:
            close_triggered = True
        return {"status": "close"}

    if calibrated:
        return {"status": "locked"}

    last_command_time = time.ticks_ms()
    current_action = action
    return {"status": action}

app.start_ap("CATAPULT", "12345678")
app.on_request(handle_app_request)

green.value(0)
red.value(0)
motors_stop()
stepper_stop()

while True:
    app.process()
    now = time.ticks_ms()

    if not calibrated:

        if current_action == "left":
            step_backward()
            red.value(1)
            green.value(0)
            time.sleep(0.003)

        elif current_action == "right":
            step_forward()
            green.value(1)
            red.value(0)
            time.sleep(0.003)

        else:
            red.value(0)
            green.value(0)

        if time.ticks_diff(now, last_command_time) > timeout:
            current_action = "stop"
            stepper_stop()

    else:

        if drop_triggered and not gate_open:
            move_angle(-90, 2)
            stepper_stop()
            gate_open = True
            motors_forward()
            drop_triggered = False

        if close_triggered and gate_open:
            motors_stop()
            move_angle_close(90, 2)
            stepper_stop()
            gate_open = False
            green.value(1)
            close_triggered = False

    time.sleep(0.001)