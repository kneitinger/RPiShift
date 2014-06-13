#! /usr/bin/env python
# Using the 595 shift register with the Raspberry Pi
# Copyright (C) 2014 Kyle J. Kneitinger

import RPi.GPIO as GPIO
import time, random

CLOCK=11
LATCH=13
DS=15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(DS, GPIO.OUT)
GPIO.setup(LATCH, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(CLOCK, GPIO.OUT, initial=GPIO.LOW)

random.seed()

def writeBit(state):
    GPIO.output(CLOCK, 0)
    time.sleep(0)
    GPIO.output(DS, state)
    GPIO.output(CLOCK, 1)

def writeLatch():
    GPIO.output(LATCH, 1)
    GPIO.output(LATCH, 0)

for i in range(10000):
    writeBit(random.getrandbits(1) )
    if (i+1)%8 == 0:
        writeLatch()

GPIO.cleanup()
exit
