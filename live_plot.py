from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()

def animate(i):
    data = pd.read_csv('sentiment.csv')
    x = data['Tweets']
    y2 = data['Trump']
    y1 = data['Biden']

    plt.cla()

    plt.plot(x, y1, label='Biden')
    plt.plot(x, y2, label='Trump')

    plt.legend(loc='upper left')
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()