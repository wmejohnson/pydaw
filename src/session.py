# William Johnson - pyDaw
# session class - the main way of working with pyDaw
# container for tracks and bouncing methods 

import track
import sound
import clip
import numpy
import scipy.io.wavfile

class session(sound.sound):

    def __init__(self, name, length, sr=44100):
	self.name = name
	self.tracks = numpy.array([])
	self.sr = sr
	self.length = length
	self.data = numpy.zeros(self.sr * self.length)
	self.master_volume = 1.0
    
    def __repr__(self):
	return "<SESSION: Name: %s , Length: %s , Master Volume: %s>" % (self.name, self.length, self.master_volume)
    
    def add_track(self, name):
	new_track = track.track(name, self.length, self.sr)
	self.tracks = numpy.append(self.tracks, [new_track])
	return new_track
    
    def render(self):
	for track in self.tracks:
	    track.render()
	    self.data += track.data
	self.data /= len(self.tracks)
	self.data *= self.master_volume
	scipy.io.wavfile.write("../temp/"+self.name+".wav", self.sr, self.data)
