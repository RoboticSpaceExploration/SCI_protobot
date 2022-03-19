#! /usr/bin/python3

# import Jetson.GPIO as GPIO
import pin_setting
import run_motor
from pynput import keyboard
from time import sleep

## Set the pins here ##
pwm1 = 5 # pulse width modulation 
dir1 = 6
brk1 = 13
pwm2 = 16
dir2 = 20
brk2 = 21
pin_setting.setup(pwm1,dir1,brk1,pwm2,dir2,brk2)
sleep(3)

# The on_press function detects the key pressed 
# if it is a letter output the character 
# else it is a special character so out put the key
def on_press(key):
    try:
        #print('Alphanumeric key pressed: {0} '.format( #for debugging 
           # key.char))
        if key.char == ('f'):
            run_motor.runMotor("f",pwm1,dir1,pwm2,dir2)

        if key.char == ('b'):
            run_motor.runMotor("b",pwm1,dir1,pwm2,dir2)

    except AttributeError:
        print('special key pressed: {0}'.format(
            key))
# The on_release function detects the key released 
# print the key released
# if the key is equal to esc then exit 
def on_release(key):
    print('Key released: {0}'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
# keyboard.Listener is a thread.
# a thread is used to run multiple threads (tasks, function calls) at the same time.
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

#GPIO.cleanup()