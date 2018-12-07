import numpy as np
from mpu6050 import mpu6050
import gpio, os, sys

sensor = mpu6050(0x68)

class Quadcopter:
	def __init__(self):
		target = list(0,0,0) # roll, pitch, yaw
		current = list(0,0,0) # roll, pitch, yaw
		throttle = 0 # throttle in [0,100]
		
	
	def updateOrientation(self):
		accel_x = sensor.get_accel_data()['x']
		accel_y = sensor.get_accel_data()['y']
		accel_z = sensor.get_accel_data()['z']
		gyro_x = sensor.get_gyro_data()['x']
		gyro_y = sensor.get_gyro_data()['y']
		gyro_z = sensor.get_gyro_data()['z']
		
		
	def initialise(self):
		""" This function initialises all ESCs. Following steps:
			 - wait 1s
			 - PWM to 2000ms
			 - wait 3s
			 - PWM to 1000ms
			 - wait 1s
			 """
		
	def display(self):
		
