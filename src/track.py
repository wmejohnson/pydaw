# William Johnson
# pyDaw track class

import sound
import numpy

class track(sound.py):
    
    def __init__(self, length, sr):
	self.length = length
	self.volume = 1.0
	self.sounds = []
	self.pan = 0.5
	self.sr = sr
	self.data = numpy.zeros(length*sr) 
	
    def add_sound(self, sound, start_point):
	#add a sound at time index
	self.sounds.append([sound, start_point])
	start_sample = self.sr/start_point
	end_sample = start_sample + (sound.length*self.sr)
	self.data[start_sample:end_sample] = sound.data
	
    def remove_sound(self, sound_array_index):
	#remove a sound a time index 
	return
	
    def erase_data(self):
	self.data = numpy.zeros(self.length*self.sr)
