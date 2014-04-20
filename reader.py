import serial
import sys
import time
from pySpacebrew.spacebrew import Spacebrew

ser = serial.Serial('/dev/tty.usbserial-AD01SUMG', 9600)
connected = False

# GENERAL IDEA
# Listen for events coming from the arduino and forward them as Spacebrew Events
# bool, string, range
# Take Spacebrew events and forward them to the arduino
# bool, string, range

# setup Spacebrew
brew = Spacebrew("pyRFID", description="Python contolled rfid scanner", server="beaglebone.local", port=9000)
brew.addPublisher("rfidscan", "string")
brew.start()

while True:
	message = ser.readline()
	connected = True
	print(message)
	brew.publish('rfidscan', message)
	time.sleep(0.1)

	ser.close