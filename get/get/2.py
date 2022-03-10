import RPi.GPIO as IO
leds = [21, 20, 16, 12, 7, 8, 25, 24]
aux = [22, 23, 27, 18, 15, 14, 3, 2]

IO.setmode(IO.BCM)
IO.setup(leds, IO.OUT)
IO.setup(aux, IO.IN, pull_up_down=IO.PUD_UP)
while 1:
    for i in range(8):
        IO.output(leds[i], IO.input(aux[i]))