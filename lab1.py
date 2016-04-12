#!/usr/bin/python

import proto as pro
import matplotlib.pyplot as plt
import numpy as np 
import tools
import math


def eucldist(A, B):

	A_num_rows, A_num_cols = A.shape

	B_num_rows, B_num_cols = B.shape

	dist = np.zeros(shape=(A_num_rows,B_num_rows))

	for i in range(0, A_num_rows):
		for j in range(0, B_num_rows):
			dist[i][j] = np.linalg.norm(A[i] - B[j])

	return dist

#----------------------------------
#		PARAMETERS
#----------------------------------

example = np.load('example.npz')['example'].item()
tidigits = np.load('tidigits.npz')['tidigits']

sampling_rate = 20000
frame_duration = 0.02
frame_shift = 200
frame_len = sampling_rate * frame_duration

graph_rows = 3

#print "tidigits['filename']: ", tidigits['filename']	#printing a dictionary named 'frames'


#----------------------------------
#		CALCULATIONS
#----------------------------------

exsamples = example['samples']
exframes = example['frames']
expre = example['preemph']
exwindowed = example['windowed']
exspec = example['spec']
exmspec = example['mspec']
exmfcc = example['mfcc']
exlmfcc = example['lmfcc']

#realframes = pro.enframe(example['samples'], frame_len, frame_shift)
#realpre = pro.preemp(realframes)
#realwindowed = pro.windowing(realpre)
#realspec = pro.powerSpectrum(realwindowed, 512)
#realmspec = pro.logMelSpectrum(realspec, sampling_rate)
#realmfcc = pro.cepstrum(realmspec, 13)

# KEEP 39 FOR TESTING PURPOSES
d = tidigits[39]	#USE SAMPLE NR 7, IT IS THE SAME AS IN 'EXAMPLE'

tid1 = d['samples']
print "Gender: ", d['gender']
print "Digit: ", d['digit']


test = tools.mfcc(tid1)

# KEEP 16 FOR TESTING PURPOSES
d = tidigits[16]
tid2 = d['samples']
test2 = tools.mfcc(tid2)

print "Gender 2: ", d['gender']
print "Digit 2: ", d['digit']

res = test

for i in range(1, tidigits.size):
	tid = tidigits[i]
	current = tools.mfcc(tid['samples'])
	res = np.append(res, current, axis=0)


#----------------------------------
#	TEST IF FUNCTIONS ARE CORRECT
#----------------------------------

#print "Frames success: ", np.array_equal(realframes,exframes)
#print "Pre-emphesis success: ", np.array_equal(realpre,expre)
#print "Window success: ", np.array_equal(realwindowed,exwindowed)

#----------------------------------
#	PLOTTING EXAMPLE ANSWERS
#----------------------------------

#ax = plt.subplot(graph_rows, 2, 1)
#ax.plot(realspec - exspec)

#ax = plt.subplot(graph_rows, 2, 3)
#ax.imshow(exframes.T, interpolation = 'nearest', aspect = 'auto', origin = 'lower')

#ax = plt.subplot(graph_rows, 2, 5)
#ax.imshow(expre.T, interpolation = 'nearest', aspect = 'auto', origin = 'lower')

#ax = plt.subplot(graph_rows, 2, 7)
#ax.imshow(exwindowed.T, interpolation = 'nearest', aspect = 'auto', origin = 'lower')

#ax = plt.subplot(graph_rows, 2, 9)
#ax.imshow(exspec.T, interpolation = 'nearest', aspect = 'auto', origin = 'lower')

#----------------------------------
#	PLOTTING REAL ANSWERS
#----------------------------------

#ax = plt.subplot(graph_rows, 2, 2)
#ax.plot(d['samples'])

#ax = plt.subplot(graph_rows, 2, 4)
#ax.imshow(realframes.T, interpolation = 'nearest', aspect = 'auto', origin = 'lower')

#ax = plt.subplot(graph_rows, 2, 6)
#ax.imshow(realpre.T, interpolation = 'nearest', aspect = 'auto', origin = 'lower')

#ax = plt.subplot(graph_rows, 2, 8)
#ax.imshow(realwindowed.T, interpolation = 'nearest', aspect = 'auto', origin = 'lower')

#ax = plt.subplot(graph_rows, 2, 10)
#ax.imshow(realspec.T, interpolation = 'nearest', aspect = 'auto', origin = 'lower')
 
#----------------------------------
#	PLOTTING ANSWERS
#----------------------------------

diff = eucldist(test, test2)

#ax = plt.subplot(graph_rows, 1, 1)
#ax.plot(tid1)

#ax = plt.subplot(graph_rows, 1, 2)
#ax.imshow(exlmfcc.T, interpolation = 'nearest', aspect = 'auto', origin = 'lower')

ax = plt.subplot(1, 1, 1)
ax.imshow(diff, interpolation = 'nearest', aspect = 'auto', origin = 'lower')

plt.show()




