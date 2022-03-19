#import Jetson.GPIO as GPIO
import pin_setting
 
def runMotor(dir,pwm1,dir1,pwm2,dir2):  ## dir: 0(forward), 1(right), 2(left), 3(backward)
    if dir == "f": ## Go straight
        print("Moving motors forward")
        #d1 = GPIO.HIGH
        #d2 = GPIO.HIGH
    elif dir == "b": ## Backward 
        print("Moving motors backward")
        #d1 = GPIO.LOW
        #d2 = GPIO.LOW
    #GPIO.output(dir1, d1)
    #GPIO.output(dir2, d2)
    #GPIO.output(pwm1, GPIO.HIGH)
    #GPIO.output(pwm2, GPIO.HIGH)

