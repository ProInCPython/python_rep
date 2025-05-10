import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def sin_func(frame, line, x):
  line.set_ydata(np.sin(x+frame))
  return [line]

x = np.arange(-2*np.pi, 2*np.pi, 0.1)
y = np.sin(x)

fig, ax = plt.subplots()

line, = ax.plot(x,y)

frames = np.arange(0, 4*np.pi, 0.1)

interval = 10
blit = False
repeat = False

animation = FuncAnimation(fig, func=sin_func, frames=frames, fargs=(line, x), interval=interval, blit=blit, repeat=repeat)
plt.show()
