#!/usr/bin/env python
from time import sleep
import RPiShift
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(23, GPIO.IN)

Shiftr = RPiShift.Shiftr(15,11,13)
# Make sure everything is hooked up
def testFunc():
    # Test byte writing by counting up and down in binary
    for i in range(256**Shiftr.CHAIN):
        Shiftr.writeByte(i)
        sleep(.008)
    for i in range((256**Shiftr.CHAIN)-1,0,-1):
        Shiftr.writeByte(i)
        sleep(.008)

    # Test individual pin writing
    for i in range(4*Shiftr.CHAIN):
        Shiftr.writePin(i,1)
        sleep(.25)
        Shiftr.writePin(i+4,1)
        Shiftr.writePin(i,0)
        sleep(.25)
        Shiftr.writePin(i+4,0)

    # Turn on every other pin
    Shiftr.writeByte(0x55)
    # Toggle between 0b01010101 and 0b10101010
    for i in range(8):
        for j in range(8):
            Shiftr.togglePin(j)
        sleep(.125)

testFunc()
Shiftr.cleanup()
