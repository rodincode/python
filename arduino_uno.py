# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 09:40:58 2019

@author: LENOVO
"""

import pyfirmata
board=pyfirmata.Arduino("COM3")
#board.digital[13].write(1)
#board.exit()
pir_pin=board.get_pin("d:7:i")
it=pyfirmata.util.Iterator(board)
it.start()

while True:
    value=pir_pin.read()
    if value is None:
        print("NO Value")
    elif value is True:
        print("Motion Detected")
    else:
        print("No Motion Detected")