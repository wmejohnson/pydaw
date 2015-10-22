# William Johnson - pyDaw
# session class - the main way of working with pyDaw
# container for tracks and bouncing methods 

import track

class Session():

    def __init__(self, name, sr=44100, length):
	self.tracks = []
	self.sr = sr
	self.length = length
	
    def add_track(self):
	self.tracks.append(track.track(self.length))

    def bounce(self):
	#bounce the session to a single audio file

    def play(self):
	#play the entire session
