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

servoLeft = 0
servoRight = 1

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

# Simple Servo Calls
def ServoClockwise(channel):
	pwm.setPWM(channel, 0, servoMin)

def ServoCounterClockwise(channel):
	pwm.setPWM(channel, 0, servoMax)

def ServoStop(channel):
	pwm.setPWM(channel, 0, servoZero)

# Keyboard stuff

import Tkinter as tk

class MyFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # method call counter
        self.pack()
        self.afterId = None
        root.bind('<KeyPress>', self.key_press)
        root.bind('<KeyRelease>', self.key_release)
        
    def key_press(self, event):
        if self.afterId != None:
            self.after_cancel( self.afterId )
            self.afterId = None
        else:
            print 'key pressed %s' % event.char
	    if event.char == "w":
	      text.insert('end', 'Forward')
	      ServoClockwise(servoLeft)
              ServoClockwise(servoRight)
	    elif event.char == "s":
	      text.insert('end', 'Backward')
	      ServoCounterClockwise(servoLeft)
              ServoCounterClockwise(servoRight)
	    elif event.char == "k":
	      text.insert('end', 'Quit')
	      pwm.setPWM(0, 0, servoZero)
	      root.destroy()
            elif event.char == "a":
	      text.insert('end', 'Left')
	      ServoCounterClockwise(servoLeft)
              ServoClockwise(servoRight)
            elif event.char == "d":
	      text.insert('end', 'Left')
	      ServoClockwise(servoLeft)
              ServoCounterClockwise(servoRight)
         




    def key_release(self, event):
        self.afterId = self.after_idle( self.process_release, event )

    def process_release(self, event):
        ServoStop(servoLeft)
	ServoStop(servoRight)
	print 'key release %s' % event.char
        self.afterId = None



# Program
pwm.setPWMFreq(60)                        # Set frequency to 60 Hz


root = tk.Tk()
root.geometry('300x200')
text = tk.Text(root, background='black', foreground='white', font=('Comic Sans MS', 12))
text.pack()
text.insert('end', 'Fun with STEM & Pi')
app1 = MyFrame(root)
root.mainloop()

print("done")



