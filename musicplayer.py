from os import system as sys
from os import chdir
import subprocess
from song import Song

class MusicPlayer:
    '''A class to contain all the functions related to mpc'''
    def __init__(self):
	print "Created MusicPlayer instance"

    def shuffle(self):
	sys("mpc shuffle")

    def get_now_playing(self):
	out_string = subprocess.check_output("mpc current")
	out_list = out_string.split(" - ")
	artist = out_list[0]
	song = out_list[1]

	return Song(artist, album, song)
	
    def volume_adjust(self, value):
	'''Changes the volume by value (+-)'''
	if value == 0:
	    return
        sys("mpc volume " + value)

    def volume_set(self, value):
        '''Sets the volume to a value 0-100'''
	if value == 0:
	    return
        sys("mpc volume " + str(value))
    
    def stop(self):
	'''Stops music'''
	sys("mpc stop")
    
    def mute(self):
	'''Mutes music'''
	sys("mpc volume 0")
    
    def pause(self):
	'''Pauses music'''
	sys("mpc pause")

