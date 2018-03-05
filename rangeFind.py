#!/usr/bin/python3
# Filename: rangeFind.py

# sample script to read range values from Maxbotix ultrasonic rangefinder

from time import sleep
import maxSonarTTY
import time

# serialPort = "/dev/tty.usbserial-MB1UTYXZ"
serialPort = "COM5"
detectionDistance = 400
# stop_by_period = time.time() + 5

while True:
    mm = maxSonarTTY.measure(serialPort)
    print("distance:", mm)
    if (mm < detectionDistance):
    	stop_by_period = time.sleep(3) #stop 3 seconds
    	print("True")
    sleepTime = time.sleep(0.3)