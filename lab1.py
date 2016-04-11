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

graph_rows = 5

#print "tidigits['filename']: ", tidigits['filename']	#printing a dictionary named 'frames'

d = tidigits[7]	#USE SAMPLE NR 7, IT IS THE SAME AS IN 'EXAMPLE'

#----------------------------------
#		CALCULATIONS
#----------------------------------

exsamples = example['samples']
exframes = example['frames']
expre = example['preemph']
exwindowed = example['windowed']
exspec = example['spec']

realframes = pro.enframe(example['samples'], frame_len, frame_shift)
realpre = pro.preemp(realframes)
realwindowed = pro.windowing(realpre)
realspec = pro.powerSpectrum(realwindowed, 512)

#----------------------------------
#	TEST IF FUNCTIONS ARE CORRECT
#----------------------------------

print "Frames success: ", np.array_equal(realframes,exframes)
print "Pre-emphesis success: ", np.array_equal(realpre,expre)
print "Window success: ", np.array_equal(realwindowed,exwindowed)

#----------------------------------
#	PLOTTING EXAMPLE ANSWERS
#----------------------------------

ax = plt.subplot(graph_rows, 2, 1)
ax.plot(realspec - exspec)

ax = plt.subplot(graph_rows, 2, 3)
ax.imshow(exframes.T, interpolation = 'nearest', aspect = 'auto', origin = 'lower')

ax = plt.subplot(graph_rows, 2, 5)
ax.imshow(expre.T, interpolation = 'nearest', aspect = 'auto', origin = 'lower')

ax = plt.subplot(graph_rows, 2, 7)
ax.imshow(exwindowed.T, interpolation = 'nearest', aspect = 'auto', origin = 'lower')

ax = plt.subplot(graph_rows, 2, 9)
ax.imshow(exspec.T, interpolation = 'nearest', aspect = 'auto', origin = 'lower')

#----------------------------------
#	PLOTTING REAL ANSWERS
#----------------------------------

ax = plt.subplot(graph_rows, 2, 2)
ax.plot(d['samples'])

ax = plt.subplot(graph_rows, 2, 4)
ax.imshow(realframes.T, interpolation = 'nearest', aspect = 'auto', origin = 'lower')

ax = plt.subplot(graph_rows, 2, 6)
ax.imshow(realpre.T, interpolation = 'nearest', aspect = 'auto', origin = 'lower')

ax = plt.subplot(graph_rows, 2, 8)
ax.imshow(realwindowed.T, interpolation = 'nearest', aspect = 'auto', origin = 'lower')

ax = plt.subplot(graph_rows, 2, 10)
ax.imshow(realspec.T, interpolation = 'nearest', aspect = 'auto', origin = 'lower')

print realspec

plt.show()
