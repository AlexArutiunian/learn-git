import RPi.GPIO as IO
import time as tm

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]
comp = 4
troyka = 17
dac = [10, 9, 11, 5, 6, 13, 19, 26]
leds = [21, 20, 16, 12, 7, 8, 25, 24]

dac.reverse()

IO.setmode(IO.BCM)
IO.setup(troyka, IO.OUT, initial = IO.HIGH)
IO.setup(dac, IO.OUT)
IO.setup(leds, IO.OUT)
IO.setup(comp, IO.IN)

def adc():
    for i in range(256):
        IO.output(dac, decimal2binary(i))
        tm.sleep(0.001)
        comp_out = IO.input(comp)
        tm.sleep(0.001)
        if comp_out == 0:
            IO.output(dac, 0)
            tm.sleep(0.01)
            return i

    IO.output(dac, 0)
    tm.sleep(0.01)
    return 256

def adc_new():
    dac_val = [0] * 8 
    for i in range(0, 8):
        dac_val[i] = 1
        IO.output(dac, dac_val)
        tm.sleep(0.001)
        comp_out = IO.input(comp)
        tm.sleep(0.001)
        if comp_out == 0:
            dac_val[i] = 0
    weight = 1 
    sum = 0
    for i in range(8):
        sum += weight * dac_val[7 - i]
        weight *= 2
    IO.output(dac, 0)
    tm.sleep(0.001)
    print(dac_val)
    return sum



try:
    while(1):
        val = adc_new()
        leds_val = [0] * 8
        for i in range(8):
            if(i * 256 / 8 < val):
                leds_val[i] =   1
        IO.output(leds, leds_val)
        print(str(val) +" " + str(float(val) /256 * 3.3))
        tm.sleep(0.001)
finally:
    IO.output(dac, 0)
    IO.cleanup()





        




