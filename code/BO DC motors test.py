from machine import Pin
import time

# Motor 1
m1a = Pin(26, Pin.OUT)
m1b = Pin(33, Pin.OUT)

# Motor 2
m2a = Pin(32, Pin.OUT)
m2b = Pin(25, Pin.OUT)

print("Motors ON")

# forward
m1a.value(1)
m1b.value(0)

m2a.value(1)
m2b.value(0)
