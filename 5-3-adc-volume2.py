import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [24, 25, 8, 7, 12, 16, 20, 21]
comp = 4
troyka = 17

GPIO.setmode (GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)

def dec2bin(x):
    return [int(i) for i in bin(x)[2:].zfill(8)]
    
def adc_new():
    dac_val = [0] * 8
    for i in range(0,8):
        dac_val[i] = 1
        GPIO.output(dac, dac_val)
        time.sleep(0.001)
        comp_out = GPIO.input(comp)
        time.sleep(0.001)
        if comp_out == 0:
            dac_val[i] = 0
    weight = 1
    sum = 0
    for i in range(8):
        sum += weight * dac_val[7-i]
        weight *= 2

    GPIO.output(dac, 0)
    time.sleep(0.001)
    print(dac_val)
    return sum

try:
    while(1):
        x = adc_new()
       
        volt = x * 3.3 / 256
        GPIO.output(dac, dec2bin(x))
        GPIO.output(leds, 0)
        print("Entered value = {:^3}, output voltage = {:.2f}".format(x, volt))
        for i in range (round(8*(x/256))):
            GPIO.output(leds[i], 1)
        print ('Цифровое значение: {}, Аналоговое значение: {:.2f}'.format(x, volt))

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    GPIO.output(leds, 0)
    GPIO.cleanup(leds)