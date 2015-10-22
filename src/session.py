# William Johnson - pyDaw
# session class - the main way of working with pyDaw
# container for tracks and bouncing methods 

class Session(track.py):

    def __init__(self, name, sr=44100):
	self.tracks = []
	self.sr = sr

    def bounce(self):
	#bounce the session to a single audio file

    def play(self):
	#play the entire session
