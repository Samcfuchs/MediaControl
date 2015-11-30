from os import system as sys
from os import chdir
import subprocess
from song import Song

class MusicPlayer:
    '''A class to contain all the functions related to mpc'''
    def __init__(self):
	sys("mpc update")

    def get_volume(self):
	command = ["mpc", "volume"]
	p = subprocess.Popen(command, stdout=subprocess.PIPE)
	raw_out = p.stdout.read()
	retcode = p.wait

	number = raw_out[8:10]
	return number
	
    def get_now_playing(self):
	command = ["mpc", "current"]
	p = subprocess.Popen(command, stdout=subprocess.PIPE)
	raw_out = p.stdout.read()
	retcode = p.wait

	out_list = raw_out.split(" - ")
	artist = out_list[0]
	song = out_list[1]

	return Song(artist, album, song)

    def shuffle(self):
	sys("mpc shuffle")
	
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
	#self.say("Music muted")
    
    def toggle_pause(self):
	'''Pauses music'''
	sys("mpc toggle")

    def pause(self):
	'''Pauses music'''
	sys("mpc pause")

    def say(self, statement):
	'''Uses espeak to say something'''
	self.pause()
	sys("espeak \"" + statement + "\"")
	self.toggle_pause()

    def next_song(self):
	'''Goes to next song on playlist'''
	sys("mpc next")

    def previous_song(self):
	'''Goes to previous song on playlist'''
	sys("mpc prev")
