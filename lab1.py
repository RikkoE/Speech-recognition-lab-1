#!/usr/bin/python

import proto
import matplotlib.pyplot as plt
import numpy as np 

example = np.load('example.npz')['example'].item()
tidigits = np.load('tidigits.npz')['tidigits']

#print "tidigits['filename']: ", tidigits['filename']	#printing a dictionary named 'frames'

samples = example['samples']

exframes = example['frames']

ax = plt.subplot(2, 1, 1)
ax.plot(samples)

ax = plt.subplot(2, 1, 2)
ax.imshow(exframes.T, interpolation = 'nearest', aspect = 'auto', origin = 'lower')

print exframes

plt.show()
