#!/usr/bin/python

import proto as pro
import matplotlib.pyplot as plt
import numpy as np 

example = np.load('example.npz')['example'].item()
tidigits = np.load('tidigits.npz')['tidigits']

#print "tidigits['filename']: ", tidigits['filename']	#printing a dictionary named 'frames'

samples = example['samples']

exframes = example['frames']

ax = plt.subplot(3, 2, 1)
ax.plot(samples)

ax = plt.subplot(3, 2, 3)
ax.imshow(exframes.T, interpolation = 'nearest', aspect = 'auto', origin = 'lower')

d = tidigits[7]	#USE SAMPLE NR 7, IT IS THE SAME AS IN 'EXAMPLE'

ax = plt.subplot(3, 2, 2)
ax.plot(d['samples'])

#ax = plt.subplot(2, 2, 4)
#test = pro.enframe(samples, 20, 10)
#ax.imshow(test.T, interpolation = 'nearest', aspect = 'auto', origin = 'lower')

expre = example['preemph']

ax = plt.subplot(3, 2, 5)
ax.imshow(expre.T, interpolation = 'nearest', aspect = 'auto', origin = 'lower')

print expre

plt.show()
