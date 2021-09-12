import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("lounge", 8, 100, 5) 
        self.song_1 = Song("Daft Punk", "Da Funk")
        self.song_2 = Song("David Bowie", "Let's Dance")
        self.song_3 = Song("Talking Heads", "Once in a lifetime")
        self.song_3 = Song("P.H.D", "Wont let you down")
        self.guest_1 = Guest("Katy", 20)
        self.guest_2 = Guest("Ryan", 30)
        self.till = Room("lounge", 8, 100, 5)
        self.entry_fee = Room("lounge", 8, 100, 5)

    def test_room_has_name(self):
        self.assertEqual("lounge", self.room.name)

    def test_room_can_add_songs(self):
        self.room.add_song(self.song_1)
        self.assertEqual(1, self.room.song_count())

    def test_room_starts_empty(self):
        self.assertEqual(0, self.room.guest_count())

    def test_can_check_in_guest(self):
        self.room.check_in(self.room.guest)
        self.assertEqual(1, self.room.guest_count())

    def test_can_check_out_guest(self):
        self.room.check_in(self.room.guest)
        self.room.check_out(self.room.guest)
        self.assertEqual(0, self.room.guest_count())
    
    def test_can_empty_room(self):
        guest = Guest("Katy", 20)
        self.room.check_in(guest)
        self.room.empty()
        self.assertEqual(0, self.room.guest_count())
# EXTENSIONS
    def test_room_capacity(self):
        self.room.check_in(self.room.guest)
        self.room.check_in(self.room.guest)
        self.room.check_in(self.room.guest)
        self.room.check_in(self.room.guest)
        self.room.check_in(self.room.guest)
        self.room.check_in(self.room.guest)
        self.room.check_in(self.room.guest)
        self.room.check_in(self.room.guest)
        self.room.check_in(self.room.guest)
        self.room.check_in(self.room.guest)
        self.assertEqual(8, self.room.guest_count())
    
    
    