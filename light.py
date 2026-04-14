from machine import Pin #import the rasberry pi pico 2W pin library
from time import sleep, time


#sets the led to the proper pins
led_red1 = Pin(0, Pin.OUT)
led_red2 = Pin(1, Pin.OUT)
led_red3 = Pin(2, Pin.OUT)
led = Pin("LED", Pin.OUT) #The on board led do not change!!

#set the proper pin for the motion sensor, and light sensor
motion_sensor = Pin(22, Pin.IN, Pin.PULL_DOWN)
light_sensor = Pin(21, Pin.IN)

#turns on all the external led lights
def On():
    led_red1.on()
    led_red2.on()
    led_red3.on()

#turns off all the external led lights
def Off():
    led_red1.off()
    led_red2.off()
    led_red3.off()

#Turns on the night light if there is motion detected, otherwise turns it off. 
#Waits for 90 seconds before starting to warm the motion sensor up
def nightLight():
    #start up process, turns on the light for 2 seconds, then turns it off for 90 seconds to warm up the motion sensor
    Off()
    led.on()
    sleep(2)
    led.off()
    sleep(90)
    led.on()
    print("on")
   
    last_motion_detected = 0  #initializes the variable for the motion sensor
    led_on = False
    hold_time = 30 #Time to keep the lights on after not detecting motion
    
    while True:
        current_time = time() # This line resets the timer every time motion is seen
        motion = motion_sensor.value() ==1
        dark = light_sensor.value() == 1
        
        #checks to see if it is both dark and motion is detected
        if motion and dark:
            last_motion_detected = current_time #sets the last motion detected to the current time
            if not led_on: #if led is off turn it on
                On()
                led_on = True
        # if led is on and there has been no motion for the hold time, turn off the light
        elif led_on and (current_time - last_motion_detected > hold_time):
            Off()
            led_on = False
        sleep(0.1) #pause time before each check.

#Test the motion sensor
def motionTest():
    print("warming Up")
    sleep(90)
    print("warm up completed")
    sleep(5)
    while True:
        if motion_sensor.value() == 1: #print on when motion is detected
            print("on")
        elif motion_sensor.value() == 0: #print off when no motion is detected
            print("off")
        else:
            print("Something is fucking wrong")
            print(motion_sensor.value())
            
        

# Test the light sensor
def lightTest():
    print("On")
    sleep(5)
    while True:
        if light_sensor.value() == 1: #print dark when no light is detected
            print ("dark")
        elif light_sensor.value() == 0: #print light when light is detected
            print("light")
        else:
            print("Something is fucking wrong")
            print(light_sensor.value())
        sleep(0.5)