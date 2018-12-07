import numpy as np
from mpu6050 import mpu6050
import gpio, os, sys, time
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error
import pigpio #importing GPIO library

ESC1=20  #Connect the ESC in this GPIO pin
ESC2=15  #Connect the ESC in this GPIO pin
ESC3=9  #Connect the ESC in this GPIO pin
ESC4=19  #Connect the ESC in this GPIO pin

pi = pigpio.pi();
pi.set_servo_pulsewidth(ESC1, 0)
pi.set_servo_pulsewidth(ESC2, 0)
pi.set_servo_pulsewidth(ESC3, 0)
pi.set_servo_pulsewidth(ESC4, 0)
pi.set_PWM_frequency(ESC1, 50)
pi.set_PWM_frequency(ESC2, 50)
pi.set_PWM_frequency(ESC3, 50)
pi.set_PWM_frequency(ESC4, 50)

max_value = 2000 #change this if your ESC's max value is different or leave it be
min_value = 1000  #change this if your ESC's min value is different or leave it be

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
