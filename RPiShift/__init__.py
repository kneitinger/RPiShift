#! /usr/bin/env python
# RpiShift
# Using the 595 shift register with the Raspberry Pi
# Copyright (C) 2014 Kyle J. Kneitinger

import RPi.GPIO as GPIO
from time import sleep
class Shiftr:
    def __init__(self, dataPin, clockPin, latchPin, chain = 1,
            boardMode = GPIO.BOARD):
        self.DATA = dataPin
        self.CLOCK = clockPin
        self.LATCH = latchPin
        self.CHAIN = chain
        self.BOARDMODE = boardMode

        # Value store in 595's storage register
        self.STORED=0x00

        # Setup pins
        GPIO.setmode(self.BOARDMODE)
        GPIO.setup(self.DATA, GPIO.OUT)
        GPIO.setup(self.LATCH, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.CLOCK, GPIO.OUT, initial=GPIO.LOW)

    # Push a single bit into the registers
    # writeLatch must be called after 8*CHAIN pushes
    def pushBit(self,state):
        GPIO.output(self.CLOCK, 0)
        sleep(0)
        GPIO.output(self.DATA, state)
        GPIO.output(self.CLOCK, 1)

    # Transfer bits from shift register to storage register
    def writeLatch(self):
        GPIO.output(self.LATCH, 1)
        GPIO.output(self.LATCH, 0)

    # Write a byte of length 8*CHAIN to the 595
    def writeByte(self,value):
        self.STORED
        for i in range(8*self.CHAIN):
            bit = (value << i) & (0x80 << 2*(self.CHAIN-1))
            self.pushBit( bit )
        self.writeLatch()
        self.STORED=value

    # High level write to a single pin
    def writePin(self, pin, value):
        self.STORED
        oldVal = (self.STORED >> pin) & 0x01
        if oldVal != value:
            self.writeByte(self.STORED ^ (0x01 << pin) )

    # Toggle the state of a single pin
    def togglePin(self, pin):
        self.writeByte(self.STORED ^ (0x01 << pin))

    # Clean up pins
    def cleanup(self):
        GPIO.cleanup()

