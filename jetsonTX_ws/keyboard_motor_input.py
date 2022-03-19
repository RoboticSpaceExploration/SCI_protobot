#! /usr/bin/python3

# keyboard_motor_input.py 
# reads the input from the keyboard

from pynput import keyboard

print("Initializing detecting keyboard input...")

# The on_press function detects the key pressed 
# if it is a letter output the character 
# else it is a special character so out put the key
def on_press(key):
    try:
        print('Alphanumeric key pressed: {0} '.format(
            key.char))
        if key.char == ('d'):
            print("YOU PRESSED D")
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