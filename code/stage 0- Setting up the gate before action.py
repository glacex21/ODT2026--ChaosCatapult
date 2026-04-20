from applink import AppInventorLink
from machine import Pin
import time

app = AppInventorLink()

# STEPPER PINS 
IN1 = Pin(21, Pin.OUT)
IN2 = Pin(19, Pin.OUT)
IN3 = Pin(18, Pin.OUT)
IN4 = Pin(5, Pin.OUT)

green = Pin(4, Pin.OUT)

# STATE 
last_command_time = time.ticks_ms()
timeout = 200
current_action = "stop"
calibrated = False   # LOCK 

#  STEPPER SEQUENCE 
step_seq = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1]
]

step_index = 0

def step_forward():
    global step_index
    seq = step_seq[step_index]
    IN1.value(seq[0])
    IN2.value(seq[1])
    IN3.value(seq[2])
    IN4.value(seq[3])
    step_index = (step_index + 1) % 8

def step_backward():
    global step_index
    step_index = (step_index - 1) % 8
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

#  APP HANDLER 
def handle_app_request(params):
    global last_command_time, current_action, calibrated

    action = params.get("action")
    print("App:", action)

    #  DONE BUTTON 
    if action == "done":
        calibrated = True
        current_action = "stop"
        stepper_stop()
        green.value(1)  # show locked
        print("Calibration LOCKED")
        return {"status": "locked"}

    #  BLOCK MANUAL AFTER LOCK 
    if calibrated:
        return {"status": "locked"}

    #  NORMAL MANUAL CONTROL 
    last_command_time = time.ticks_ms()
    current_action = action

    return {"status": action}

# WIFI 
app.start_ap("CATAPULT", "12345678")
app.on_request(handle_app_request)

print("Calibration Mode Ready")

green.value(0)
stepper_stop()

# LOOP 
while True:
    app.process()

    now = time.ticks_ms()

    if current_action == "left":
        step_backward()
        time.sleep(0.003)

    elif current_action == "right":
        step_forward()
        time.sleep(0.003)

    # AUTO STOP
    if time.ticks_diff(now, last_command_time) > timeout:
        current_action = "stop"
        stepper_stop()

    time.sleep(0.001)
