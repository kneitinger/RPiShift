#!/usr/bin/env python
from time import sleep
import RPiShift
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(23, GPIO.IN)

Shiftr =RPiShift.Shiftr(15,11,13)
# Make sure everything is hooked up
def testFunc():
    # Test bit pushing
    for i in range(256**Shiftr.CHAIN):
        Shiftr.writeByte(i)
        Shiftr.writeLatch()
        sleep(.008)
    for i in range((256**Shiftr.CHAIN)-1,0,-1):
        Shiftr.writeByte(i)
        Shiftr.writeLatch()
        sleep(.008)
        
    # Test individual pin writing
    for i in range(4*Shiftr.CHAIN):
        Shiftr.writePin(i,1)
        sleep(.25)
        Shiftr.writePin(i+4,1)
        Shiftr.writePin(i,0)
        sleep(.25)
        Shiftr.writePin(i+4,0)

    # Test byte writing
    Shiftr.writeByte(0xFF)
    sleep(.25)
    Shiftr.writeByte(0x0F)
    sleep(.25)
    Shiftr.writeByte(0xF0)
    sleep(.25)
    Shiftr.cleanup()
testFunc()
