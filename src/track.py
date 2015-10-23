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
	self.volume = 1.0
	self.clips = []
	self.pan = 0.5
	self.sr = sr
	self.data = numpy.zeros(length*sr) 
	
    def add_clip(self, clip, start_point):
	#add a sound at time index
	start_sample = self.sr/start_point
	end_sample = start_sample + (sound.length*self.sr)
	self.clips.append([sound, start_sample, end_sample])
	
    def remove_clip(self, clip_array_index):
	#remove a sound at array index 
	del self.clips[clip_array_index]
	
    def erase_data(self):
	self.data = numpy.zeros(self.length*self.sr)

    def render(self):
	for t in self.clips:
	    self.data[1:2] = sound.data
	scipy.io.wavfile.write("../temp/"+self.name+".wav", self.sr, self.data)

    def play(self):
	self.render()
	os.system("paplay ../temp/"+self.name+".wav")
