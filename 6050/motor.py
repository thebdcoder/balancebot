# A program to control the movement of a single motor using the RTK MCB!
# Composed by The Raspberry Pi Guy to accompany his tutorial!
# Let's import the modules we will need!
import time
import RPi.GPIO as GPIO
# Next we setup the pins for use!
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

mhz = 100

GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)

m1 = GPIO.PWM(21, mhz)
m2 = GPIO.PWM(20, mhz)
m3 = GPIO.PWM(16, mhz)
m4 = GPIO.PWM(12, mhz)

<<<<<<< HEAD
def backward(speed):
    if(speed > 100):
        speed = 100
=======
def forward(speed):
>>>>>>> 01c76a9d8aa82cbdef8ddcd37d6c48a8aa3fdf8e
    m1.start(speed) 
    GPIO.output(20, False)
    m3.start(speed)
    GPIO.output(12, False)
    
<<<<<<< HEAD
def forward(speed):
    if(speed > 100):
        speed = 100
=======
def backward(speed):
>>>>>>> 01c76a9d8aa82cbdef8ddcd37d6c48a8aa3fdf8e
    m2.start(speed) 
    GPIO.output(21, False)
    m4.start(speed)
    GPIO.output(16, False)
<<<<<<< HEAD

def stop():
    m1.stop()
    m2.stop()
    m3.stop()
    m4.stop()
=======
>>>>>>> 01c76a9d8aa82cbdef8ddcd37d6c48a8aa3fdf8e
    
def finish():
	print('Finishing up!')
	GPIO.output(21, False)
	GPIO.output(20, False)
	GPIO.output(16, False)
	GPIO.output(12, False)
	quit()
