import board
import time
from adafruit_bme280 import basic as adafruit_bme280
import csv
import serial
# for input arguments
import sys


#with open('sensor.csv', 'w') as csvfile:

# Create sensor object, using the board's default I2C bus.
i2c = board.I2C()   # uses board.SCL and board.SDA
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1013.25

start_time = time.time()

sleep_time = int(sys.argv[2])

current_time = start_time

dataFile = open(sys.argv[4], 'w')
dataWriter = csv.writer(dataFile)


header = ['time', 'temperature', 'pressure', 'humidity', 'PM1', 'PM2', 'PM3']
dataWriter.writerow(header)

port = serial.Serial('/dev/serial0')


delay_time = int(sys.argv[3])
run_time = int(sys.argv[1])+int(sys.argv[3])
stop_time = start_time+run_time

time.sleep(delay_time)

while current_time < stop_time:
    
    current_time = time.time()
    Data= port.read(32)
    PM1 = int.from_bytes(Data[4:6], byteorder='big')
    PM2 = int.from_bytes(Data [6:8], byteorder='big')
    PM3 = int.from_bytes(Data [8:10], byteorder='big')
    data_list = [current_time, bme280.temperature, bme280.pressure, bme280.relative_humidity, PM1, PM2, PM3]
    dataWriter.writerow(data_list)
    print("\nTemperature: %0.1f C" % bme280.temperature)
    print("Humidity: %0.1f %%" % bme280.relative_humidity)
    print("Pressure: %0.1f hPa" % bme280.pressure)
    print("Altitude = %0.2f meters" % bme280.altitude)
    print ("Data: ", PM1, PM2, PM3)
    time.sleep(sleep_time)
    




	
    

