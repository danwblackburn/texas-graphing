import matplotlib.animation as ani
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import numpy as np
import csv



new_cases = list(np.loadtxt('texas.csv', delimiter=',', dtype = int, skiprows=1,usecols=(4)))
date_list = list(np.loadtxt('texas.csv', delimiter=',', dtype = str, skiprows=1,usecols=(0)))

date_axis = [dates.datestr2num(date) for date in date_list]

fig = plt.figure() 
plt.xticks(rotation=45, ha="right", rotation_mode="anchor")
plt.subplots_adjust(bottom = 0.2, top = 0.9)
plt.ylabel('No of Deaths')
plt.xlabel('Dates')
ax = plt.gca()
ax.xaxis.set_major_formatter(dates.DateFormatter('%Y-%m-%d'))
line, = ax.plot([], [], lw=2) 

def animate(i):
    if(i < 50):
        line.set_data(date_axis[:i], new_cases[:i])
    else:
        line.set_data(date_axis[i - 50:i], new_cases[i - 50:i])
    ax.relim()
    ax.autoscale_view()
    ax.set_ylim(0, max(new_cases))

anim = ani.FuncAnimation(fig, animate, interval=40, frames=len(new_cases) + 1)

# anim.save('graph.mp4')

plt.show()