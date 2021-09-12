class Song:
    def __init__(self, artist, title):
        self.artist = artist
        self.title = title
        self.song = []

    def song_count(self):
        return len(self.song)