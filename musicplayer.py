from os import system as sys
from os import chdir
import subprocess
from song import Song

class MusicPlayer:
    def __init__(self):
        self.path = path
	        
    def shuffle():
	sys("mpc shuffle")

    def get_now_playing():
	out_string = subprocess.check_output("mpc current")
	out_list = out_string.split(" - ")
	artist = out_list[0]
	song = out_list[1]

	return Song(artist, album, song)
	
    def volume_adjust(value):
	'''Changes the volume by value (+-)'''
	if value == 0:
	    return
        sys("mpc volume " + str(value))

    def volume_set(value):
        '''Sets the volume to a value 0-100'''
	if value == 0:
	    return
        sys("mpc volume " + str(value))
    
    def stop():
	'''Stops music'''
	sys("mpc stop")

