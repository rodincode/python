# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 12:16:42 2019

@author: ACER
"""

# Import Required Libraries
import pyfirmata
from time import sleep

# Define custom function to perform Blink action
def blinkLED(pin, message):
    print(message)
    board.digital[pin].write(1)
    sleep(1)
    board.digital[pin].write(0)
    sleep(1)
	
# Associate port and board with Pyfirmata
board = pyfirmata.Arduino('COM3')

# Define Pins
pirPin = board.get_pin('d:7:i') #d is the digital pin, 7 is the pin number and i is the input pin
redPin = 12
greenPin = 13


# Run the Iterator. Otherwise the values are not updated from the serial data.
it = pyfirmata.util.Iterator(board)
it.start()

# Check continusly for PIR Sensor input  
while True:
    value = pirPin.read()
    #print(value)
    if value is None: #	Ignore case	when receiving None value from pin. Usually when the program starts, introduced due to delay
        #print("No value")
        pass
    if value is True:
        #print("Motion Detected")
        blinkLED(redPin, "Motion Detected")
    else:
        blinkLED(greenPin, "No motion Detected")
        #print("No motion detected")
        
# Release the board and the connections so that program can restart from python. Otherwise restart ipython console. 
board.exit()
    
    