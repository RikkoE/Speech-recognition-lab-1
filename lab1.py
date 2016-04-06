#!/usr/bin/python

import proto as pro
import matplotlib.pyplot as plt
import numpy as np 

#----------------------------------
#		PARAMETERS
#----------------------------------

example = np.load('example.npz')['example'].item()
tidigits = np.load('tidigits.npz')['tidigits']

sampling_rate = 20000
frame_duration = 0.02
frame_shift = 0.01
frame_len = sampling_rate * frame_duration

#print "tidigits['filename']: ", tidigits['filename']	#printing a dictionary named 'frames'

d = tidigits[7]	#USE SAMPLE NR 7, IT IS THE SAME AS IN 'EXAMPLE'

#----------------------------------
#		CALCULATIONS
#----------------------------------

exsamples = example['samples']
exframes = example['frames']
expre = example['preemph']


realframes = pro.enframe(example['samples'], frame_len, frame_shift)
realpre = pro.preemp(realframes)

#----------------------------------
#	TEST IF FUNCTIONS ARE CORRECT
#----------------------------------

print "Frames success: ", np.array_equal(realframes,exframes)
print "Pre-emphesis success: ", np.array_equal(realpre,expre)

#----------------------------------
#	PLOTTING EXAMPLE ANSWERS
#----------------------------------

ax = plt.subplot(3, 2, 1)
ax.plot(exsamples)

ax = plt.subplot(3, 2, 3)
ax.imshow(exframes.T, interpolation = 'nearest', aspect = 'auto', origin = 'lower')

ax = plt.subplot(3, 2, 5)
ax.imshow(expre.T, interpolation = 'nearest', aspect = 'auto', origin = 'lower')

#----------------------------------
#	PLOTTING REAL ANSWERS
#----------------------------------

ax = plt.subplot(3, 2, 2)
ax.plot(d['samples'])

ax = plt.subplot(3, 2, 4)
ax.imshow(realframes.T, interpolation = 'nearest', aspect = 'auto', origin = 'lower')

ax = plt.subplot(3, 2, 6)
ax.imshow(realpre.T, interpolation = 'nearest', aspect = 'auto', origin = 'lower')


#print samples.shape

plt.show()
