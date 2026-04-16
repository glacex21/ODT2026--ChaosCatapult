from applink import AppInventorLink
from machine import Pin
import time

app = AppInventorLink()

in1 = Pin(25, Pin.OUT)  # motor IN1
in2 = Pin(26, Pin.OUT)  # motor IN2

green = Pin(18, Pin.OUT)  # green LED
red = Pin(19, Pin.OUT)    # red LED

state = "stop"  
last_blink = time.ticks_ms()  
led_on = False  

def motor_cw():
    print("CW")
    in1.value(1)
    in2.value(0)

def motor_ccw():
    print("CCW")
    in1.value(0)
    in2.value(1)

def motor_stop():
    print("STOP")
    in1.value(0)
    in2.value(0)
    green.value(0)
    red.value(0)

def handle_app_request(params):
    global state
    print("App:", params)

    if params.get("action") == "cw":
        state = "cw"
        motor_cw()
        return {"status": "cw"}

    elif params.get("action") == "ccw":
        state = "ccw"
        motor_ccw()
        return {"status": "ccw"}

    elif params.get("action") == "stop":
        state = "stop"
        motor_stop()
        return {"status": "stop"}

    return {"status": "ok"}

app.start_ap("ESP32", "12345678")  # wifi name/password
app.on_request(handle_app_request)

print("Ready")

while True:
    app.process()

    now = time.ticks_ms()

    if state == "cw":
        if time.ticks_diff(now, last_blink) > 300:
            last_blink = now
            led_on = not led_on
            green.value(1 if led_on else 0)
            red.value(0)
            print("GREEN")

    elif state == "ccw":
        if time.ticks_diff(now, last_blink) > 300:
            last_blink = now
            led_on = not led_on
            red.value(1 if led_on else 0)
            green.value(0)
            print("RED")

    time.sleep(0.01)