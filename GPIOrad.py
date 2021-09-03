import RPi.GPIO as GPIO
from time import sleep

counts = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

def callBack(channel):
	global counts
	if GPIO.input(17):
		counts += 1
		print (counts)
	
	
		
GPIO.add_event_detect(17, GPIO.BOTH, callback = callBack)

#raw_input("Press Enter when ready/n")

try: sleep (30)

	print("Total counts: ", counts)

finally: 
	GPIO.cleanup()

