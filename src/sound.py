# Will Johnson
# Sound class for pyDaw

import numpy
import os
import scipy.io.wavfile

class sound:
    
    def __init__(self, name="sound", sr=44100, data=numpy.zeros(44100)):
	self.name = name
	self.sr = sr
	self.data = data
	self.channels = self.get_n_channels()
	self.length = self.get_length_s()

    def __repr__(self):
	return "<SOUND: Name: %s, Channels %s, Sample Rate: %s, Length: %s seconds>" % (self.name, self.channels, self.sr, self.length) 
    
    def get_length_s(self):
	return len(self.data)/float(self.sr)

    def normalized(self, ceiling=0.9):
	max_sample = numpy.max(abs(self.data))
	scalar = ceiling/float(max_sample)
	data = self.data.astype(float)
	data *= scalar
	return data

    def normalize(self, ceiling=0.9):
	max_sample = numpy.max(abs(self.data))
	scalar = ceiling/float(max_sample)
	data = self.data.astype(float)
	data *= scalar
	self.data = data    
 
    def fade_in(self, len_sec):
	len_samp = len_sec *self.sr
	self.data[:len_samp] = numpy.arange(len_samp, self.data[len_samp]/len_samp)

    def fade_out(self, len_sec):
	len_samp = len_sec *self.sr
	ramp = numpy.arange(len_samp, self.data[:-len_samp]/len_samp)
	numpy.fliplr(ramp)
	self.data[-len_samp:] = ramp

    def reverse(self):
	self.data = self.data[::-1]    

    def reversed(self):
	return self.data[::-1]

    def play(self):
	self.render()
	os.system("paplay ../temp/"+self.name+".wav") 

    def render(self):
	scipy.io.wavfile.write("../temp/"+self.name+".wav", self.sr, self.data)
