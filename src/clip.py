# Will Johnson
# clip class for pyDaw

import sound
import numpy
import os
import scipy.io.wavfile

class clip(sound.sound):

    def __init__(self, name="clip", sr=44100, data=numpy.zeros(44100)):
	self.name = name
	self.sr = sr
	self.data = data
	self.channels = self.get_n_channels()
	self.length = self.get_length_s()

    def __repr__(self):
	return "<CLIP: Name: %s, Channels %s, Sample Rate: %s, Length %s seconds>" % (self.name, self.channels, self.sr, self.length)

    def read_from_file(self, filename):
        self.name = filename[:-4]
        self.sr = scipy.io.wavfile.read(filename)[0]
        self.data = scipy.io.wavfile.read(filename)[1]
        self.channels = self.get_n_channels()
        self.length = self.get_length_s()

    def concat(self, other_clip):
	if self.sr != other_sound.sr:
	    print "warning, sample rate mismatch"
	return clip(self.name+"_concat"+other_clip.name, self.sr, numpy.concatenate((self.data, other_clip.data)))

    def toMono(self):
        if self.channels > 1:
            temp = 0
            mono_data = []
            for s in self.data:
                for c in s:
                    temp += c
                temp = temp/self.channels
                mono_data.append(temp)
            mono_data = self.normalized()
            self.data = mono_data
        else:
            return

    def get_n_channels(self):
        if type(self.data[0]) != numpy.ndarray:
            return 1
        else:
            return len(self.data[0])

    def read_from_file(self, filename):
        self.name = filename[:-4]
        self.sr = scipy.io.wavfile.read(filename)[0]
        self.data = scipy.io.wavfile.read(filename)[1]
        self.channels = self.get_n_channels()
        self.length = self.get_length_s()

