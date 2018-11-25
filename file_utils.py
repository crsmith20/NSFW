import media
import os
import sys

def load_media_record(location):
	media = []
	try:
		with open(location, "r") as f:
			for line in f.readlines():
				words = line.split(",", 3)
				m = media.Media(words[0], words[1], words[2])
				tags = words[3].split(",")
				m.setTags(tags)
				media.append(m)
	except Exception as e:
		print("There was an error reading from file", location "\n", e)
		return media
	return media

def create_media_record(location, media_locs):
	try:
		with open(location, "w") as f:
			for loc in media_locs:
				if os.path.isfile(loc):
					file, ext = os.path.splitext(loc)
					f.write(ext.strip(".") + "," + getname(file) + "," + loc + ",")
				else:
					media_locs.extend(os.listdir(loc))
	except Exception as e:
		print("There was an error reading from file", loc "\n", e)print("There was an error reading from file", location "\n", e)

def getname(title):
	parts = title.split("/")
	return parts[len(parts) - 1]