import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setmode (GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH) 
GPIO.setup(comp, GPIO.IN)

def dec2bin(x):
    return [int(i) for i in bin(x)[2:].zfill(8)]

def adc():
    for i in range (256):
        GPIO.output(dac, dec2bin(i))
        time.sleep(0.001)
        comp_out = GPIO.input(comp)

        if not comp_out: 
            return i
        time.sleep(0.001)
    return 255

try:
    while 1:
        val = adc()
        voltage = val * 3.3 / 256
        print('Цифровое значение = {} Аналоговое значение = {:.2f}'.format(val, voltage))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()        