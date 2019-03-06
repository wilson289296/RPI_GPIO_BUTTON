#import gpio library
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(8, GPIO.OUT)
try:
    while True:
        if GPIO.input(7) == GPIO.HIGH:
            print("Closed")
	    GPIO.output(8, GPIO.HIGH)
	else:
	    GPIO.output(8, GPIO.LOW)
        sleep(0.1)

finally:
    GPIO.cleanup()
