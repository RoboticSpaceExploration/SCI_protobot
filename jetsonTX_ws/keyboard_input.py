#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import keyboard

# keyboard_input.py 
# reads the import from the keyboard 

while True:
    if keyboard.read_key() == "p":
        print("You pressed p")
        break

while True:
    if keyboard.is_pressed("q"):
        print("You pressed q")
        break
        
keyboard.on_press_key("r", lambda _:print("You pressed r"))
