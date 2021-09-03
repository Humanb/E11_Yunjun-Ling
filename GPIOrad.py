import RPi.GPIO as GPIO
import time
from time import sleep
import csv
import sys
import serial

counts = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)



current_time = time.time()
sleep_time = int(sys.argv[2])

port = serial.Serial('/dev/serial0')

delay_time = int(sys.argv[3])
run_time = int(sys.argv[1])+int(sys.argv[3])
stop_time = current_time+run_time

time.sleep(delay_time)

dataFile = open(sys.argv[4], 'w')
dataWriter = csv.writer(dataFile)
header = ['time','counts']
dataWriter.writerow(header)


def callBack(channel):
	global counts
	if GPIO.input(17):
		counts += 1
		print (counts)
		
GPIO.add_event_detect(17, GPIO.BOTH, callback = callBack)

while current_time < stop_time:
	
	current_time = time.time()
	dataList = [current_time, counts]
	dataWriter.writerow(dataList)
	print("radiation counts:", counts)
	counts = 0
	time.sleep(sleep_time)
	
	

#raw_input("Press Enter when ready/n")

#try: sleep (30)

#print("Total counts: ", counts)

 
GPIO.cleanup()

dataFile.close()

