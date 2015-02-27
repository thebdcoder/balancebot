#!/usr/bin/python

import smbus
import math
import time
from MPU6050 import MPU6050
from PID import PID
import motor as MOTOR

gyro_scale = 131.0
accel_scale = 16384.0
RAD_TO_DEG = 57.29578
M_PI = 3.14159265358979323846

address = 0x68  # This is the address value read via the i2cdetect command
bus = smbus.SMBus(1)  # or bus = smbus.SMBus(1) for Revision 2 boards

now = time.time()

K = 0.98
K1 = 1 - K

time_diff = 0.01

sensor = MPU6050(bus, address, "MPU6050")
sensor.read_raw_data()

rate_gyroX = 0.0
rate_gyroY = 0.0
rate_gyroZ = 0.0

gyroAngleX = 0.0 
gyroAngleY = 0.0 
gyroAngleZ = 0.0 

raw_accX = 0.0
raw_accY = 0.0
raw_accZ = 0.0

rate_accX = 0.0
rate_accY = 0.0
rate_accZ = 0.0

accAngX = 0.0

CFangleX = 0.0
CFangleX1 = 0.0

K = 0.98

FIX = -12.89

#print "{0:.4f} {1:.2f} {2:.2f} {3:.2f} {4:.2f} {5:.2f} {6:.2f}".format( time.time() - now, (last_x), gyro_total_x, (last_x), (last_y), gyro_total_y, (last_y))

def dist(a, b):
    return math.sqrt((a * a) + (b * b))


def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

p=PID(1.0,-0.04,0.0)
p.setPoint(0.0)

for i in range(0, int(300.0 / time_diff)):
    time.sleep(time_diff - 0.005) 
    
    sensor.read_raw_data()
    
    # Gyroscope value Degree Per Second / Scalled Data
    rate_gyroX = sensor.read_scaled_gyro_x()
    rate_gyroY = sensor.read_scaled_gyro_y()
    rate_gyroZ = sensor.read_scaled_gyro_z()
	
	# The angle of the Gyroscope
    gyroAngleX += rate_gyroX * time_diff 
    gyroAngleY += rate_gyroY * time_diff 
    gyroAngleZ += rate_gyroZ * time_diff 
	
	# Accelorometer Value
    raw_accX = sensor.read_raw_accel_x()
    raw_accY = sensor.read_raw_accel_y()
    raw_accZ = sensor.read_raw_accel_z()
    
    rate_accX = sensor.read_scaled_accel_x()
    rate_accY = sensor.read_scaled_accel_y()
    rate_accZ = sensor.read_scaled_accel_z()

    accAngX = ( math.atan2(rate_accX, rate_accY) + M_PI ) * RAD_TO_DEG
    
    accAngX1 = get_x_rotation(rate_accX, rate_accY, rate_accX)
    
    CFangleX = K * ( CFangleX + rate_gyroX * time_diff) + (1 - K) * accAngX
    
    CFangleX1 = ( K * ( CFangleX1 + rate_gyroX * time_diff) + (1 - K) * accAngX1 )
	
    pid = p.update(CFangleX1)
    
    if(-10 < pid < 10):
        MOTOR.forward(0)
    else:
        if(pid > 10):
            MOTOR.backward(pid)
        else:
            MOTOR.forward(pid*-1)
    
    print "{0:.2f} {1:.2f} {2:.2f} {3:.2f} | {4:.2f} {5:.2f} | {6:.2f}".format( gyroAngleX, gyroAngleY , accAngX, CFangleX, accAngX1, CFangleX1, pid)
