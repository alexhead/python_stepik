class Song:
	def __init__(self, artist, song):
		self.artist = artist
		self.song = song
		self.tags = []

	def add_tags(self, *args):
		self.tags.extend(args)

song1 = Song("Skakey Graves", "Roll the Bones")
song1.add_tags("Americana", "Country")

song2 = Song("Neromonah Feofan", "Holodno v lesu")
song2.add_tags("Russina", "Drum'n'base")

print(song1.tags)
print(song2.tags)