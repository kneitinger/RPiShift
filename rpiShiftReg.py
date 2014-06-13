#! /usr/bin/env python
# rpiShiftReg
# Using the 595 shift register with the Raspberry Pi
# Copyright (C) 2014 Kyle J. Kneitinger

import RPi.GPIO as GPIO
import random
from time import sleep

random.seed()

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

# Make sure everything is hooked up
def testFunc():
    for i in range(256):
        pushBit(random.getrandbits(1))
        if (i+1)%(8*CHAIN) == 0:
            writeLatch()
            sleep(.125)

testFunc()
GPIO.cleanup()
exit
