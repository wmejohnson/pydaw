# William Johnson
# pyDaw track class

import sound
import clip
import numpy
import scipy.io.wavfile
import os

class track(sound.sound):
    
    def __init__(self, name, length, sr):
	self.name = name
	self.length = length
	self.sr = sr
	self.clips = numpy.array([])
	self.data = numpy.zeros(self.length * self.sr)
	self.pan = 0.5
	self.volume = 1.0
	
    def __repr__(self):
	return "<TRACK: Name: %s, Volume: %s>" % (self.name, self.volume)

    def add_clip(self, clip, start_second):
	#add a sound at time index
	start_sample = self.sr*start_second
	end_sample = start_sample + (clip.length*self.sr)
	clip.start_sample = start_sample
	clip.end_sample = end_sample
	self.clips = numpy.append(self.clips, [clip])
	
    def remove_clip(self, clip_array_index):
	#remove a sound at array index 
	del self.clips[clip_array_index]
	
    def erase_data(self):
	self.data = numpy.zeros(self.length*self.sr)

    def render(self):
	for clip in self.clips:
	    self.data[clip.start_sample:clip.end_sample] = clip.data
	self.data *= self.volume
	scipy.io.wavfile.write("../temp/"+self.name+".wav", self.sr, self.data)

    def play(self):
	self.render()
	os.system("paplay ../temp/"+self.name+".wav")
