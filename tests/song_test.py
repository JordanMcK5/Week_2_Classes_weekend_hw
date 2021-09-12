import unittest
from src.song import Song



class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Daft Punk", "Da Funk")

    def test_song_by_title(self):
        self.assertEqual("Da Funk", self.song.title)

    def test_song_has_artist(self):
        self.assertEqual("Daft Punk", self.song.artist)
