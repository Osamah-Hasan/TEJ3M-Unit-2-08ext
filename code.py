# Created by: Osamah
# Created on: APR 2025
# servo change angle with potentiometer

import time
import board
import analogio
import pwmio
from adafruit_motor import servo

# Set up the analog input for the potentiometer
potentiometer = analogio.AnalogIn(board.A0)

# Set up the PWM output for the servo
pwm = pwmio.PWMOut(board.GP15, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)

# Constants
wait_time = 0.015 # 15 milliseconds
full_number = 180.0
pot_max = 65535.0 # 16-bit ADC in CircuitPython

while True:
    pot_value = potentiometer.value
    angle = (pot_value / pot_max) * full_number
    my_servo.angle = angle
    time.sleep(wait_time)