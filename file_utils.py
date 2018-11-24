import media
import os
import sys

def load_media(location):
	media = []
	try:
		with open(location, "r") as f:
			for line in f.readlines():


	except Exception as e:
		print("There was an error reading from file", location)
		return media
	return media
