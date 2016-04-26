#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096
servoZero = (servoMax-servoMin)/2 + servoMin

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

# Keyboard stuff

import Tkinter as tk

afterId = None

def onKeyPress(event):
  global afterId
  if afterId != None:
    isKeyDown = True
    if event.char == "w":
      text.insert('end', 'Forward')
      pwm.setPWM(0, 0, servoMin)
    elif event.char == "s":
      text.insert('end', 'Backward')
      pwm.setPWM(0, 0, servoMax)
    elif event.char == "q":
      text.insert('end', 'Quit')
      pwm.setPWM(0, 0, servoZero)
      root.destroy()

def onKeyRelease(event):
  text.insert('end', 'release')
  pwm.setPWM(0, 0, servoZero)
  global isKeyDown
  isKeyDown = False

# Program
pwm.setPWMFreq(60)                        # Set frequency to 60 Hz


root = tk.Tk()
root.geometry('300x200')
text = tk.Text(root, background='black', foreground='white', font=('Comic Sans MS', 12))
text.pack()
root.bind('<Key>', onKeyPress)
root.bind('<KeyRelease>', onKeyRelease)
text.insert('end', 'Fun with STEM & Pi')
root.mainloop()

print("done")



