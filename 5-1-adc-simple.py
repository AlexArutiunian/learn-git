import RPi.GPIO as GPIO
import time

dac = [26,19, 13, 6, 5, 11, 9, 10]

maxVoltage = 3.3
troyka = 17
comp =  4

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(i):
    return [int(elem) for elem in bin(i)[2:].zfill(8)]

def bin2dac(i):
    signal = decimal2binary(i)
    GPIO.output(dac, signal)    
    return signal

def adc():
    for i in range(256):
        bin2dac(i)
        time.sleep(0.01)
        compVAL = GPIO.input(comp)

        if compVAL == 0:
            return i

try:
    while True:
        const = adc()
        print("цифровое значение =")
        print(const)
        print("напряжение")
        valToPr = const/ 2**8 * 3.3
        print(valToPr)

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)