#!/usr/bin/env python3

import numpy as np
from scipy.io import wavfile

samp_rate = 48000	# audio file sample rate
tone = 500 	# frequency of the CW tone in Hz
vol = 0.3 	# volume = max amplitude of the audio tone

# these definitions have been copied from:
# 	A Standard for Morse Timing Using the Farnsworth Technique
#	Jon Bloom, KE3Z
#	ARRL Laboratory
wpm = 35
u = 1.2/wpm

# define the numbers from 0 to 9 in terms of dits and dahs
numbers = [[1,1,1,1,1],[0,1,1,1,1],[0,0,1,1,1],[0,0,0,1,1],[0,0,0,0,1],[0,0,0,0,0],
	[1,0,0,0,0],[1,1,0,0,0],[1,1,1,0,0],[1,1,1,1,0]]

# generate dit and dah sounds
dit = vol*np.sin(2*np.pi*tone/samp_rate*np.arange(u*samp_rate))
dah = vol*np.sin(2*np.pi*tone/samp_rate*np.arange(3*u*samp_rate))
space = np.zeros(int(u*samp_rate))

# generate windowing functions for dits and dahs to mitigate 'key-clicking'
cos_rise = 0.5 - 0.5*np.cos(np.linspace(0,np.pi,int(0.125*u*samp_rate)))
cos_fall = 0.5 - 0.5*np.cos(np.linspace(np.pi,2*np.pi,int(0.125*u*samp_rate)))
ditwin = np.concatenate((cos_rise,np.ones(dit.size-cos_rise.size-cos_fall.size),cos_fall))
dahwin = np.concatenate((cos_rise,np.ones(dah.size-cos_rise.size-cos_fall.size),cos_fall))

# apply windowing functions
dit = dit*ditwin
dah = dah*dahwin # Darwin lol

# generate WAV files for all numbers
for k in range(10):
	sound = np.array([])
	for n in numbers[k]:
		if n == 0:
			sound = np.concatenate((sound,dit))
		else:
			sound = np.concatenate((sound,dah))

		sound = np.concatenate((sound,space))

	# add 2 more units after character for 3 units total character spacing
	sound = np.concatenate((sound,space))
	sound = np.concatenate((sound,space))

	wavfile.write("wav/"+str(k)+".wav",samp_rate,np.array(sound,dtype="float32"))

# generate another WAV file for inter word (7 unit) spacing
wordspace = np.array([])
for k in range(7):
	wordspace = np.concatenate((wordspace,space))
wavfile.write("wav/wordspace.wav",samp_rate,np.array(wordspace,dtype="float32"))
