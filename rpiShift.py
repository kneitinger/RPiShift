#! /usr/bin/env python
# rpiShiftReg
# Using the 595 shift register with the Raspberry Pi
# Copyright (C) 2014 Kyle J. Kneitinger

import RPi.GPIO as GPIO
from time import sleep

# Rpi Pin Definitions
CLOCK=11
LATCH=13
DS=15

# How many 595s are connected to Rpi
CHAIN=1
# Value store in 595's storage register
STORED=0x00

# Setup pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(DS, GPIO.OUT)
GPIO.setup(LATCH, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(CLOCK, GPIO.OUT, initial=GPIO.LOW)

# Push a single bit into the registers
# writeLatch must be called after 8*CHAIN pushes
def pushBit(state):
    GPIO.output(CLOCK, 0)
    sleep(0)
    GPIO.output(DS, state)
    GPIO.output(CLOCK, 1)

# Transfer bits from shift register to storage register
def writeLatch():
    GPIO.output(LATCH, 1)
    GPIO.output(LATCH, 0)

# Write a byte of length 8*CHAIN to the 595
def writeByte(value):
    global STORED
    for i in range(8*CHAIN):
        bit = (value << i) & (0x80 << 2*(CHAIN-1))
        pushBit( bit )
    writeLatch()
    STORED=value

# High level write to a single pin
def writePin(pin, value):
    global STORED
    oldVal = (STORED >> pin) & 0x01
    if oldVal != value:
        writeByte(STORED ^ (0x01 << pin) )

# Make sure everything is hooked up
def testFunc():
    # Test bit pushing
    for i in range(256**CHAIN):
        writeByte(i)
        writeLatch()
        sleep(.008)
    for i in range((256**CHAIN)-1,0,-1):
        writeByte(i)
        writeLatch()
        sleep(.008)

    # Test individual pin writing
    for i in range(4*CHAIN):
        writePin(i,1)
        sleep(.25)
        writePin(i+4,1)
        sleep(.25)
        writePin(i,0)
        sleep(.25)
        writePin(i+4,0)
        sleep(.25)

    # Test byte writing
    writeByte(0xFF**CHAIN)
    sleep(.25)
    writeByte(0x0F**CHAIN)
    sleep(.25)
    writeByte(0xF0**CHAIN)
    sleep(.25)

testFunc()
GPIO.cleanup()
exit
