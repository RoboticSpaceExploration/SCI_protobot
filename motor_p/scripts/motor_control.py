#!/usr/bin/python2

import serial
import time

serialPort = "/dev/ttyArduinoMega" # on jetson TX2

def motors_init():
    global arduino	
    arduino = serial.Serial(port=serialPort, baudrate=9600, timeout=0.1)

def motors_quit():
	arduino.close()

def toggle_motors(cmd):
        arduino.write(chr(0))
        time.sleep(0.1)
	arduino.write(chr(int(cmd)+48))
	time.sleep(0.1)

