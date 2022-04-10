#!/usr/bin/python2

import serial
import time

global arduino
serialPort = "/dev/ttyArduinoUno" # on jetson TX2

def motors_init():
	arduino = serial.Serial(port=serialPort, baudrate=9600, timeout=0.1)

def motors_quit():
	arduino.close()

def toggle_motors(cmd):
	arduino.write(bytes(cmd, 'ascii'))
	time.sleep(0.1)

