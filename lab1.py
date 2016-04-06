#!/usr/bin/python

import proto as pro
import matplotlib.pyplot as plt
import numpy as np 

example = np.load('example.npz')['example'].item()
tidigits = np.load('tidigits.npz')['tidigits']

sampling_rate = 20000
frame_duration = 0.02
frame_shift = 0.01
frame_len = sampling_rate * frame_duration

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

expre = example['preemph']

ax = plt.subplot(3, 2, 5)
ax.imshow(expre.T, interpolation = 'nearest', aspect = 'auto', origin = 'lower')

testing = pro.enframe(example['samples'], frame_len, frame_shift)

ax = plt.subplot(3, 2, 4)
ax.imshow(testing.T, interpolation = 'nearest', aspect = 'auto', origin = 'lower')



print np.array_equal(testing,exframes)

#print samples.shape

plt.show()
