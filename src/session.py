# William Johnson - pyDaw
# session class - the main way of working with pyDaw
# container for tracks and bouncing methods 

import track
import sound
import clip
import numpy

class session(sound.sound):

    def __init__(self, name, length, sr=44100):
	self.tracks = numpy.array([])
	self.sr = sr
	self.length = length
	self.data = numpy.array([])
	
    def add_track(self, name):
	self.tracks.append(track.track(name, self.length, self.sr))

    def render(self):
	#bounce the session to a single audio file
	for track in self.tracks:
	    track.render()
	self.data = sum(tracks)
	
