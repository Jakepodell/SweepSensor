import serial
import Tkinter
import time

usbport = 'COM4'
distString =""
dist =0;

# Set up serial baud rate
ser = serial.Serial(usbport, 9600, timeout=1)

while True:
    distString =""
    for line in ser.readline():
        if line.isdigit():
            distString+=line
    if distString.isdigit():
        dist = float(distString)
    print dist
