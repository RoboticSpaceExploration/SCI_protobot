#!/usr/bin/python3

import serial                                               # import pyserial 

ser = serial.Serial('COM3', baudrate = 9600, timeout = 1)   # COM3 is the serial communication port specific to the computer
                                                            # baudrate matches the rate in the arduino code
                                                            # timeout is the number of seconds to wait for serial input  



while 1:                                                    # this while loop runs indefinitely until you exit the script

    arduinoData = ser.readline().decode('ascii')            # utilize the readline function to read the information comming in serially until EOL
                                                            # decode returns the information in ascii 
    print(arduinoData)                                      # print information

