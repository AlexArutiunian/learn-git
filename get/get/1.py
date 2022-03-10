import RPi.GPIO as IO
import time
try:
    leds = [21, 20, 16, 12, 7, 8, 25, 24]
    dac = [10, 9, 11, 5, 6, 13, 19, 26]

    n = int(input())
    if n <= 255:
        bnr = list(map(int, list(bin(n).replace('0b',''))))
        print(bnr)
        number = [1,0,0,0,0,0,0,0]

        num_of_pins = len(leds)
        num_of_dacs = len(dac)

        IO.setmode(IO.BCM)

        IO.setup(leds, IO.OUT)
        IO.setup(dac, IO.OUT)

        IO.output(dac, bnr)
        time.sleep(20)
finally:
    IO.cleanup()
