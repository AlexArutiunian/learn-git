import numpy as np
import matplotlib.pyplot as plt

k = 3.3/255

data = np.loadtxt ('data.txt')
data *= k
settings = np.loadtxt ('settings.txt')

charge = settings[0]
finish = settings[1]
dt = settings[0]
dv = settings[1]

time = np.linspace (0, finish, len(data))

x_axes = np.linspace (0, finish, 10)
y_axes = np.linspace(0, data.max(), 10)

plt.ylim([0, data.max() * 1.1])
plt.xlim([0, finish])

plt.grid()



plt.plot(time, data, c='blue', linewidth=1, label = 'V(t)')

    

plt.xlabel(r'Время, $c$',    wrap=True)
plt.ylabel(r'Напряжение, $V$', wrap=True)
plt.scatter (0.0046, data.max(), c="red")

plt.legend()
plt.title('Процесс заряда и разряда конденсатора в RC-цепи', wrap=True)
plt.savefig ('graph.png')
plt.savefig ('graph.svg')