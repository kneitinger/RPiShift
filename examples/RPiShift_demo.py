#!/usr/bin/env python
# RPiShift_demo.py - A script to demonstrate the functions of the RPiShift
# module for 595 shift registers and the Raspberry Pi
# Copyright (c) 2014 Kyle Kneitinger
# kylejkneitinger@gmail.com

from time import sleep
import RPiShift

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

    # Clear the register
    Shiftr.writeByte(0x00)
    # Manually toggle latch on each bit to push data "into" the outputs
    for i in range(16):
        Shiftr.pushBit( ((i+1)%8)==1)
        Shiftr.writeLatch()
        sleep(.1)

# Catch ^C and cleanup pins before exiting
try:
    testFunc()
except KeyboardInterrupt:
    Shiftr.cleanup()
    exit(1)
Shiftr.cleanup()
