"""
This matplotlib example uses December 2015 daily high
and low temperatures in London, UK.
"""

import numpy as np
import matplotlib.pyplot as plt

# store data in NumPy arrays for later use.
# (could also read data from a file using 'open' or 'np.loadtxt')

sf_high_temp = np.array([14, 14, 13, 13, 13, 14, 14, 14, 12, 12, 10, 13, 10, 10, 13, 15, 15, 14, 16, 15, 13, 15, 12, 13, 15, 15, 15, 14, 12, 14, 12])
sf_low_temp = np.array([9, 12, 12, 6, 11, 12, 11, 6, 3, 8, 5, 5, 6, 6, 10, 13, 12, 11, 13, 9, 6, 10, 8, 6, 4, 14, 11, 9, 9, 10, 5])

# make days go from 1st to 31st.

day = 1.0 + np.arange(len(sf_high_temp))

# setup the plots.

plt.plot(day, sf_high_temp, 'bo-', label='high')
plt.plot(day, sf_low_temp, 'r^-', label='low')
plt.xlim(1,31)
plt.legend()
plt.xlabel('Day in December 2015')
plt.ylabel('Temperature in C')
plt.title('Daily High/Low Temps in London, UK for December 2015')

# make it easy to read visually.

plt.grid()
plt.fill_between(day, sf_high_temp, color='m', alpha=0.3)
plt.fill_between(day, sf_low_temp, color='w')

# make the plot.

plt.show()
