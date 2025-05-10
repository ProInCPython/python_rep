import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt('data.csv', delimiter=',')

x = [int(i[0]) for i in data]
y = [int(i[1]) for i in data]

plt.title("A function from the data.csv file", color="black",
          fontdict={'family':'serif','color':'black','size':15})
plt.plot(x,y, color="#bfa636", label="function f")
plt.xlabel("X axis",
           fontdict={'family':'verdana','color':'#1114cf','size':12})
plt.ylabel("Y axis",
           fontdict={'family':'verdana','color':'#cf1127','size':12})


plt.ylim(bottom=min(y))
plt.xlim(left=x[0], right=x[-1])
plt.legend()
plt.show()