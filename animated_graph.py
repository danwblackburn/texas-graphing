import matplotlib.animation as ani
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import numpy as np
from datetime import datetime

title_font = {'family': 'helvetica',
        'color':  'darkred',
        'weight': 'normal',
        'size': 22,
        }

ylabel_font = {'family': 'helvetica',
        'color':  'black',
        'weight': 'normal',
        'size': 16,
        }

xlabel_font = {'family': 'helvetica',
        'color':  'black',
        'weight': 'normal',
        'size': 16,
        }

new_cases = list(np.loadtxt('texas.csv', delimiter=',', dtype = int, skiprows=1,usecols=(4)))
unformatted_dates = list(np.loadtxt('texas.csv', delimiter=',', dtype = str, skiprows=1,usecols=(0)))
date_list = [datetime.strptime(date,"%m/%d/%y").strftime('%d %b') for date in unformatted_dates]

date_axis = [dates.datestr2num(date) for date in date_list]

fig = plt.figure(figsize=(10, 7.5)) 
plt.ylabel('New Cases', fontdict=ylabel_font)
plt.title('Texas Corona Cases', fontdict=title_font)
plt.xticks([])
ax = plt.gca()
line, = ax.plot([], [], color='red', lw=2) 

def animate(i):
    line.set_data(date_axis[:i], new_cases[:i])
    ax.set_xlim(date_axis[0], date_axis[i - 1] + 5)
    ax.set_ylim(0, max(new_cases) + 1000)
    if not i == 0:
        plt.xlabel(date_list[i - 1], fontdict=xlabel_font, labelpad=10)

anim = ani.FuncAnimation(fig, animate, interval=97, frames=len(new_cases) + 1)

anim.save('graph.mp4')

# plt.show()