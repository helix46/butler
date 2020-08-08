# This file runs at startup because it is in rc.local
# To edit enter in a terminal
# sudo nano /etc/rc.local
# https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/

# find and kill process running python
# ps aux | grep python
# sudo kill XXX


import RPi.GPIO as GPIO
import time
from pygame import mixer
from random import *

# board pin 2  DC +5V motion detector orange wire
# board pin 6  GND relay GND
# board pin 16 GPIO 23 motion detector yellow wire
# board pin 18 GPIO 24 relay IN1

# board pin 1  DC +3.3V relay UCC
# board pin 9  gnd motion detector green wire

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT) # GPIO Assign mode
GPIO.setup(24, GPIO.OUT) # GPIO Assign mode
GPIO.setup(23, GPIO.IN) #PIR

GPIO.output(24, GPIO.HIGH)
GPIO.output(22, GPIO.HIGH)
    
# open mouth
# yawn
# pause 2 seconds
# close mouth
# open eyes
# pause 1 second
# fart
# pause 1 second
# close eyes
# pause 5 seconds

def log(s):
    print(s)

def openMouth():
    GPIO.output(24, GPIO.LOW)
    log("openMouth")

def closeMouth():
    GPIO.output(24, GPIO.HIGH)
    log("closeMouth")

def openEyes():
    GPIO.output(22, GPIO.LOW)
    log("openEyes")

def closeEyes():
    GPIO.output(22, GPIO.HIGH)
    log("closeEyes")

def yawn():
    mixer.music.load("/home/pi/sounds/yawn.mp3")
    mixer.music.play()
    log("yawn")

def fart():
    mixer.music.load("/home/pi/sounds/fart.mp3")
    mixer.music.play()
    log("fart")

def randomDelay():
    time.sleep(random())

def playRemark():
    log("start play Remark")
    # open eyes and blink
    openEyes()
    time.sleep(1)
    closeEyes()
    time.sleep(.2)
    openEyes()
    # pause 2 seconds
    time.sleep(2)
    # open mouth randomly
    for x in range(6):
        openMouth()
        randomDelay()
        closeMouth()
        randomDelay()
    # play random lewd remark
    fart()
    closeMouth()
    closeEyes()
    log("end play Remark")
    

mixer.init()
openMouth()
yawn()
time.sleep(6)
closeMouth()
time.sleep(2)
openEyes()
fart()
time.sleep(2)
closeEyes()

time.sleep(5) # to stabilize sensor
while True:
    if GPIO.input(23):
        playRemark()
        time.sleep(5) #to avoid multiple detection
    time.sleep(0.1) #loop delay, should be less than detection delay
            
    
    

    