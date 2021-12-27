from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation as ani
from psutil import cpu_percent
ax=plt.axes()
y=[]
def animate(i):
    y.append(cpu_percent())
    ax.cla()
    ax.plot(y,label="realtime cpu uses")
    ax.set_xlim(left=max(0,i-50),right=i+50)
    ax.set_ylim(0,100)
    plt.title("Real time cpu")
    plt.legend()
    

an=ani(plt.gcf(),animate,interval=80)
plt.show()
