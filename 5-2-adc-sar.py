import RPi.GPIO as GPIO
import time

dac = [26,19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]

maxVoltage = 3.3
troyka = 17
comp =  4

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(leds, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(i):
    return [int(elem) for elem in bin(i)[2:].zfill(8)]

def bin2dac(i):
    signal = decimal2binary(i)
    GPIO.output(dac, signal)    
    #return signal

def adc(i, value):
    if i == -1:
        return value
    bin2dac(value + 2**i)
    time.sleep(0.01)
    compVAL = GPIO.input(comp)
    if compVAL == 0:
        return adc(i - 1, value)
    else:
        return adc(i - 1, value + 2**i)

try:
    while True:
        const = adc(7, 0)
        print("цифровое значение =")
        print(const)
        print("напряжение")
        valToPr = const/ 2**8 * 3.3
        print(valToPr)
        valToPr = valToPr/3.3 * 8 +0.4
        for i in range(8):
            if valToPr >= 1:
                GPIO.output(leds[7 - i], 1)
            else:
                GPIO.output(leds[7 - i], 0)
            valToPr = valToPr - 1

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    GPIO.cleanup(leds)