#RPiShift

A python module for interfacing a 595 shift register with the Raspberry Pi

#Installation
You can install RPiShift one of two ways:
* Using **pip**:
```sh
$: pip install RPiShift
```

* Using setup.py and **setuptools**:
```sh
$: git clone git@github.com:kneitinger/RPiShift.git
$: ./setup.py install RPiShift
```
#Usage

## Hardware
To use RPiShift attach a 595 chip as indicated by the following schematic ![595_Pi_schematic](./schematics/generic_schematic.jpg)

## Software

###Initializing the module
If the 595 is only device attached to the GPIO pins of the Raspberry Pi, begin
by importing the RPiShift module
```python
import RPiShift
```
After that call the shiftr initialization function to configure the pins:
```python
# Argument list
# Shiftr(dataPin, clockPin, latchPin, [chainLength], [boardMode])
# Args in [] are optional and default to 1 and GPIO.BOARD respectively
shift = RPiShift.Shiftr(11,13,15)
```

###Writing bytes
To write a byte to the shift register simply call the writeByte method with the
desired value to write:
```python
# Turn on all LEDs (with only one 595 in the chain)
shift.writeByte(0xFF)
# Turn off all LEDs
shift.writeByte(0x00)
# Display a binary 37 (00100101)
shift.writeByte(37)
# Display every 4 LEDs in a 4-chain circuit
shift.writeByte(0x0F0F0F0F)
```
Currently there is no bounds checking, so be sure you're writing the correct
amount of digits for the length of your chain: 2 hex digits or 8 binary
digits per 595.

###Toggling pins
