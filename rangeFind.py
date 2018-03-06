#!/usr/bin/python3
# Filename: rangeFind.py

# sample script to read range values from Maxbotix ultrasonic rangefinder

from time import sleep
import maxSonarTTY
import time

# serialPort = "/dev/tty.usbserial-MB1UTYXZ"
serialPort = "COM5"
detectionDistance = 400
sleepTime = 1
stop_by_period = time.time() + 5


while True:
	mm = maxSonarTTY.measure(serialPort)
	print("distance:", mm)
	if mm < detectionDistance:
		if time.time() - stop_by_period > 5:
			stop_by_period = time.time()
			print("True")
	sleep(sleepTime)

# while True:
#     mm = maxSonarTTY.measure(serialPort)
#     print("distance:", mm)
#     if (mm < detectionDistance):
#     	start = time.time()
#     	stop_by_period = 10
#     	if (start > stop_by_period):
#     		print("Detected")
    # time.sleep(2)


# #!/usr/bin/python3
# # Filename: rangeFind.py

# # sample script to read range values from Maxbotix ultrasonic rangefinder

# from time import sleep
# import maxSonarTTY

# serialPort = "COM5"
# maxRange = 400  # change for 5m vs 10m sensor
# sleepTime = 1
# minMM = 9999
# maxMM = 0

# while True:
#     mm = maxSonarTTY.measure(serialPort)
#     if mm >= maxRange:
#         print("no target")
#         sleep(sleepTime)
#         continue
#     if mm < minMM:
#         minMM = mm
#     if mm > maxMM:
#         maxMM = mm

#     print("distance:", mm, "  min:", minMM, "max:", maxMM)
#     sleep(sleepTime)