import serial
import time

port = serial.Serial('/dev/serial0')



Data= port.read(32)
PM1 = int.from_bytes(Data[4:6], byte_order='big')
PM2 = int.from_bytes(Data [6:8], byte_order='big')
PM3 = int.from_bytes(Data [8:10], byte_order='big')
