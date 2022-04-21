import RPi.GPIO as IO
import time as tm
import matplotlib.pyplot as plt

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]
comp = 4
troyka = 17
dac = [10, 9, 11, 5, 6, 13, 19, 26]
leds = [21, 20, 16, 12, 7, 8, 25, 24]

dac.reverse()

IO.setmode(IO.BCM)
IO.setup(troyka, IO.OUT)
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
        if comp_out == 0:
            dac_val[i] = 0
    weight = 1 
    sum = 0
    for i in range(8):
        sum += weight * dac_val[7 - i]
        weight *= 2
    IO.output(dac, 0)
    return sum



try:
    vals_of_capasitor = []
    IO.output(troyka, IO.HIGH)
    time_of_start = tm.time()
    while(adc_new() <= 256 * 0.97):
        val = adc_new()
        IO.output(leds, decimal2binary(val))
        vals_of_capasitor.append(val)
        tm.sleep(0.001)
        print(val)
    IO.output(troyka, IO.LOW)
    while(adc_new() >= 256 * 0.02):
        val = adc_new()
        IO.output(leds, decimal2binary(val))
        vals_of_capasitor.append(val)
        tm.sleep(0.001)
        print(val)
    time_of_end = tm.time()
    plt.plot(vals_of_capasitor)
    with  open("data.txt", 'w')  as  data:
        for i in range(len(vals_of_capasitor)):
             data.write(str(vals_of_capasitor[i]) + '\n')
    with  open("settings.txt", 'w')  as  settings:
        settings.write(str(time_of_end - time_of_start) +'\n')
        settings.write(str((time_of_end - time_of_start) / len(vals_of_capasitor))+'\n')
        settings.write(str(len(vals_of_capasitor) / (time_of_end - time_of_start))+'\n')
        settings.write(str(3.3*0.02)+"-"+str(3.3*0.97)+'\n')
        settings.write(str(3.3/256)+'\n')
    plt.show()
    print("Время эксперимента = ", (time_of_end - time_of_start) / len(vals_of_capasitor), '\n')
    print("Время периода = ", time_of_end - time_of_start, '\n')
    print("Средняя частота дискретизации = ",  len(vals_of_capasitor) / (time_of_end - time_of_start), '\n')
    print((3.3/256), '\n')
finally:
    IO.output(dac, 0)
    IO.cleanup()





        




