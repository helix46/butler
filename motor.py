# This file runs at startup because it is in rc.local
# To edit enter in a terminal
# sudo nano /etc/rc.local
# https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/

# find and kill process running python
# ps aux | grep python
# should see something like
# root XXX  3.8  0.6  70664 26632 ?        Sl   09:23   0:02 python /home/pi/motor/motor.py
# sudo kill XXX


import RPi.GPIO as GPIO
import time
from pygame import mixer
from random import *
import random

# board pin 2  DC +5V motion detector 1 orange wire
# board pin 4  DC +5V motion detector 2 white wire
# board pin 6  GND relay GND
# board pin 16 GPIO 23 motion detector 1 yellow wire
# board pin 18 GPIO 24 relay IN1 open eyes
# board pin 20 gnd motion detector 2 white wire
# board pin 22 GPIO 25 motion detector 2 black wire

# board pin 1  DC +3.3V relay UCC
# board pin 9  gnd motion detector 1 green wire
# board pin 15 GPIO 22 relay IN2 close eyes
# board pin 11 GPIO 17 relay IN3 open mouth
# board pin 13 GPIO 27 relay IN4 close mouth

class comment:
    def __init__(self, fileName, pause, length):
        self.fileName = fileName
        self.pause = pause
        self.length = length

listOfComments = []
listOfComments.append(comment("Attire", 2, 2) )
listOfComments.append(comment("Footman", 2, 3))
listOfComments.append(comment("Fork", 1, 3))
listOfComments.append(comment("Freshen", 1, 3))
listOfComments.append(comment("Gaunt", 1, 3))
listOfComments.append(comment("Hors-doeuvre", 1, 3))
listOfComments.append(comment("Inappropriate", 1, 2))
listOfComments.append(comment("Lint", 1, 3))
listOfComments.append(comment("Restorative", 1, 3))
listOfComments.append(comment("Retrosexual", 1, 5))
listOfComments.append(comment("Service", 1, 3))
listOfComments.append(comment("Shaken", 1, 3))
listOfComments.append(comment("Tempations", 1, 4))
listOfComments.append(comment("Tipple", 1, 3))
listOfComments.append(comment("Toupee", 1, 4))
listOfComments.append(comment("Very-good-sir", 1, 2))


def setGpio():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT) # GPIO Assign mode
    GPIO.setup(27, GPIO.OUT) # GPIO Assign mode
    GPIO.setup(22, GPIO.OUT) # GPIO Assign mode
    GPIO.setup(24, GPIO.OUT) # GPIO Assign mode
    
    GPIO.setup(23, GPIO.IN) #motion detector 1
    GPIO.setup(25, GPIO.IN) #motion detector 2

def log(s):
    print(s)

def sendPulse(gpio_pin):
    GPIO.output(gpio_pin, GPIO.LOW)
    time.sleep(.2)
    GPIO.output(gpio_pin, GPIO.HIGH)

def openMouth():
    #relay IN3
    sendPulse(17)
    log("openMouth")

def closeMouth():
    #relay IN4
    sendPulse(27)
    log("closeMouth")

def openEyes():
    #relay IN1
    sendPulse(24)
    log("openEyes")

def closeEyes():
    #relay IN2
    sendPulse(22)
    log("closeEyes")

def blink():
    closeEyes()
    time.sleep(.2)
    openEyes()

def wakeUp():
    openEyes()
    time.sleep(2)
    blink()
    time.sleep(2)
    closeEyes()

def playRemark(comment):
    # open eyes and blink
    openEyes()
    time.sleep(1)
    blink()
    
    # play remark
    mixer.music.load("/home/pi/motor/audio-files/" + comment.fileName + ".mp3")
    mixer.music.play()
    
    # pause
    time.sleep(comment.pause)
    # open mouth randomly
    for x in range(comment.length):
        openMouth()
        time.sleep(1)
        closeMouth()
    closeEyes()
 
def mainLoop(): 
    time.sleep(5) #to stabilize sensor
    while True:
        if GPIO.input(23) or GPIO.input(25):
            index = random.randint(0,15)
            playRemark(listOfComments[index])
            time.sleep(5) #to avoid multiple detection
            time.sleep(60) #to prevent too many comments
        time.sleep(0.1) #loop delay, should be less than detection delay


# main
setGpio()
mixer.init()
# openMouth()
# closeMouth()
# openEyes()
# closeEyes()

wakeUp()
mainLoop()

# for x in range(16):
#     log(x)
#     playRemark(listOfComments[x])
#     time.sleep(2)


    
    

    