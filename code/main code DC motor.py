from applink import AppInventorLink
from machine import Pin, PWM
import time

app = AppInventorLink()

# stepper (gate)
IN1 = Pin(21, Pin.OUT)
IN2 = Pin(19, Pin.OUT)
IN3 = Pin(18, Pin.OUT)
IN4 = Pin(5, Pin.OUT)

# LEDs
green = Pin(13, Pin.OUT)
red = Pin(12, Pin.OUT)

# DC motor (PWM)
in3 = PWM(Pin(26), freq=1000)
in4 = PWM(Pin(27), freq=1000)

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

# stepper sequence
step_seq = [
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]
]

step_index = 0

#  STEPPER 
def step_forward():
    global step_index
    s = step_seq[step_index]
    IN1.value(s[0]); IN2.value(s[1]); IN3.value(s[2]); IN4.value(s[3])
    step_index = (step_index + 1) % 4

def step_backward():
    global step_index
    step_index = (step_index - 1) % 4
    s = step_seq[step_index]
    IN1.value(s[0]); IN2.value(s[1]); IN3.value(s[2]); IN4.value(s[3])

def stepper_stop():
    IN1.value(0); IN2.value(0); IN3.value(0); IN4.value(0)

def move_angle(angle, speed):
    global step_index
    steps = int(angle * 512 / 360 * 4)
    direction = 1 if steps > 0 else -1
    steps = abs(steps)

    for _ in range(steps):
        step_index = (step_index + direction) % 4
        s = step_seq[step_index]
        IN1.value(s[0]); IN2.value(s[1]); IN3.value(s[2]); IN4.value(s[3])
        time.sleep(speed/1000)

#  DC MOTOR 
def motor_ccw():
    in3.duty(512)
    in4.duty(0)

def motor_cw():
    in3.duty(0)
    in4.duty(512)

def motor_stop():
    in3.duty(0)
    in4.duty(0)

#  APP 
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
        motor_stop()
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
motor_stop()
stepper_stop()

# MAIN LOOP 
while True:
    app.process()
    now = time.ticks_ms()

    # Stage 0–1: Manual gate setup
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

        # DROP → full automatic sequence
        if drop_triggered and not gate_open:

            move_angle(-90, 2)
            stepper_stop()
            gate_open = True

            # rewind until IR
            while ir.value() == 1:
                motor_ccw()
                red.value(1)
                time.sleep(0.2)
                red.value(0)

            motor_stop()

            # release for 5 sec
            start = time.time()
            while time.time() - start < 5:
                motor_cw()
                green.value(1)
                time.sleep(0.2)
                green.value(0)

            motor_stop()
            drop_triggered = False

        # CLOSE gate
        if close_triggered and gate_open:
            motor_stop()
            move_angle(90, 2)
            stepper_stop()
            gate_open = False
            green.value(1)
            close_triggered = False

        #  MANUAL MOTOR CONTROL 

        if rewind_active:
            if ir.value() == 1:
                motor_ccw()
                red.value(1)
            else:
                motor_stop()
                rewind_active = False
                red.value(0)

        elif unwind_active:
            motor_cw()
            green.value(1)

        else:
            motor_stop()
            red.value(0)
            green.value(0)

    time.sleep(0.001)